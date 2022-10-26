import random

print(random.randrange(100, 10, -2))

print(random.sample(range(1, 11, 1), 10));

print(random.sample(range(0, 100), 2));

test = [3,4,5, 2, 1, 10, 47, 6];

del test[1];

test.sort();

print("test : ", test)