# expenses=[
#   ["January","February","March","April","May"],
#   [2200,2350,2600,2130,2190]
# ]

# print(type(expenses))

expenses= [2200,2350,2600,2130,2190]

# 1. In Feb, how many dollars you spent extra compare to January?

print("In February this much extra dollers i spent = ", expenses[1]-expenses[0])

# 2. Find out your total expense in first quarter (first three months) of the year

total= 0
for item in expenses[:3]:
    total = total+item

print("Total expense in 1st 4 months is : ", total)


# 3. Find out if you spent exactly 2000 dollars in any month

print("Did i spent $2000 in any month of the 1st 5 of 2024 : ", 2000 in expenses)

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list

expenses.append(1980)
print(expenses)

# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this

expenses[3]= expenses[3]-200
print(expenses)


# 2. You have a list of your favourite marvel super heros
# heros=['spider man','thor','hulk','iron man','captain america']
# Using this list

heros=['spider man','thor','hulk','iron man','captain america']
# 1. Length of the list
print(len(heros))
# 2. Add 'black panther' at the end of this list
heros.append('black panther')
print(heros)
# 3. You realize that you need to add 'black panther' after 'hulk',
# so remove it from the list first and then add it after 'hulk'
heros.remove('black panther')
heros.insert(3,'black panther')
print(heros)
# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
heros[1:3]=['doctor strange']
print(heros)
# 5. Sort the list in alphabetical order
heros.sort()
print(heros)

#Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function

userInput=int(input("Enter a max number : "))

odd_Numbers=[]

for i in range(1,userInput):
  if i % 2 ==0:
    odd_Numbers.append(i)

print("Odd Numbers : ", odd_Numbers)



