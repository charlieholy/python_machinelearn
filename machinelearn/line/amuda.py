import matplotlib.pyplot as plt
import numpy as np

#S=1/(1-a+a/n)


def amuda(x):
    # 直接返回sigmoid函数
    return 1/(1-x+x/4)


def plot_sigmoid():
    # param:起点，终点，间距
    x = np.arange(0, 100, 1)
    y = amuda(x)
    plt.plot(x, y)
    plt.show()


if __name__ == '__main__':
    plot_sigmoid()