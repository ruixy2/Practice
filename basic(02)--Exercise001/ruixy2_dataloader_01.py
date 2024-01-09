from torch.utils.data import Dataset
from torch.utils.data import DataLoader
import torch

class MyDataset(Dataset):
    def __init__(self,data):
        self.data = data

    def __getitem__(self,index):
        return self.data[index]
    
    def __len__(self):
        return len(self.data)
    
if __name__ == '__main__':
    data = list(range(100))  #0-99
    dataset = MyDataset(data)

    dataloader = DataLoader(dataset,batch_size=3,shuffle=True,num_workers=3)
    for i,batch in enumerate(dataloader):
        print(batch)
        if i > 5:
            break