import sys
sys.path.append('d:/a-xiaoyu/learn/AI/Practice/basic(01)--Exercise003')
from ruixy2_files_03 import get_file_list
if __name__ == '__main__':
    mylist = get_file_list('d:/a-xiaoyu/learn/AI/Practice/')
    print(mylist[0:6])
    print(mylist[-1])
    print(mylist[4:])