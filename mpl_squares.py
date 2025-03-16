import matplotlib.pyplot as plt
plt.style.available

#数据
square = [1,4,9,16,25]
value = [1,2,3,4,5]

#样式(表格)
plt.style.use('seaborn')

#绘图
fig, ax  = plt.subplots()
ax.plot(value,square,linewidth = 3)

#绘点并设置颜色
x_values = range(1,1001)
y_values = [x**2 for x in x_values]
ax.scatter(x_values, y_values, color = 'red', s = 5)

#设置图题，表明xy轴，设置刻度字号以及其他的字号
ax.set_title('Square number',fontsize = 24)
ax.set_xlabel('Value',fontsize = 14)
ax.set_ylabel('Square of value',fontsize = 14)
ax.tick_params(labelsize = 14)

#设置坐标轴的取值范围
ax.axis([0,1100,0,1_100_000])

#保存
#plt.savefig('squares_plot.jpg',bbox_inches = 'tight')

#展示
plt.show()