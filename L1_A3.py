import pandas as pd

# 数据加载
df = pd.read_csv('car_complain.csv')
# print(df)
# 抱怨点拆分
df = df.drop('problem', axis=1).join(df.problem.str.get_dummies(','))


# 数据清洗，将一汽大众和一汽-大众合并
def f(x):
    x = x.replace('一汽-大众', '一汽大众')
    return x


df['brand'] = df['brand'].apply(f)

# 按品牌统计投诉总数
result = df.groupby(['brand'])['id'].agg(['count'])
# print(result)

# 统计同一品牌同一投诉类型的个数
tags = df.columns[7:]
print(tags)
result2 = df.groupby(['brand'])[tags].agg(['sum'])

result2 = result.merge(result2, left_index=True, right_index=True, how='left')
result2.reset_index(inplace=True)
result2.to_excel("result2.xlsx", index=False)
# 按照投诉总数Count从大到小排序
result2 = result2.sort_values('count', ascending=False)
print(result2)
# 查看特定抱怨点的排名
query = ('A114', 'sum')
result3 = result2.sort_values(query, ascending=False)
print(result3)
