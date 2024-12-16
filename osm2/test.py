import matplotlib.pyplot as plt

# 创建一个8x8的矩阵数据表示点
matrix_data = [[(i, j) for j in range(8)] for i in range(8)]

# 绘制矩阵图
plt.figure(figsize=(6, 6))
for i in range(8):
    for j in range(8):
        plt.plot(i, j, 'bo')  # 绘制点

plt.xlim(-1, 8)
plt.ylim(-1, 8)
plt.gca().invert_yaxis()
plt.grid(True)
plt.show()

# 输出线段数据
for i in range(8):
    for j in range(8):
        if i < 7:
            print((matrix_data[i][j], matrix_data[i+1][j]))  # 垂直线段
        if j < 7:
            print((matrix_data[i][j], matrix_data[i][j+1]))  # 水平线段
