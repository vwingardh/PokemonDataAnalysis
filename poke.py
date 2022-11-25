import numpy as np 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Function to assign column names to new DataFrames
def assign_column(dataFrame):
    dataFrame.columns = [
        '#', 
        'Name', 
        'Type 1', 
        'Type 2', 
        'Total', 
        'HP', 
        'Attack', 
        'Defense', 
        'Sp. Atk', 
        'Sp. Def', 
        'Speed', 
        'Generation', 
        'Legendary'
    ]
    return dataFrame


# Function accepts one variant to exclude
def exclude_variant(dataFrame, variant):
    df = dataFrame.to_numpy()
    variation_list = []

    for i in df:
        name = (i[1])
        if variant not in name:
            variation_list.append(i)
    
    variation_list = pd.DataFrame(np.array(variation_list))
    variation_list = assign_column(variation_list)
    return variation_list


# Function accepts multiple variations to exclude
def exclude_variations(dataFrame, variations):
    df = dataFrame.to_numpy()
    variation_list = []

    for i in df:
        name = (i[1])
        print(name)
        for variant in variations:
            if variant not in name:
                variation_list.append(i)

    variation_list = pd.DataFrame(np.array(variation_list))
    variation_list = assign_column(variation_list)
    return variation_list


# Function that plots data according to x, y values, data frame, and sort by
def plot_data(x, y, dataFrame, sortType, headSize):
    top_ten_attack = dataFrame.sort_values(by=sortType, ascending=False).head(headSize)
    sns.set_style('whitegrid')
    plt.figure(figsize=(10, 10))
    return sns.barplot(x=x, y=y, data=top_ten_attack, palette='inferno')


# Function that returns a data frame of only the 18 starter pokemon gen1-6
def get_starter_pokemon(dataFrame, starter_pokemon):
    df = dataFrame.to_numpy()
    df_starter = []

    for i in df:
        name = (i[1])
        for j in starter_pokemon:
            if name == j:
                df_starter.append(i) 

    df_starter = pd.DataFrame(np.array(df_starter))

    df_starter = assign_column(df_starter)
    return df_starter


# Returns a data frame containg only pokemon with type 1 or only pokemon with Type 1 and 2
def get_type(dataFrame, type):
    df = dataFrame.to_numpy()
    type_df = []

    if type == 1:
        for i in df:
            is_type = i[1]
            if is_type == '':
                type_df.append(i)
    else:
        for i in df:
            is_type = i[1]
            if is_type != '':
                type_df.append(i)

    type_df = pd.DataFrame(np.array(type_df))
    type_df.columns = [
            'Type 1', 
            'Type 2', 
            'Name', 
            'Attack', 
            'Sp. Atk'
        ]
    if type == 1:
        type_df = type_df.drop(['Type 2'], axis=1)
    
    return type_df
