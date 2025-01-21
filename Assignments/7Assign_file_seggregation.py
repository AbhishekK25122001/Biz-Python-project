import os
import shutil

for i in os.listdir(r'E:\\Python\\python_assign\\'):
    fnm=r'E:\\Python\\python_assign\\'+i
    sz=os.stat(fnm).st_size/1000

    if 0<=sz<=200:
        shutil.move(fnm,'E:\\Python\\python_assign\\small')
    elif 200<=sz<=400:
        shutil.move(fnm,'E:\\Python\\python_assign\\mid')
    else:
        shutil.move(fnm,'E:\\Python\\python_assign\\large')