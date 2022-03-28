#random
#append
#len
import random
# numbers = ()
# for i in range(0, 10):

numbers = (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10))
print('Os valores sorteados foram : ', *numbers, sep=' ')
print(f'O maior valor {max(numbers)}')
print(f'O menor valor {min(numbers)}')