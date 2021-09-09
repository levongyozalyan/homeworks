"""IF, ELIF, ELSE"""

# 1. Enter your name, then find the sum of the ASCII values of the letters in your name. If that number is larger than
# 500, print "I've got a great name!", and "I've got a fancy name!" otherwise.
# Ներմուծեք ձեր անունը և գտեք անվան տառերի ASCII արժեքների գումարը։ Եթե թիվը մեծ է 500-ից, տպել "I've got a great
# name!", իսկ հակառակ դեպքում՝ "I've got a fancy name!"։

name = str(input('Enter your name:'))
name_sum = 0

for i in range(0, len(name)):
    name_sum = name_sum + ord(name[i])

if name_sum > 500:
    print('I\'ve got a fancy name!')

# 2. Ask the user for a movie title. If the title starts with a capital letter, print "Great title!", otherwise print
# "Titles start with capital letters...". If the input starts with a special character [!, @, #, $, %, ^, &], print "I
# doubt that this is a title.".
# Պահանջել ներմուծել ֆիլմի վերնագիր։ Եթե վերնագիրը սկսվում է մեծատառով, տպել "Great title!", հակառակ դեպքում տպել
# "Titles start with capital letters..."։ Եթե ներմուծվածը սկսվում է [!, @, #, $, %, ^, &] նշաններով, տպել "I doubt that
# this is a title."․

movie_title = str(input('What\'s your favourite movie:'))

if ord(movie_title[0]) in range(65, 91):
    print('Great title!')
elif ord(movie_title[0]) in range(33, 39):
    print('I doubt that this is a title.')


# 3. Ask the user to input his/her age. If the user is older than 18, than tell them they're eligible to vote. If they
# are younger than 18, tell them how many years do they have to wait.
# Հարցրեք օգտատիրոջ տարիքը։ Եթե նա 18 տարեկանից մեծ է, նրան տեղյակ պահեք, որ կարող է քվեարկել։ Հակառակ դեպքում ասեք, թե
# քանի տարուց նա կկարողանա դա անել։

age = int(input('Enter your age:'))

if age > 18:
    print('You\'re eligible to vote!')
else:
    print('You have to waite {} more years to vote.'.format(18-age))

# 4. Write a program that will tell us whether a given year is a leap year or not.
# Գրել ծրագիր, որը կտեղեկացնի, թե տրված տարին նահանջ է, թե ոչ։

year = int(input('Check the year:'))

if year % 400 == 0 or year % 100 != 0 and year % 4 == 0:
    print('{} is a leap year'.format(year))
else:
    print('{} is not a leap year'.format(year))

# 5. Using 'random' module, generate a random number between -1000 and 1000. If the number is positive, print positive.
# If it's negative, print negative along with the absolute value of the number.
# Օգտագործելով random գրադարանը, գեներացնել [-1000,1000]-ը տիրույթում պատահական թիվ։ Եթե թիվը դրական է, տպել positive.
# Հակառակ դեպքում տպել negative և այդ թվի բացարձակ արժեքը։

from random import randint

random_number = randint(-1000, 1000)

if random_number > 0:
    print('positive')
elif random_number < 0:
    print('negative', abs(random_number))
