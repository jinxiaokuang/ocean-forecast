import os
import os.path as osp
import json
import copy
import torch
import pickle
import logging
import numpy as np
from model import IAM4VP
from tqdm import tqdm
from API import *
from utils import *

class Exp:
    def __init__(self, args):
        super(Exp, self).__init__()
        self.args = args
        self.device = self._acquire_device()
        self._preparation()#准备模型
        print_log(output_namespace(self.args))
    def _acquire_device(self):
        if self.args.use_gpu:
            os.environ["CUDA_VISIBLE_DEVICES"] = str(self.args.gpu)
            device = torch.device('cuda:{}'.format(0))
            print_log('Use GPU: {}'.format(self.args.gpu))
        else:
            device = torch.device('cpu')
            print_log('Use CPU')
        return device

    def _preparation(self):
        # seed
        set_seed(self.args.seed)
        # log and checkpoint
        self.path = osp.join(self.args.res_dir, self.args.ex_name)
        check_dir(self.path)

        self.checkpoints_path = osp.join(self.path, 'checkpoints')
        check_dir(self.checkpoints_path)

        sv_param = osp.join(self.path, 'model_param.json')
        with open(sv_param, 'w') as file_obj:
            json.dump(self.args.__dict__, file_obj)

        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
        logging.basicConfig(level=logging.INFO, filename=osp.join(self.path, 'log.log'),
                            filemode='a', format='%(asctime)s - %(message)s')
        self._build_model()

    def _build_model(self):
        args = self.args
        self.model = IAM4VP(tuple(args.in_shape), args.hid_S,
                           args.hid_T, args.N_S, args.N_T).to(self.device)

    def get_12_hours(self,inputs:torch.Tensor):
        inputs = inputs.unsqueeze(dim=1)
        inputs = inputs.unsqueeze(dim=0)
        with torch.no_grad():
            args = self.args
            model = IAM4VP(tuple(args.in_shape), args.hid_S,
                                args.hid_T, args.N_S, args.N_T).to(self.device)
            if os.path.exists('wind_v_checkpoint.pth'):
                print("load_model!")
                model.load_state_dict(torch.load('wind_v_checkpoint.pth'))
            model.eval()
            batch_x= inputs.to(self.device)
            pred_list = []
            for timestep in range(12):
                t = torch.tensor(timestep * 100).repeat(batch_x.shape[0]).cuda()
                pred_y = model(batch_x, pred_list, t)  ##
                pred_list.append(pred_y)
            pred_y = torch.cat(pred_list, dim=1).unsqueeze(2)
        return pred_y.detach().cpu().squeeze()

