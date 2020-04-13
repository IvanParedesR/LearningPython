# Se corre en RStudio, de ahí que se use reticulate
#remotes::install_github("rstudio/reticulate")
library(reticulate)
# imprimir
print(4)
# solo toma los 0
print(1,000,000)

# Tipo de variable
type('Hello, World!')
# String
type(5)
# number
type(7.65)
# float
message = 'And now for something completely different'
n = 17

print(n)

pi = 3.1415926535897931

empty_list = list()
also_empty_list = []

zeros_list = [0] * 5
print(zeros_list)

print(1)
x = 2
print(x)
20+32
hour = 10
hour-1
minute = 13
hour*60+minute
minute/60
5**2
(5+9)*(15-7)

first = 10
second = 15
print(first+second)

indp = input()
#comentarios
name = input('What is your name?')
print(name)

a = 35.0
b = 12.50
c = a * b
print(c)

hours = 35.0
rate = 12.50
pay = hours * rate
print(pay)

name = input('What is your name?\n')
print("Hello",name)

x = 5
y = 3
x != y # x is not equal to y
x > y # x is greater than y
x < y # x is less than y
x >= y # x is greater than or equal to y
x <= y # x is less than or equal to y
x is y # x is the same as y
x is not y # x is not the same as y

if x > 0 :
  print('x is positive')
  
x = 6
if x < 10:
  print('Small')

if x%2 == 0 :
  print('x es par')
else :
  print('x es impar')
 
 
x = 3
y = 7
  if x < y:
  print('x es menos que y')
elif x > y:
  print('x es mas que y')
else:
  print('x y y son iguales')
  
choice = "a"  
if choice == 'a':
  print('Bad guess')
elif choice == 'b':
  print('Good guess')
elif choice == 'c':
  print('Close, but not correct')  
  
  
  if x == y:
  print('x and y are equal')
else:
  if x < y:
    print('x is less than y')
  else:
    print('x is greater than y')
    
if 0 < x:
  if x < 10:
    print('x es un numero positivo.')

x = 11    
if 0 < x and x < 10:
  print('x es un número positivo de un digito')
else:
    print('x es mayor')
    
inp = input('Enter Fahrenheit Temperature: ')
fahr = float(inp)
cel = (fahr - 32.0) * 5.0 / 9.0
print(cel)

inp = input('Enter Fahrenheit Temperature:')
try:
  fahr = float(inp)
  cel = (fahr - 32.0) * 5.0 / 9.0
  print(cel)
except:
  print('Please enter a number')
  
x = 6
y = 2
x >= 2 and (x/y) > 2

type(32)

max('Hello world')

min('aHello world')

len('Hello world')

int(3.99999)

float(32)

import math
print(math)

ratio = signal_power / noise_power
decibels = 10 * math.log10(ratio)
radians = 0.7
height = math.sin(radians)

degrees = 45
radians = degrees / 360.0 * 2 * math.pi
math.sin(radians)

math.sqrt(16) / 2.0

import random
for i in range(10):
  x = random.random()
  print(x)
  
def print_lyrics():
  print("I'm a lumberjack, and I'm okay.")
  print('I sleep all night and I work all day.')
  
def repeat_lyrics():
  print_lyrics()
  print_lyrics()

repeat_lyrics() 

def print_twice(bruce):
  print(bruce)
  print(bruce)
  
print_twice('Spam')
print_twice('Spam '*4)

print_twice(math.cos(math.pi))

michael = 'Eric, the half a bee.'
print_twice(michael)

x = math.cos(radians)
golden = (math.sqrt(5) + 1) / 2

n = 20
while n > -10:
  print(n)
  n = n - 1
  print('Blastoff!')
  
#no sé que hace
while True:
  line = input('> ')
  if line[0] == '#':
    continue
if line == 'done':
    break
  print(line)
print('Done!')


friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
  print('Happy New Year:', friend)
print('Done!')


for friend in friends:
  print('Happy New Year:', friend)
  
count = 0
for itervar in [3, 41, 12, 9, 74, 15]:
  count = count + 1
print('Contado: ', count)

total = 0
for itervar in [3, 4, 1, 1, 1, 1]:
  total = total + itervar
print('Total: ', total)


largest = None
print('Before:', largest)
for itervar in [3, 41, 12, 9, 74, 15]:
  if largest is None or itervar > largest :
    largest = itervar
  print('Loop:', itervar, largest)
print('Largest:', largest)


smallest = None
print('Before:', smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
  if smallest is None or itervar < smallest:
    smallest = itervar
  print('Loop:', itervar, smallest)
print('Smallest:', smallest)

def min(values):
smallest = None
for value in values:
  if smallest is None or value < smallest:
    smallest = value
  return smallest
  
fruit = 'banana'
letter = fruit[5]
print(letter)
len(fruit)

length = len(fruit)
last = fruit[length-1]
print(last)

### duda

index = 0
while index < len(fruit):
  letter = fruit[index]
  print(letter)
  index = index + 1

for char in fruit:
  print(char)

tot = 0 
for i in [5, 4, 3, 2, 1] :
    tot = tot + 1
print(tot)

zork = 0
for thing in [9, 41, 12, 3, 74, 15] :
    zork = zork + thing
print('After', zork)

smallest_so_far = -1
for the_num in [9, 41, 12, 3, 74, 15] :
   if the_num < smallest_so_far :
      smallest_so_far = the_num
print(smallest_so_far)

if smallest is None :
     smallest = value
     
n = 0
while n > 0 :
    print('Lather')
    print('Rinse')
print('Dry off!')

s = 'Monty Python'
print(s[0:5])

fruit = 'banana'
fruit[:3]
fruit[3:]

#If the first index is greater than or equal to the second the result is an empty string, represented by two quotation marks:
fruit = 'banana'
fruit[3:3]
fruit[1:4]

greeting = 'Hello, world!'
new_greeting = 'J' + greeting[5:11]
print(new_greeting)

word = 'banana'
count = 0
for letter in word:
  if letter == 'a':
    count = count + 1
print(count)

'a' in 'banana'

if word == 'banana':
  print('All right, bananas.')
  
word = "aineaple"
if word < 'banana':
  print('Your word, ' + word + ', comes before banana.')
elif word > 'banana':
  print('Your word, ' + word + ', comes after banana.')
else:
  print('All right, bananas.')

stuff = 'Hello world'
type(stuff)
<class 'str'>
dir(stuff)

capitalize(...)
  S.capitalize() -> str

word = 'banana'
new_word = word.upper()
print(new_word)

word = 'banana'
index = word.find('a')
print(index)

word.find('na')


n = 5
while n > 0 :
   print(n)
print('All done')


str1 = "Hello"
str2 = 'there'
bob = str1 + " " + str2
print(bob)

x = '40'
y = int(x) + 2
print(y)

x = 'From marquard@uct.ac.za'
print(len('banana')*7)

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(data[pos:pos+3])

#Exercise 1: Write a while loop that starts at the last character in the
#string and works its way backwards to the first character in the string,
#printing each letter on a separate line, except backwards.

fruit = "banana"
index = -5
while index < 1:
  letter = fruit[index]
  print(letter)
  index = index + 1

#Exercise 3: Encapsulate this code in a function named count, and gen-
#eralize it so that it accepts the string and the letter as arguments.
# checar

def countLetters(str, ch):
	fruit = str
	count = 0
	for char in fruit:
		if char == ch:
			count = count + 1
	print count
	
	countLetters('amigable', a)

#### Checar
def teste:
  word = input('ingrese palabra:')
  letra = input('ingrese letra:')
  count = 0
  for letter in word:
    if letter == 'a':
      count = count + 1
  print(count)
  
def addtwo(a, b):
  added = a + b
  return added
x = addtwo(3, 5)
print(x)

word = 'dios'
if word < 'banana':
  print('Your word,' + word + ', comes before banana.')
elif word > 'banana':
  print('Your word,' + word + ', comes after banana.')
else:
  print('All right, bananas.')

word = 'banana'
new_word = word.upper()
print(new_word)


#6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475";

spacePos = text.find(" ")
number = text[spacePos::1]
number
#not really necessary but since we are just learning and playing
strippedNumber = number.lstrip();
result = float(strippedNumber)

def reprint(printed):
    print(printed)  

reprint(result)

word.find('na')

word.find('na', 3)

line = ' Here we go      '
line.strip()

line = 'Have a nice day'
line.startswith('Have')
line.startswith('h')

line.lower()
'have a nice day'
line.lower().startswith('h')

data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('om')
print(atpos)

sppos = data.find(' ',atpos)
print(sppos)

host = data[atpos+1:sppos]
print(host)

camels = 42
'%d' % camels

'I have spotted %d camels.' % camels

'In %d years I have spotted %g %s.' % (3, 0.1, 'camels')

'%d %d %d' % (1, 2, 5)

#While the file handle does not contain the data for the file, it is quite easy to
#construct a for loop to read through and count each of the lines in a file:
  
fhand = open('C:/Users/iparedes/Documents/Clase/mbox.txt')
x = 0
for line in fhand:
       x = x + 1
print(x)
#no sale
inp = fhand.read()
print(len(inp))
print(inp[:20])

#7.5 Searching through a file
fhand = open('C:/Users/iparedes/Documents/Clase/mbox.txt')
count = 0
for line in fhand:
  if line.startswith('From:'):
    print(line)
  
for line in fhand:
    line = line.rstrip()
    # Skip 'uninteresting lines'
    if not line.startswith('From:'):
        continue
    # Process our 'interesting' line
    print(line)

for line in fhand:
    line = line.rstrip()
    if line.find('@uct.ac.za') == -1: continue
    print(line)


fname = input('Enter the file name: ')
fhand = open(fname)
count = 0
for line in fhand:
  if line.startswith('Subject:'):
    count = count + 1
  print('There were', count, 'subject lines in', fname)
  
fname = input('Enter the file name: ')
try:
fhand = open(fname)
except:
print('File cannot be opened:', fname)
exit()
count = 0
for line in fhand:
  if line.startswith('Subject:'):
    count = count + 1
  print('There were', count, 'subject lines in', fname)

# 7.1 Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case. Use the file words.txt to produce the output below.

# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
#Checar
print(text.upper()) 
