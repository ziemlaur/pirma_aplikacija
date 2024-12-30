# 1.	Load a CSV file into a `DataFrame` and print the first 5 rows.  

# import pandas as pd

# df = pd.read_csv(r'D:\PYTON\pirma_aplikacija\failas.csv')
# print(df.head())


# 2.	Create a `pandas` `DataFrame` with sales data and sort it by sales amount.  


# import pandas as pd

# data = {
#     'Product': ['TV', 'PHONE', 'COMPUTER', 'IPAD', 'IPOD'],
#     'Sales_Amount': [2500, 500, 2000, 530, 200],
#     'Sales_Date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05']
# }

# df = pd.DataFrame(data)

# df_sorted = df.sort_values(by='Sales_Amount', ascending=False)

# print(df_sorted)


# 3.	Write a program that filters a dataset to show only rows where a specific column's value is greater than a threshold.  


# import pandas as pd

# data = {
#     'Product': ['TV', 'PHONE', 'COMPUTER', 'IPAD', 'IPOD'],
#     'Sales_Amount': [2500, 500, 2000, 530, 200],
#     'Sales_Date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05']
# }

# df = pd.DataFrame(data)

# threshold = 1000

# filtered_df = df[df['Sales_Amount'] > threshold]

# print(filtered_df)



# 4.	Create a `pandas` `DataFrame` from a dictionary of lists and display summary statistics.  

# import pandas as pd

# data = {
#     'Product': ['TV', 'PHONE', 'COMPUTER', 'IPAD', 'IPOD'],
#     'Sales_Amount': [2500, 500, 2000, 530, 200],
#     'Sales_Date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05']
# }


# df = pd.DataFrame(data)

# print(df.describe())