import csv
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号 #有中文出现的情况，需要u'内容
filename = 'data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    head_row = next(reader)

    highs = []
    for row in reader:
        high = int(row[5])
        highs.append(high)

fig, ax = plt.subplots()
ax.plot(highs, c='red')

ax.set_title('2018年7月每日最高温度', fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel('温度（F）', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
