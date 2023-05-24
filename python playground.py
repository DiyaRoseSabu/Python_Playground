print('hello world')

age = 7
if age < 18:
    print('minor')
elif age >= 18 and  age <= 65:
    print('adult')
else:
    print('senior citizen')

fruits = ['apple,banana,watermelon']
for fruits in fruits:
    print(fruits)
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

count = 1
while count <= 5:
    print('count', count)
    count += 1



