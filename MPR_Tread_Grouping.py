
import os
import pandas as pd
import numpy as np

# Path to directory containing CSV files
RAW_FILES_PATH = 'C:/Users/sochen/OneDrive - Kal Tire/Documents/PowerBI report/Pricing Record Power BI/Archived_Raw_MPR/'

file_name_group = ['MPR_2018','MPR_2019','MPR_2020','MPR_2021','MPR_2022','MPR_2023']


def merge_csv_files(path):

    for file_name in file_name_group:
        csv_files = [f for f in os.listdir(path) if f.startswith(file_name)]
        df_list = []
        for f in csv_files:
            filepath = os.path.join(path, f)
            df = pd.read_csv(filepath)
            df_list.append(df)
        merged_df = pd.concat(df_list, ignore_index=True)

        # drop the specified columns
        merged_df = merged_df.drop(columns=['Base', 'CostGroupValue', 'CostGrp', 'DCLID', 'Default', 'DiscGrp', 'DiscGrpRate', 'DiscOvr', 'DiscOvrRate', 'ExtraLoad', 'FX', 'FXRate', 'Fleet', 'HOWhsSpec', 'InvPrice', 'L-cost1', 'L-cost1Rate', 'L-cost2', 'L-cost2Rate', 'L-cost3', 'L-cost3Rate', 'L-cost4', 'L-cost4Rate', 'LandedCostGroup', 'LoadIndex', 'Net', 'PriceGrp', 'PriceType', 'ProType', 'ProdGrp', 'RebateGrp', 'RebateRate', 'RegNet', 'SpecFleet', 'Staff', 'SuggRetail', 'SuppPrice', 'TireType', 'VIP', 'Wholesale'])
        merged_df.to_csv(file_name + '.csv', index=False)


merge_csv_files(RAW_FILES_PATH)