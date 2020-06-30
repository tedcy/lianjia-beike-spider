import pandas as pd
import os
import tqdm
import re

dir1="./data/lianjia/ershou/gz/20200619/"
dir2="./data/lianjia/ershou/gz/20200630/"

filenames=os.listdir(dir1)
dir1Dict = {}
for i, filename in tqdm.tqdm(enumerate(filenames), total=len(filenames)):
    if (filename != "panyu_yayuncheng.csv"):
        continue
    df=pd.read_csv(dir1 + filename)
    for name in df.index:
        line = df.loc[name]
        dir1Dict[line['pic']] = line['price']

filenames=os.listdir(dir2)
dir2Dict = {}
for i, filename in tqdm.tqdm(enumerate(filenames), total=len(filenames)):
    if (filename != "panyu_yayuncheng.csv"):
        continue
    df=pd.read_csv(dir2 + filename)
    for name in df.index:
        line = df.loc[name]
        dir2Dict[line['pic']] = line['price']

sum = 0
increase = 0
decrease = 0
new = 0
maxDecrease = 0
maxDecreasePic = ''
print(len(dir1Dict), len(dir2Dict))
for k in dir2Dict:

    v1 = dir1Dict.get(k)
    v2 = dir2Dict.get(k)
    if v1 == None:
        new = new + 1
        continue
    t = re.findall('^[0-9]*', v1)
    v1 = int(t[0])
    t = re.findall('^[0-9]*', v2)
    v2 = int(t[0])
    if v2 > v1:
        increase = increase + 1
    if v2 < v1:
        if maxDecrease < v1 - v2:
            maxDecrease = v1 - v2
            maxDecreasePic = k
        decrease = decrease + 1
print(increase, decrease, new)
print(maxDecrease, maxDecreasePic)
