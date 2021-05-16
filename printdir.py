'''
剩余希望实现的功能：
输出的文件名存在指定路径的csv或者txt里
'''

import os.path
from openpyxl import workbook
import pandas as pd
from pathlib import Path
import pdb



target_path=input("请输入路径：")
target_path_validation = Path(target_path)
df=pd.DataFrame(columns=["a"])
if target_path_validation.is_dir():
    for roots, dirs, files in os.walk(target_path, topdown=False):
        for dir in dirs:
            df =df.append({"a":dir},ignore_index=True)
            # print("dir:",dir)
        # for name in files:
        #     print(name)
        df.to_csv("test.csv")
else:
    print("路径不存在")
