import random as rd
sentence = input("write your sentence\n")
newsent = ""
for i in range(len(sentence)):
  randint = rd.randint(1, 100)
  if randint < 55:
    newsent = newsent + sentence[i].upper()
  else:
    newsent = newsent + sentence[i].lower()
print(str(newsent))