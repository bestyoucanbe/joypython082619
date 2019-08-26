import random

my_randoms = list()
for i in range(10):
    my_randoms.append(random.randrange(1, 6, 1))

for number in range(1, 6):
    # This is to see the value of the number
    print(number)
    # count finds how many times it appears in a whatever is passed in.
    if my_randoms.count(number) > 0:
        print(f'My randoms list contains {number}')
    else:
        print(f'My randoms does not contain {number}')
