import torch

## 测试是否模型使用GPU

print(torch.cuda.is_available())
print(torch.cuda.empty_cache())
print(torch.__version__)
print(torch.version.cuda)
print(torch.cuda.empty_cache())