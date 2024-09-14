import torch

# 检查是否有可用的 GPU
if torch.cuda.is_available():
    device = torch.device("cuda")
    print("使用 GPU：", torch.cuda.get_device_name(0))
else:
    device = torch.device("cpu")
    print("使用 CPU")

# 将张量移动到 GPU 或 CPU
x = torch.rand(3, 3).to(device)
print(x)
