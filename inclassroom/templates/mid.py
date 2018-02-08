def median(num_1,num_2,num_3,num_4,num_5):
    sum_number = num_1+num_2+num_3+num_4+num_5
    return sum_number/5

def max_num(num_1,num_2,num_3,num_4,num_5):
    max1 = 0
    max2 = 0
    if num_1<num_2 :
        max1 = num_2
        max2 = num_1
    else:
        max1 = num_1
        max2 = num_2

    if max1 < num_3:
        max2 = max1
        max1 = num_3
    elif max2 < num_3:
        max2 = num_3
    if max1 < num_4:
        max2 = max1
        max1 = num_4
    elif max2 < num_4:
        max2 = num_4
    if max1 < num_5:
        max2 = max1
        max1 = num_5
    elif max2 < num_5:
        max2 = num_5
    print(max1,max2)



print(max_num(num_1 = int(input()),num_2 = int(input()),num_3 = int(input()),num_4 = int(input()),num_5 = int(input())))