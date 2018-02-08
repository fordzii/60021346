a = int(input())
value = 1
max_value = 1
while not a == 0:
  pre , a = a, int(input())
  if pre == a:
    value +=1
  else:
    value +=0
    max_value = max(value,max_value)
print(max_value)
max