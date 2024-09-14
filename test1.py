import torch

# 创建一个 3x3 的随机张量
x = torch.rand(3, 3)
print("随机张量 x：")
print(x)

# 创建一个全 1 的张量
y = torch.ones(3, 3)
print("\n张量 y：")
print(y)

# 张量加法
z = x + y
print("\n张量加法 z = x + y：")
print(z)
