import os
import pandas as pd

# This code is for EDSNC history PBI report

# Instructions

# backup all_MPR_trimmed.csv file to archived folder in 'C:/Users/sochen/OneDrive - Kal Tire/Documents/PowerBI report/Pricing Record Power BI/datasource/output_files/all_MPR_trimmed2.csv'
# change the file name all_MPR_trimmed2.csv to all_MPR_trimmed.csv

# 1. Download MPR file every month 
# with alias
# 020,021,022,023,024,025,026,027,028,029,030,031,032,033,034,035,036,037,038,039,040,041,042,043,044,045,046,047,048,049,050,051,052,053,054,055,056,058,059,060,060I,061,061I,062,062I,063,063I,064,064I,065,065I,066,066I,068,068I,069,069I,070,072,073,074,075


# 2. Save it as raw data and add System_Date Column in BH Column
# 3. Clean the data as we want that match the all_MPR_trimmed.csv format by running this srcipt
# 4. then append the new file to all_MPR_trimmed.csv


# Path to directory containing CSV files
all_MPR_trimmed_csv_path = 'C:/Users/sochen/OneDrive - Kal Tire/Documents/PowerBI report/Pricing Record Power BI/datasource/output_files/all_MPR_trimmed.csv'
csv_dir = 'C:/Users/sochen/OneDrive - Kal Tire/Documents/PowerBI report/Pricing Record Power BI/datasource/raw_files'
output_dir = 'C:/Users/sochen/OneDrive - Kal Tire/Documents/PowerBI report/Pricing Record Power BI/datasource/raw_files/Output_Files/out.csv'
# List all CSV files in the directory
csv_files = [f for f in os.listdir(csv_dir) if f.endswith('.csv')]

# Create an empty list to hold the dataframes
df_list = []

# Loop through each CSV file, read it into a dataframe, and append to the list
for f in csv_files:
    filepath = os.path.join(csv_dir, f)
    df = pd.read_csv(filepath, low_memory=False)
    df_list.append(df)

# Concatenate all dataframes in the list into a single dataframe
merged_df = pd.concat(df_list, ignore_index=True)

# drop the specified columns
merged_df = merged_df.drop(columns=['Base', 'CostGroupValue', 'CostGrp', 'DCLID', 'Default', 'DiscGrp', 'DiscGrpRate', 'DiscOvr', 'DiscOvrRate', 'ExtraLoad', 'FX', 'FXRate', 'Fleet', 'HOWhsSpec', 'InvPrice', 'L-cost1', 'L-cost1Rate', 'L-cost2', 'L-cost2Rate', 'L-cost3', 'L-cost3Rate', 'L-cost4', 'L-cost4Rate', 'LandedCostGroup', 'LoadIndex', 'Net', 'PriceGrp', 'PriceType', 'ProType', 'ProdGrp', 'RebateGrp', 'RebateRate', 'RegNet', 'SpecFleet', 'Staff', 'SuggRetail', 'SuppPrice', 'TireType', 'VIP', 'Wholesale'])
# merged_df = merged_df.drop(columns=['Base', 'DCLID', 'Default', 'DiscGrp', 'DiscGrpRate', 'DiscOvr', 'DiscOvrRate', 'ExtraLoad', 'FX', 'FXRate', 'Fleet', 'HOWhsSpec', 'InvPrice', 'L-cost1', 'L-cost1Rate', 'L-cost2', 'L-cost2Rate', 'L-cost3', 'L-cost3Rate', 'L-cost4', 'L-cost4Rate', 'LandedCostGroup', 'LoadIndex', 'PriceGrp', 'PriceType', 'ProType', 'ProdGrp', 'RebateGrp', 'RebateRate', 'RegNet', 'SpecFleet', 'Staff', 'TireType', 'VIP', 'Wholesale'])

# print(merged_df.head(100))


# Save the merged dataframe to a new CSV file 
merged_df.to_csv(output_dir, index=False)



# Now append the new output file to all_MPR_trimmed file

all_MPR_trimmed2_path = 'C:/Users/sochen/OneDrive - Kal Tire/Documents/PowerBI report/Pricing Record Power BI/datasource/output_files/all_MPR_trimmed2.csv'

All_MPR_trimmed = pd.read_csv(all_MPR_trimmed_csv_path)
new_file = pd.read_csv(output_dir)

merged_df = pd.concat([All_MPR_trimmed, new_file], ignore_index=True)




# Save the merged dataframe to a new CSV file 
merged_df.to_csv(all_MPR_trimmed2_path, index=False)