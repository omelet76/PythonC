import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号 #有中文出现的情况，需要u'内容'

input_value = [1, 2, 3, 4, 5]
squars = [1, 4, 9, 16, 25]
# plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(input_value, squars, linewidth=3)

# 设置图表标题并给坐标轴加上标签
ax.set_title('平方数', fontsize=24)
ax.set_xlabel('值', fontsize=14)
ax.set_ylabel('值的平方', fontsize=14)

# 设置刻度标记的大小
ax.tick_params(axis='both', labelsize=14)
plt.show()
