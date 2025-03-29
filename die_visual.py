from die import Die
import plotly.express as px

#创建一个D6
die = Die()
#掷几次骰子并将结果存储在一个列表中
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)
#结果分析
frequencies = []
poss_results = range(1, die.num_size+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)
print(frequencies)
#结果可视化
fig = px.bar(x=poss_results,y=frequencies)
fig.show()