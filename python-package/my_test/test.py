#%%
import sys
from pathlib import Path
sys.path.append(str(Path(sys.path[0]).parent))
from lightgbm import Dataset, Booster
import pandas as pd

if __name__ == '__main__':
    data_X = pd.read_csv('train_X_clean.csv')
    data_Y = pd.read_csv('train_Y_clean.csv')

    # Load from other formats and save binary file
    # ==done==
    dataset1 = Dataset(data_X.values, data_Y['SalePrice'].values)
    dataset1.save_binary("myfile.bin")

    # Load from binary file
    # ==done==
    dataset1 = Dataset("myfile.bin")

    # Load dataset1 from binary file
    # Load dataset2 from raw csv file
    # Call ConcatDataset
    #   main_set provides the binmapper
    #   append_set fit the raw data to the binmapper
    #   return a new dataset, which concatenates the two datasets together
    # ==Not done==
    dataset1 = Dataset("myfile.bin")
    new_data_X = pd.read_csv('train_X_clean.csv')
    new_data_Y = pd.read_csv('train_Y_clean.csv')
    dataset1.AddData(new_data_X.values, data_Y['SalePrice'].values)
    dataset1.save_binary("Concat.bin")

    # Load from raw data, which has been already splitted into bins
    # ==Not done==
    new_data_X = pd.read_csv('train_X_clean.csv')
    new_data_Y = pd.read_csv('train_Y_clean.csv')
    dataset1 = Dataset(data_X.values, data_Y['SalePrice'].values, already_bins=True)
    dataset1.save_binary("myfile.bin")

# %%
