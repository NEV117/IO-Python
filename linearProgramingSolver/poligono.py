import matplotlib.pyplot as plt

vertices = [(0, 120), (10, 120), (70, 90), (115, 0), (0,0)]

xx = [v[0] for v in vertices]
yy = [v[1] for v in vertices]

plt.fill(xx, yy, 'b')
plt.axis('equal')
plt.show()
