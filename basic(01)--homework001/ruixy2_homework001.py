import os
import random

def split_dataset(directory_path, train_ratio=0.8, validation_ratio=0.1):
    # 获取目录下所有的.py文件
    all_files = [os.path.join(directory_path, f) for f in os.listdir(directory_path) if f.endswith('.py')]
    
    # 随机打乱文件顺序
    random.shuffle(all_files)

    # 计算各个子集的数量
    total_files = len(all_files)
    train_count = int(total_files * train_ratio)
    validation_count = int(total_files * validation_ratio)
    test_count = total_files - train_count - validation_count

    # 分割数据集
    train_set = all_files[:train_count]
    validation_set = all_files[train_count:train_count + validation_count]
    test_set = all_files[train_count + validation_count:]

    return all_files, train_set, validation_set, test_set

# 调用函数并输出结果
full_dataset, train_set, validation_set, test_set = split_dataset('d:/a-xiaoyu/learn/AI/basic(01)--Exercise001')

print("全集数量：", len(full_dataset))
print("训练集数量：", len(train_set), " 文件名：", train_set)
print("验证集数量：", len(validation_set), " 文件名：", validation_set)
print("测试集数量：", len(test_set), " 文件名：", test_set)