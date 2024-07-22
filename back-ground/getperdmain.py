from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from netCDF4 import Dataset
import os
import netCDF4 as nc
import argparse
import numpy as np
import torch

from getperd import Exp
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
def showp(outputs):
    plt.figure(figsize=(10,10))
    plt.imshow(outputs)
    plt.colorbar()
    plt.title('outputs')
    plt.show()
def create_parser():
    parser = argparse.ArgumentParser()
    # Set-up parameters
    parser.add_argument('--device', default='cuda', type=str, help='Name of device to use for tensor computations (cuda/cpu)')
    parser.add_argument('--res_dir', default='./results', type=str)
    parser.add_argument('--ex_name', default='Debug', type=str)
    parser.add_argument('--use_gpu', default=True, type=bool)
    parser.add_argument('--gpu', default=0, type=int)
    parser.add_argument('--seed', default=1, type=int)

    # dataset parameters
    parser.add_argument('--batch_size', default=1, type=int, help='Batch size')
    parser.add_argument('--val_batch_size', default=1, type=int, help='Batch size')
    parser.add_argument('--data_root', default='./data/')
    parser.add_argument('--dataname', default='weather', choices=['mmnist', 'taxibj','weather'])
    parser.add_argument('--num_workers', default=8, type=int)

    # model parameters
    parser.add_argument('--in_shape', default=[12, 1, 120, 120], type=int,nargs='*') # [10, 1, 64, 64] for mmnist, [4, 2, 32, 32] for taxibj
    parser.add_argument('--hid_S', default=64, type=int)##
    parser.add_argument('--hid_T', default=512, type=int)##
    parser.add_argument('--N_S', default=4, type=int)
    parser.add_argument('--N_T', default=8, type=int)
    parser.add_argument('--groups', default=4, type=int)

    # Training parameters
    parser.add_argument('--epochs', default=600, type=int)
    parser.add_argument('--log_step', default=1, type=int)
    parser.add_argument('--lr', default=0.001, type=float, help='Learning rate')
    return parser


def nc2asc(nc_path, output):
    if not os.path.exists(output):  # 检测文件夹是否存在
        os.makedirs(output)

    nc_file = nc.Dataset(nc_path, 'r')
    print(nc_file.variables.keys())

    time_var = nc_file.variables['time']
    data_var = nc_file.variables['vo']  # [24, 120, 120]
    print(data_var.shape)
    time_data = time_var[:]
    time_units = time_var.units
    time_dates = nc.num2date(time_data, units=time_units)

    header_info = f"""ncols         {data_var.shape[2]}
nrows         {data_var.shape[1]}
xllcorner     110.0
yllcorner     3.0
cellsize      0.25
NODATA_value  0.0"""

    for i, date in enumerate(time_dates):
        time_data_slice = data_var[i, :, :]
        asc_filename = os.path.join(output, f'wave-{date.strftime("%Y-%m-%dT%H-%M-%S")}.asc')
        with open(asc_filename, 'w') as asc_file:
            asc_file.write(header_info + '\n')
            np.savetxt(asc_file, time_data_slice, fmt='%f')
        print(f'The {asc_filename} has been written.')

    nc_file.close()

def save_to_netcdf(data, filename):
    """
    Save data to a NetCDF file.
    :param data: numpy array of shape (time, height, width)
    :param filename: file path to save the NetCDF file
    """
    with nc.Dataset(filename, 'w', format='NETCDF4') as dataset:
        # Create dimensions
        time_dim = dataset.createDimension('time', data.shape[0])
        height_dim = dataset.createDimension('height', data.shape[1])
        width_dim = dataset.createDimension('width', data.shape[2])

        # Create variables
        times = dataset.createVariable('time', np.float64, ('time',))
        heights = dataset.createVariable('height', np.float32, ('height',))
        widths = dataset.createVariable('width', np.float32, ('width',))
        values = dataset.createVariable('vo', np.float32, ('time', 'height', 'width'))

        # Write data to variables
        times[:] = np.arange(data.shape[0])
        heights[:] = np.arange(data.shape[1])
        widths[:] = np.arange(data.shape[2])
        values[:, :, :] = data

        # Add units attribute to time variable
        times.units = "hours since 2024-07-19 00:00:00.0"
        times.calendar = "gregorian"

        print(f'{filename} has been written.')



if __name__ == '__main__':
    args = create_parser().parse_args()
    config = args.__dict__
    # Load NetCDF file
    nc_file = 'G:/Implicit-Stacked-Autoregressive-Model-for-Video-Prediction-main (2)/data/seadata/seawindvdatanc/sea_windv_data_new.nc'
    dataset = Dataset(nc_file, 'r')
    inputs = dataset.variables['eastward_wind'][:]
    inputs = torch.Tensor(np.squeeze(inputs)[-12:].astype(np.float32))# Remove single-dimensional entries
    print("Input shape after squeeze:", inputs.shape)

    # Close the dataset after loading
    dataset.close()

    # inputs = torch.Tensor(np.load('data/weather/test.npy').astype(np.float32))
    exp = Exp(args)
    for i in range(6):
        pred_y = exp.get_12_hours(inputs[-12:])
        inputs = torch.concat((inputs, pred_y), dim=0)
        print(inputs.shape)
    # mse:0.000015
    # mae::0.003053
    # for i in range(13,84):
    showp(inputs[12])
    showp(inputs[13])
    showp(inputs[83])
    # Save predictions to NetCDF file
    pred_nc_file = 'G:/Implicit-Stacked-Autoregressive-Model-for-Video-Prediction-main (2)/data/seadata/predictions.nc'
    save_to_netcdf(inputs[12:], pred_nc_file)

    # Convert the saved NetCDF file to ASC files
    nc2asc(pred_nc_file, 'G:/Implicit-Stacked-Autoregressive-Model-for-Video-Prediction-main (2)/data/seadata/ISAMseawindv_asc')
    print('mse:{:.6f}'.format(mean_squared_error(inputs[36], pred_y[11])))
    print('mae::{:.6f}'.format(mean_absolute_error(inputs[36], pred_y[11])))
