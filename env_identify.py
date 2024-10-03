import sys
import torch
import torchaudio

# 优化：使用 f-string 写入字符串到文件
with open("env_identify_output.txt", "a") as file:
    file.write(f"python interpreter: {sys.executable}\n")
    file.write(f"torch version: {torch.__version__}\n")
    file.write(f"torchaudio version: {torchaudio.__version__}\n")
    # 检查是否安装了 CUDA
    if torch.cuda.is_available():
        file.write("CUDA is available! PyTorch is using GPU.")
    else:
        file.write("CUDA is not available. PyTorch is using CPU.")
