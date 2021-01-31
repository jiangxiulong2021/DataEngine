"""
黑马训练营第一节课
Action2：统计全班的成绩
"""
# 导入numpy

import numpy as np

# 定义两个数组
persontype = np.dtype({
    'names': ['name', 'chinese', 'math', 'english'],
    'formats': ['S32', 'i', 'i', 'i']})
peoples = np.array([('ZhangFei', 68, 65, 30),
                    ('GuanYu', 95, 76, 98),
                    ('LiuBei', 98, 86, 88),
                    ('DianWei', 90, 88, 77),
                    ('XuChu', 80, 90, 90)], dtype=persontype)

chineses = peoples['chinese']
maths = peoples['math']
englishes = peoples['english']
print('*******语文******')
print('平均成绩：', np.mean(chineses))
print('最低分：', np.min(chineses))
print('最高分：', np.max(chineses))
print('方差：', np.var(chineses))
print('标准差：', np.std(chineses))

print('*******数学******')
print('平均成绩：', np.mean(maths))
print('最低分：', np.min(maths))
print('最高分：', np.max(maths))
print('方差：', np.var(maths))
print('标准差：', np.std(maths))

print('*******英语******')
print('平均成绩：', np.mean(englishes))
print('最低分：', np.min(englishes))
print('最高分：', np.max(englishes))
print('方差：', np.var(englishes))
print('标准差：', np.std(englishes))

persontype2 = np.dtype({
    'names': ['name', 'Total'],
    'formats': ['S32', 'i']})
peoples2 = np.array([('ZhangFei', 0),
                     ('GuanYu', 0),
                     ('LiuBei', 0),
                     ('DianWei', 0),
                     ('XuChu', 0)], dtype=persontype2)

for i in range(5):
    sum1 = 0
    for j in range(1, 4):
        sum1 = sum1 + peoples[i][j]
    peoples2[i][1] = sum1
Names = peoples2['name']
Totals = peoples2['Total']
ind = np.lexsort((Names, Totals))
Rind = reversed(ind)
Rank = 1
print('排名', '姓名  ', '总分', '语文', '数学', '英语')
for i in Rind:
    print(Rank, Names[i], Totals[i], chineses[i], maths[i], englishes[i])
    Rank = Rank + 1
