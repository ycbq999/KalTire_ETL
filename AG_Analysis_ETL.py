import pandas as pd
import os

# set working directory
AG_Pricing_Data_Folder ='C:/Users/sochen/OneDrive - Kal Tire/Documents/files to work on/Pricing Strategy/DataSource/2023-08-21'
os.chdir(AG_Pricing_Data_Folder)
MPR_PATH = "C:/Users/sochen/OneDrive - Kal Tire/Documents/PowerBI report/Pricing Record Power BI/datasource/raw_files/Archived"



#################################################################################Phase One#################################################################################
"""
# Uncomment the flowing if you want to start from stratch

# List all CSV files in the directory
csv_files = [f for f in os.listdir(MPR_PATH) if f.endswith('.csv')]

# Create an empty list to hold the dataframes
df_list = []

# Loop through each CSV file, read it into a dataframe, and append to the list
for f in csv_files:
    filepath = os.path.join(MPR_PATH, f)
    df = pd.read_csv(filepath)
    df_list.append(df)

merged_df = pd.concat(df_list, ignore_index=True)

# drop the specified columns
merged_df = merged_df.drop(columns=[ 'CostGroupValue','CostGrp', 'DCLID', 'Default',\
                                    'DiscGrp', 'DiscGrpRate', 'DiscOvr', 'DiscOvrRate', \
                                    'ExtraLoad', 'FX', 'FXRate', 'Fleet', 'HOWhsSpec', 'InvPrice', \
                                    'L-cost1', 'L-cost1Rate', 'L-cost2', 'L-cost2Rate', 'L-cost3', \
                                    'L-cost3Rate', 'L-cost4', 'L-cost4Rate', 'LandedCostGroup', 'LoadIndex', \
                                    'PriceGrp', 'PriceType', 'ProType', 'ProdGrp', 'RebateGrp', \
                                    'RebateRate', 'RegNet', 'SpecFleet', 'Staff', 'SuggRetail', 'SuppPrice',\
                                      'TireType', 'VIP', 'Wholesale'])

merged_df.to_csv("out.csv", index=False)
"""  
#################################################################################Phase Tow#################################################################################


# write a function that take a csv file and extract the unique SKUs from it
def extract_SKUs_from_csv(csv_file):
    DF = pd.read_csv(csv_file)
    return DF["SKU"].unique()

active_SKUs = extract_SKUs_from_csv("Result_LSR_Size.csv")
# print(len(active_SKUs))

# read the output from phase 1
DF = pd.read_csv("out.csv", index_col=False)

print(f'DF.shape: {DF.shape}')
print(f'DF.columns: {DF.columns}')

print(DF.head(3))

DF1 = DF[DF["SKU"].isin(active_SKUs)]
print(f'DF1.shape: {DF1.shape}')

# apply GP% formula
DF1["GP%"] = (DF1["Net"] - DF1["Base"])/DF1["Net"]*100
DF1["GP%"] = DF1["GP%"].round(0)


import numpy as np
DF1["System_Date"] = pd.to_datetime(DF1["System_Date"])
DF1["Quarter"] = np.array(pd.PeriodIndex(DF1["System_Date"], freq='Q'))
print(DF1["Quarter"].head())

print(f'DF1.shape: {DF1.shape}')
#summarize MPR data abit

MPR_Cols_Keeper= ["SKU" ,"Manuf",  "RimDia.",  "EDSNC",  "WhsCost",  "BranchCost",  "Net",  "Base",  "Quarter",  "GP%"]

DF1 = DF1[MPR_Cols_Keeper]


# write a for loop to extract the MPR data for each SKU, group by Quarter and calculate average of each other columns
MPR_SKUs = DF1["SKU"].unique()
MPR_SKUs = MPR_SKUs.tolist()

dataframes_list = []
for sku in MPR_SKUs:
  DF1_SKU = DF1[DF1["SKU"] == sku]
  DF1_SKU = DF1_SKU.groupby(["Quarter"]).agg(
      {"Manuf": lambda x: x.value_counts().index[0], 
        "RimDia.": lambda x: x.value_counts().index[0],  
        "EDSNC": "mean", 
        "WhsCost": "mean", 
        "BranchCost": "mean", 
        "Net": "mean", 
        "Base":"mean", 
        "GP%": "mean"}).reset_index()
  DF1_SKU['SKU'] = sku
  dataframes_list.append(DF1_SKU)
DF2 = pd.concat(dataframes_list, axis=0,ignore_index=True)
DF2.to_csv('MPR_SUM_OUT.csv', index=False)


print(f'DF2.shape: {DF2.shape}')


    
    


# AG_Analysis_output = 'C:/Users/sochen/OneDrive - Kal Tire/Documents/PowerBI report/Pricing Record Power BI/datasource/raw_files/Output_Files/AG_Out.csv'
# DF1.to_csv('MPR_OUT.csv', index=False)


