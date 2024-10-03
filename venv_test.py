import sys
import torch

# 优化：使用 f-string 写入字符串到文件
with open("venv_test_output.txt", "a") as file:
    file.write(f"Python interpreter: {sys.executable}\n")
    file.write(f"Torch version: {torch.__version__}\n")
