# Creating a List
List1 = []
print(len(List1))

List2 = [10, 20, 14]
print(len(List2))

f = [1, 1, 2, 3, 5, 8]
p = [2, 3, 5, 7]
grading = ["Tests", "Quizzes", "Individual Labs", "Group Labs", "Hackathons"]
grades = [300, 60, 120, 60, 120]
oddjob = [1, 5.6, True, 4-7j, "Hello", [1, 2], [3.9, "World"]]
print(len(grading))
print(sum(f), sum(p))

grading = ["Tests", "Quizzes", "Individual Labs", "Group Labs", "Hackathons"]
grades = [300, 60, 120, 60, 120]
oddJob = [1, 5.6, True, 4-7j, "Hello", [1, 2], [3.9, "World"]]
# We access individual elements using the index
# The first element is at index 0
print(grades[1], oddJob[4])
# We access the elements from the back using negative indices
# -1 is the last, -2 is the last but one and so on
print(grading[-1], grading[-3])
print(max(grades), min(grades))

# Python program to take space separated input as a string
# split and store it to a list and print the string list

# input the list as string

string = input("Enter elements of a list (Space-separated): ")
lst = string.split()            # split the strings and store it to a list
print("The list is: ", lst)     # printing the list

# Python program to store integers in a list in one line

# input size of the list
n = int(input("Enter the size of list: "))
# store integers in a list using map, split and strip functions
lst = list(map(int, input("Enter the integer elements of list(Space-Separated): ").strip().split()))[:n]
print('The list is:', lst)   # printing the list


