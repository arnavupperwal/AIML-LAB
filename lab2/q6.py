import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,3,5,7,11]
plt.bar(x, y)
plt.title("bar graph")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()

x = [2,4,6,8,10]
y = [2,3,5,7,11]
plt.bar(x, y)
plt.title('data')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()
plt.legend(['series 1','series 2'])

