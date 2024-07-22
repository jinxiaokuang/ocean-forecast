import warnings
warnings.filterwarnings("ignore")
import random
import numpy as np
import os.path as osp
import torch
import torch.nn.functional as F
from torch.utils.data import Dataset


class WeatherBenchDataset(Dataset):
    def __init__(self,data_root, idx_in, idx_out, step=1,
                 mean=None, std=None,
                 transform_data=None, transform_labels=None):
        super().__init__()
        self.idx_in = np.array(idx_in)
        self.idx_out = np.array(idx_out)
        self.step = step
        self.data = None
        self.mean = mean
        self.std = std
        self.transform_data = transform_data
        self.transform_labels = transform_labels
        self.time = None
        self.data = np.load(data_root)[:,:,:].astype(np.float32)   # todo:Step1:将插值后的数组放置于此,训练集[7800, 120, 120]

        self.valid_idx = np.array(
            range(-idx_in[0], self.data.shape[0]-idx_out[-1]-1))

    def __len__(self):
        return self.valid_idx.shape[0]

    def __getitem__(self, index):
        index = self.valid_idx[index]
        data = torch.tensor(self.data[index+self.idx_in])
        labels = torch.tensor(self.data[index+self.idx_out])
        data = torch.unsqueeze(data,dim=1)
        labels = torch.unsqueeze(labels, dim=1)
        return data, labels


def load_data(batch_size,
              val_batch_size,
              data_root='',
              num_workers=4,
              idx_in=[-11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0],
              idx_out=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
              step=1,
              drop_last=False,
              **kwargs):

    train_set = WeatherBenchDataset(data_root='data/weather/train.npy',
                                    idx_in=idx_in,
                                    idx_out=idx_out,
                                    step=step)
    test_set = WeatherBenchDataset(data_root='data/weather/test.npy',
                                   idx_in=idx_in,
                                   idx_out=idx_out,
                                   step=step,
                                   mean=train_set.mean,
                                   std=train_set.std)

    dataloader_train = torch.utils.data.DataLoader(train_set, batch_size, shuffle=True ,pin_memory=True)
    dataloader_vail = torch.utils.data.DataLoader(test_set, val_batch_size, shuffle=True, pin_memory=True)
    dataloader_test = torch.utils.data.DataLoader(test_set, val_batch_size, shuffle=True, pin_memory=True)
    return dataloader_train, dataloader_vail, dataloader_test


if __name__ == '__main__':
    idx_ins = np.arange(-23, 1)
    idx_outs = np.arange(1, 25)
    print(idx_ins)
    print(idx_outs)
