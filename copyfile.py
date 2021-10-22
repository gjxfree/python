import os
path1 = r'config5'
path2 = r'config_log'
os.mkdir(path2)
for root, dirs, files in os.walk(path1):
    for dd in dirs:
        pp = os.path.join(root,dd)[len(path1)+1:]
        pp = os.path.join(path2, pp)
        os.mkdir(pp)
    for file in files:
        if file.split(".")[-1] == "log":
            p1 = os.path.join(root,file)
            p2 = os.path.join(path2,os.path.join(root,file)[len(path1)+1:])
            with open(p1,'r') as f:
                temp = f.read()
            with open(p2,'w') as f:
                f.write(temp)
                
for root, dirs, files in os.walk(path2):
    for dd in dirs:
        if not os.listdir(os.path.join(root,dd)):
            os.rmdir(os.path.join(root,dd))
