def vowel_count(s):
  """Counts the number of vowels in s and returns the same
  Ignores case of letters"""
  VOWELS = "aeiouAEIOU"
  vc = 0
  for ch in s:
    if ch in VOWELS:
      vc += 1
  return vc


if __name__ == "__main__":
  print(vowel_count("GFG is the best platform to learn from."))
