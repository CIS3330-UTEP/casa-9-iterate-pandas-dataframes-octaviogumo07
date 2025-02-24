# import pandas as pd

# # Load the dataset
# file_path = "big-mac-full-index.csv"  # Ensure this file exists in your directory
# df = pd.read_csv(file_path)

# # Method 1: Using iterrows()
# def iterate_using_iterrows():
#     print("\nIterating using iterrows():")
#     for index, row in df.iterrows():
#         print(f"Row {index} - Country: {row['name']}, Local Price: {row['local_price']}")

# # Method 2: Using apply()
# def iterate_using_apply():
#     print("\nIterating using apply():")
#     df.apply(lambda row: print(f"Country: {row['name']}, Local Price: {row['local_price']}"), axis=1)

# # Run the functions
# if __name__ == "__main__":
#     iterate_using_iterrows()
#     iterate_using_apply()



# import pandas as pd #importing pandas

# df = pd.read_csv('big-mac-full-index.csv')      #loading the CVS file into dataframe

# for index, row in df.iterrows():          #iterate through each row
#     iso_a3 = row['iso_a3']
#     print(iso_a3)

# for index, row in df.iterrows():         #print the value enabled
#     iso = row['iso_a3']
#     print(iso)

# print(df.head())



import pandas as pd

df = pd.read_csv("big-mac-full-index.csv")

df["iso_a3"].apply(lambda x: print(x))

print(df.head())


import pandas as pd 

#dataframe
data = {'numbers': [5, 6, 7, 8, 9]}
df = pd.DataFrame(data)

def square(x):
    return x ** 2

#apply fucntion to the numbers column 
df['sqaure_numbers'] = df['numbers'].apply(square)

print(df)
