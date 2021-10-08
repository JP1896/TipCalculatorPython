import Functions as fun

print('WELCOME TO THE TIP CALCULATOR APP')
print('Enter the Bill : ')
amount = float(input()) #Amount to pay original
print('Amount : $', amount)
print('Tip % : ')
per = float(input())
print('Tip % : ', per, '%')
print('Number of people : ')
people = int(input())
print('Number of people: ', people)

if people == 1:
    fun.getTipPerson(amount,per,people)
else:
    fun.getTipPeople(amount,per,people)
