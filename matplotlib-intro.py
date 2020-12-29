import matplotlib.pyplot as plt
import numpy as np

# x = np.linspace(0, 5, 11)
# y = x ** 2

# FUNCTIONAL
# plt.plot(x, y)
# plt.xlabel('X Label')
# plt.ylabel('Y Label')
# plt.title('Geoff is the best.')
# plt.subplot(1, 2, 1)
# plt.plot(x, y, 'r')
# plt.subplot(1, 2, 2)
# plt.plot(y, x, 'b')
# plt.show()

# OO
# fig = plt.figure()
# axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
# axes.plot(x, y)
# axes.set_xlabel('X Label')
# axes.set_ylabel('Y Label')
# axes.set_title('Big Data')

# Part 1
# fig = plt.figure()
# axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
# axes1.set_title('Big plot')
# axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])
# axes2.set_title('Little plot')
# axes1.plot(x, y)
# axes2.plot(y, x)

# Part 2
## This is tuple unpacking creating a fig and an axes object
## at the same time.
# fig, axes = plt.subplots(nrows = 1, ncols = 2)
# axes[0].plot(x, y)
# axes[0].set_title('First plot')
# axes[1].plot(y, x)
# axes[1].set_title('Second plot')

# Figure Size and DPI
# fig, axes = plt.subplots(nrows = 2, ncols = 1, figsize = (4, 5))
# axes[0].plot(x, y)
# axes[1].plot(y, x)
# 
# plt.tight_layout()
# plt.show()

# Save a figure
# newFig = plt.figure()
# ax = newFig.add_axes([0, 0, 1, 1])
# ax.plot(x, x**2, label = 'x squared')
# ax.plot(x, x**3, label = 'x cubed')
# ax.legend(loc = (0.1, 0.1))
# plt.tight_layout()
# plt.show()
# newFig.savefig('my_picture.png', dpi = 200)

# Part 3; colors, line widths and line types
# fig = plt.figure()
# ax = fig.add_axes([0, 0, 1, 1])
# ax.plot(x, y,
#         color = 'purple',
#         lw = 0.7,
#         ls = '-',
# )
# ax.set_xlim([0, 1])
# ax.set_ylim([0, 2])
# plt.show()

# MatPlotLib exercises
x = np.arange(0, 100)
y = x*2
z = x**2

fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
ax.plot(x, y)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('title')

plt.tight_layout()
plt.show()
