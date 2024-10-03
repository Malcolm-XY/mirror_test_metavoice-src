import torch

# 写入字符串到文件
with open("venv_test_output.txt", "a") as file:
    file.write(torch.__version__)
