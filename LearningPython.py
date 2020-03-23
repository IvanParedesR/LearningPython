#Para correr en R.
# Basado en ejercicios y problemas de  Exploring Data Using Python 3. Dr. Charles R. Severance

#remotes::install_github("rstudio/reticulate")
# Se carga la libreria reticulate
library(reticulate)

print(4) #imrpime el número 4
type('Hello, World!') #Da el tipo de dato
print(1,000,000)

message = 'And now for something completely different'
n = 17
print(n)
pi = 3.1415926535897931

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
name = input('What is your name?\n')
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
