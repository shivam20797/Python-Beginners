
# function for count vowels and consonants
# used this ['a','e','i','o','u'] or "aeiou"

def count_vowels(str=""):
  countVowel = 0
  countConso = 0
  for char in str:
    if char.isalpha():  
      if char.lower() in "aeiou":
        countVowel = countVowel + 1
      else :
        countConso = countConso + 1

  print(f"Total vowels {countVowel} and Total consonants {countConso}",)    

count_vowels("Shivam123")  


def count_vowels1(str=""):
  countVowel = 0
  countConso = 0
  for char in str:
    if char.isalpha():  
      if char.lower() in "aeiou":
        countVowel = countVowel + 1
      else :
        countConso = countConso + 1

  return countVowel,countConso  

vowels,Consos = count_vowels1("Shivam123")
print(f"Total vowels {vowels} and Total consonants {Consos}",)     