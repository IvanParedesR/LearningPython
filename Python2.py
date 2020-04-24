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

