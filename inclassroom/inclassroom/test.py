# Read an integer:
'''
month = int(input())
day = int(input())

if month == 1 or month ==3 or month==5 or month ==7 or month==8 :
  if day <31 :
    print('A')
    print(month)
    print(day+1)
  elif day>=31:
    print('B')
    print(month+1)
    print(day-32)
elif month ==10:
  if day <31 :
    print('C')
    print(month)
    print(day+1)
  elif day>=31:
    print('D')
    print(month+1)
    print(day-32)
elif month == 4 or month== 6 or month== 9 or month==11:
  if day <30 :
    print('E')
    print(month)
    print(day+1)
  elif day>=30:
    print('F')
    print(month+1)
    print(day-31)

elif month == 12:
  if day <31 :
    print('G')
    print(month)
    print(day+1)
  elif day>=31:
    print('H')
    print(month-12)
    print(day-32)
elif month == 2:
  if day <=27 :
    print('1')
    print(month)
    print(day+1)
  elif day>27 :
    print('2')
    print(month+1)
    print((day-28)+1)
'''


def linear(a,b):

  if a == 0:
    if b == 0:
      return'many solutions'
    else:
      return 'no solution'
  elif b % a == 0:
    return(b // a)
  else:
    return 'no solution'

a = int(input())
b = int(input())
print(linear(a,b))