
import matplotlib.pyplot as plt

data = list(open('datasets/curvefitting.txt'))
dots = list([tuple(map(float, x.strip().split(' '))) for x in data])
xdots = [x[0] for x in dots]
ydots = [x[1] for x in dots]

# print(dots)
plt.plot(xdots, ydots, 'ko')
plt.axis([-0.1, 1.1, -1.3, 1.3])
plt.show()