import sys
import torch
import torchaudio

# 优化：使用 f-string 写入字符串到文件
with open("env_identify_output.txt", "a") as file:
    file.write(f"Python interpreter: {sys.executable}\n")
    file.write(f"Torch version: {torch.__version__}\n")
    file.write(f"Torch version: {torchaudio.__version__}\n")
