import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号 #有中文出现的情况，需要u'内容
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()
ax.scatter(x, y, s=100)
ax.set_title('平方数', fontsize=24)
ax.set_xlabel('值', fontsize=14)
ax.set_ylabel('值的平方', fontsize=14)

# 设置刻度标记的大小
ax.tick_params(axis='both', labelsize=14)
# plt.show()

plt.savefig('quares_plt.png')
