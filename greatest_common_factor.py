def gcf(small, large):
    if large % small == 0:
        return small
    elif small % 2 == 0:
        num = int(small / 2)
    else:
        num = int((small + 1) / 2)

    for factor in range(num, 0, -1):
        if large % factor == 0 and small % factor == 0:
            return factor
        else:
            continue


print('Program will find the greatest common factor between 2 numbers')
no1 = input('Please enter your first number: ')
no2 = input('Please enter your second number: ')

if no1 > no2:
    small = int(no2)
    large = int(no1)
else:
    small = int(no1)
    large = int(no2)

answer = gcf(small, large)
print(f'The Greatest Common Factor between {large} and {small} is {answer}')
