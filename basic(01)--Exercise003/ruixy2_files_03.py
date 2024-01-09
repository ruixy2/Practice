import os
def get_file_list(path):
    return os.listdir(path)
    
if __name__ == '__main__':
    list = get_file_list('d:/a-xiaoyu/learn/AI/Practice/basic(01)--Exercise002')
    for item in list:
        print(item)
    