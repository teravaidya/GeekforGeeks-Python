# GeekforGeeks-Python
#login to your azure subscription
az login

#see your subscriptions
az account list

#set active subscription if you have more than one
az account set --name "pcs-krvt-a006b2-dev-01"

# general
$location = "australiaeast"
$aksrg = "t3-mes-dev-dev-nsw-rg"

# VNET##
#$vnet = "cluster-vnet"
$vnet_address_range = "10.0.0.0/16"

# aks subnet
$akssn = "aks-sn"
$aks_cidr = "10.0.0.0/23"

# aks
$aks = "saea3krvtacr01"
$aks_srv_cidr = "10.0.0.0/16"
#$aks_dns_ip = "192.168.6.10"
$aks_pod_cidr = "10.244.0.0/16"
$aks_docker_bridge = "10.0.2.1/16"

# acr
$registry = "saea3krvtacr01"

# create the resource group - Already exists
az group create --name $aksrg --location $location

# define a VNET - Already exists
az network vnet create --name $vnet --resource-group $aksrg --address-prefixes 
$vnet_address_range

# create the AKS subnet inside the vnet
az network vnet subnet create -g $aksrg --vnet-name $vnet -n $akssn --address-prefixes $aks_cidr

# get id of the vnet
$vnetid = $(az network vnet show -n $vnet -g $aksrg --query id --output tsv)

# get the id of the subnet
$akssnid = $(az network vnet subnet show -g $aksrg --vnet-name $vnet -n $akssn --query id --output tsv)

#create the service prinsipal and store the output in a json file
$outputfile = "aks_sp.json"
$filecontent = $(az ad sp create-for-rbac --skip-assignment --name "${aks}_sp" --output json)
$Utf8NoBomEncoding = New-Object System.Text.UTF8Encoding $False
[System.IO.File]::WriteAllLines($outputfile, $filecontent, $Utf8NoBomEncoding)


#read the values from the json file
$aks_appid = $(jq -r ".appId" $outputfile)
$aks_secret = $(jq -r ".password" $outputfile)

#ZzzzZZz
Start-Sleep -s 10
az role assignment create --assignee $aks_appid --scope $vnetid --role Contributor

# optional create Azure Container Registry
az acr create --name $registry --resource-group $aksrg --sku basic

#create the aks service (remove linebreaks before running
az aks create --resource-group $aksrg \
       --name $aks \
       --attach-acr $registry \
       --node-count 3 \
       --network-plugin kubenet \
       --service-cidr $aks_srv_cidr \
       #--dns-service-ip $aks_dns_ip \
       --pod-cidr $aks_pod_cidr \
       --docker-bridge-address $aks_docker_bridge \
       #--vnet-subnet-id $akssnid \
       #--service-principal $aks_appid \
       --client-secret $aks_secret

# get the aks resource id
$aks_resourceId = $(az aks show -n $aks -g $aksrg --query id -o tsv)

# wait for aks to be up and running
az resource wait --exists --ids $aks_resourceId

az aks get-credentials --resource-group $aksrg --name $aks  --overwrite-existing
