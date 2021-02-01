import pandas as pd

# 数据加载
df = pd.read_csv('car_complain.csv')

# 抱怨点拆分
df = df.drop('problem', axis=1).join(df.problem.str.get_dummies(','))


# 数据清洗，将一汽大众和一汽-大众合并
def f(x):
    x = x.replace('一汽-大众', '一汽大众')
    return x


df['brand'] = df['brand'].apply(f)

# 按品牌统计投诉总数
result = df.groupby(['brand'])['id'].count().sort_values(ascending=False)
print("******品牌投诉总数******")
print(result)

# 按车型统计投诉总数
result3 = df.groupby(['car_model'])['id'].count().sort_values(ascending=False)
print("******车型投诉总数******")
print(result3)

# 统计品牌平均车型投诉数量
result4 = df.groupby('brand')['car_model'].value_counts().groupby('brand').\
    mean().sort_values(ascending=False)
print("******品牌平均车型投诉数量******")
print(result4)
