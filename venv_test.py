import torch

# 写入字符串到文件
with open("venv_test_output.txt", "w") as file:
    file.write(torch.__version__)
