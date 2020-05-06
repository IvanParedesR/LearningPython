cheeses = ['Cheddar', 'Edam', 'Gouda']
numbers = [17, 123]
empty = []
print(cheeses, numbers, empty)

print(cheeses[0])

numbers = [17, 123]
print(numbers)

for cheese in cheeses:
  print(cheese)

for i in range(len(numbers)):
  numbers[i] = numbers[i] * 2

for x in empty:
  print('This never happens.')
  
# Use words.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
for i in fh:
    i = i.rstrip().upper()
    print i
    
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b*2 
print(c)

t = ['a', 'b', 'c', 'd', 'e', 'f']
t[1:3]

t = ['a', 'b', 'c']
t.append('d')
print(t)

t1 = ['a', 'b', 'c']
t2 = ['d', 'e']
t1.extend(t2)
print(t1)

t = ['d', 'c', 'e', 'b', 'a']
t.sort()
print(t)


t = ['a', 'b', 'c']
x = t.pop(1)
print(t)
['a', 'c']
print(x)

t = ['a', 'b', 'c']
del t[1]
print(t)

t = ['a', 'b', 'c']
t.remove('b')
print(t)

t = ['a', 'b', 'c', 'd', 'e', 'f']
del t[1:5]
print(t)

nums = [3, 41, 12, 9, 74, 15]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))


total = 0
count = 0
while (True):
  inp = input('Enter a number: ')
  if inp == 'done': break
  value = float(inp)
  total = total + value
  count = count + 1
  
average = total / count
print('Average:', average)

numlist = list()
while (True):
  inp = input('Enter a number: ')
  if inp == 'done': break
  value = float(inp)
    numlist.append(value)
    
average = sum(numlist) / len(numlist)
print('Average:', average)

s = 'spam es una basura pero que podemos hacer'
t = list(s)
print(t)

s = 'pining for the fjords'
t = s.split()
print(t)

print(t[3])

t = ['pining', 'for', 'the', 'fjords']
delimiter = ' '
delimiter.join(t)


#^	Matches the beginning of a line
#$	Matches the end of the line
#.	Matches any character
#\s	Matches whitespace
#\S	Matches any non-whitespace character
#*	Repeats a character zero or more times
#*?	Repeats a character zero or more times (non-greedy)
#+	Repeats a character one or more times
#+?	Repeats a character one or more times (non-greedy)
#[aeiou]	Matches a single character in the listed set
#[^XYZ]	Matches a single character not in the listed set
#[a-z0-9]	The set of characters can include a range
#(	Indicates where string extraction is to start
#)	Indicates where string extraction is to end


import re
hand = open('mbox.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:', line):
          print(line)

# Search for lines that start with 'From'
import re
hand = open('mbox.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line):
        print(line)
        
hand = open('mbox.txt')        
for line in hand:
    line = line.rstrip()
    if re.search('^F..m:', line):
        print(line)
        
hand = open('mbox.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:.+@', line):
      print(line)

import re
s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\S+@\S+', s)
print(lst)

# Search for lines that have an at sign between characters
import re
hand = open('mbox.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('\S+@\S+', line)
    if len(x) > 0:
        print(x)

# Search for lines that have an at sign between characters
# The characters must be a letter or number
import re
hand = open('mbox.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('[a-zA-Z0-9]\S+@\S+[a-zA-Z]', line)
    if len(x) > 0:
        print(x)

# Search for lines that start with 'X' followed by any non
# whitespace characters and ':'
# followed by a space and any number.
# The number can include a decimal.
hand = open('mbox.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^X\S*: [0-9.]+', line):
        print(line)
        

# Search for lines that start with 'X' followed by any
# non whitespace characters and ':' followed by a space
# and any number. The number can include a decimal.
# Then print the number if it is greater than zero.
import re
hand = open('mbox.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^X\S*: ([0-9.]+)', line)
    if len(x) > 0:
        print(x)
        
# Search for lines that start with 'Details: rev='
# followed by numbers and '.'
# Then print the number if it is greater than zero
import re
hand = open('mbox.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^Details:.*rev=([0-9.]+)', line)
    if len(x) > 0:
        print(x)
        
# Search for lines that start with From and a character
# followed by a two digit number between 00 and 99 followed by ':'
# Then print the number if it is greater than zero
import re
hand = open('mbox.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^From .* ([0-9][0-9]):', line)
    if len(x) > 0: print(x)
    
x = 'We just received $10.00 for cookies.'
y = re.findall('\$[0-9.]+',x)
