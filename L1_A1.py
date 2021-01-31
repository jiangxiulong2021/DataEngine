"""
黑马训练营第一节课
Action1：求2+4+6+8+.。。+100的求和
"""
# 变量初始化
count = 0

# for循环求和，利用range函数取[2~102)的偶数，+2
for i in range(2, 102, +2):
    count = count + i

# 打印计算结果
print("SUM(2+4+6+8+...+100)=", count)
