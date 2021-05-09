import os.path
from pathlib import Path
import pdb



target_path=input("请输入路径：")
target_path_validation = Path(target_path)
if target_path_validation.is_dir():
    for roots, dirs, files in os.walk(target_path, topdown=False):
        for dir in dirs:
            print("dir:",dir)
        # for name in files:
        #     print(name)
else:
    print("路径不存在")
