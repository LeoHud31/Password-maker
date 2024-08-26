import random

def load_words():
    with open('pdictionary.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words
#numbers
num1 = random.randint(0,100)
num2 = random.randint(0,100)
num3 = random.randint(0,100)

#words
f = open ('pdictionary.txt')
word1 = f.read().split()
word1 = random.choice(word1)
word1 = word1.title()

f = open ('pdictionary.txt')
word2 = f.read().split()
word2 = random.choice(word2)
word2 = word2.title()

f = open ('pdictionary.txt')
word3 = f.read().split()
word3 = random.choice(word3)
word3 = word3.title()

#special characters
schar = random.randint(1, 4)
if schar == 1:
    scha = "+"
if schar == 2:
    scha = "-"
if schar == 3:
    scha = ","
if schar == 4:
    scha  = "."

#additioon of all the parts
p1 = word1 + str(num1) + str(scha)
p2 = word2 + str(num2)
p3 = word3 + str(num3) + str(scha)
passw = p1 + p2 + p3 
print("password is:", passw)