import sys
import os
dir = os.getcwd()
print(dir)
sys.path.append('d:/a-xiaoyu/learn/AI/Practice/')

from ruixy2_01 import whatIsYourName
if __name__ == '__main__':
    name = whatIsYourName()
    print("Hello " + name + "," + " Welcom to AI Force!")