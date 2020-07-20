import os
path = r'/root/'
for root, dirs, files in os.walk(path):   # 遍历path目录下的所有文件和文件夹（root：当前遍历目录，dirs：当前遍历目录所包含的文件夹，files：当前遍历目录所包含的文件）
  for file in files:
    print(os.path.join(root,file))
