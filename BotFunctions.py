import re
import pandas as pd
import csv
import matplotlib.pyplot as plt
import time
import os


# method to print all the themes that have not been used
def get_unused_themes(database):
    df = pd.read_csv(database)
    unused_df = df.loc[df['Used'] == False]
    # print(unused_df.to_string())
    unused_list = unused_df['Theme'].tolist()
    # print(unused_list)
    return unused_list


# method to print all the themes that have been used
def get_used_themes(database):
    df = pd.read_csv(database)
    used_df = df.loc[df['Used'] == True]
    # print(used_df.to_string())
    used_list = used_df['Theme'].tolist()
    # print(used_list)
    return used_list


# returns all themes in a list, regardless of whether they have been used or not, use this to check if the theme is
# already present in the database
def get_all_themes(database):
    df = pd.read_csv(database)
    theme_list = df['Theme'].tolist()
    # print(theme_list)
    return theme_list


# this method formats the input received by the bot in the discord channel, it forces all lower case,
# it forces no leading or trailing spaces, and no additional spaces
# This was written to standardize the input from discord users to prevent repeat theme ideas
def format_input(*inp):
    to_return = ''
    for i in inp:
        to_return = f'{to_return} {i} '
    to_return = to_return.lower()
    to_return = to_return.strip()
    to_return = re.sub(' +', ' ', to_return)  # this regex removes extra spaces between words.
    return to_return


# returns a boolean depending on whether the theme already exists in the
def contains_theme(theme, database):
    theme = format_input(theme)
    theme_list = get_all_themes(database)
    in_list = theme in theme_list
    return in_list


# void function that takes as input all of the necessary input from the discord bot, and writes the new theme to the
# database: (Themes.csv file)
def add_theme(theme, creator, used, date_added, date_used):
    df = pd.read_csv('Resources/Themes.csv', index_col='Index')
    # print(df.to_string())
    add_row = [theme, creator, used, date_added, date_used]
    df.loc[len(df.index)] = add_row
    # print(df.to_string())
    df.to_csv('Themes.csv')


# Selects a random theme that has not been used yet, returns the name of the theme and marks it as used.
def select_theme():
    df = pd.read_csv('Resources/Themes.csv', index_col='Index')
    # print(df.to_string())
    unused_df = df.loc[df['Used'] == False]
    # print(unused_df.to_string())
    theme = unused_df.sample()
    theme_value = theme.iloc[0, 0]
    theme_index = theme.index.item()
    # print(theme)
    print('\n' + theme_value + '\n')
    df.iloc[theme_index, df.columns.get_loc('Used')] = True
    # print(df.to_string())
    df.to_csv('Themes.csv')
    return theme_value


# get's the channel code theme bot will be posting in, input the file path for the channel codes csv file
# and if you want the bot to run in a testing channel, input "test" for the second parameter
def get_channel_code(fpath, c):
    with open(fpath) as cc:
        csv_reader = csv.reader(cc, delimiter=',')
        csv_reader = list(csv_reader)
        day = csv_reader[1][1]
        test = csv_reader[2][1]
        if c == 'test':
            return test
        else:
            return day


def build_filepath_nov(name):
    filepath = f'NoFatNovember/{name}.csv'
    return filepath


def write_weight_to_file(fpath, date, weight):
    df = pd.read_csv(fpath)
    values = [date, weight]
    df.loc[len(df)] = values
    df.to_csv(fpath, index=False)


# returns file path for chart to use in conjunction with delete_image_resource
def get_weight_loss_chart(fpath, name):
    df = pd.read_csv(fpath)
    rpath = f'Resources/{name}-chart.png'
    dates = df['date']
    weights = df['weight']
    with plt.style.context('dark_background'):
        plt.title('No Fat November Chart')
        plt.xlabel('Date(mm/dd)')
        plt.ylabel('Weight(lbs.)')
        plt.plot(dates, weights, color='blue')
        # plt.show()
        plt.savefig(rpath)
        # time.sleep(2)
    return rpath


def delete_image_resource(fpath):
    os.remove(fpath)

