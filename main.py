
from plotting import plot

data = list(open('datasets/curvefitting.txt'))
dots = list([tuple(map(float, x.strip().split(' '))) for x in data])

print(dots)
plot(dots, 1)

# print(dots)