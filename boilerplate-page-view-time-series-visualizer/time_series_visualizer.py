import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
import numpy as np
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv( "fcc-forum-pageviews.csv")

# Clean data
df_cleaned = df.loc[
    
    df['value'] >= df['value'].quantile(0.025)

].loc[
    
    df['value'] <= df['value'].quantile(0.975)
    
]


def draw_line_plot():
    # Draw line plot

    x = df_cleaned['date']
    y = df_cleaned['value']

    length = len(df_cleaned['date'])

    length

    first = 155
    second = 310
    third = 464
    fourth = 619
    fifth = 774
    sixth = 929
    seventh = 1083

    labels = (df_cleaned['date'][first], df_cleaned['date'][second], df_cleaned['date'][third],
              df_cleaned['date'][fourth], df_cleaned['date'][fifth], df_cleaned['date'][sixth],
              df_cleaned['date'][seventh], df_cleaned['date'][length]
            )
    
    fig = plt.figure(figsize=(12, 6))

    ax = fig.add_subplot(111)

    ax.plot(x, y)

    ax.set_xticks(labels)

    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel("Date")
    plt.ylabel("Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

mean_months_2016 = []

for i in np.array([5,6,7,8,9,10,11,12]):
    a = ('%02d' % i)
    month_2016 = '2016-' + a
    extracted_days = []
    for j in df_cleaned['date']:
        if month_2016 in j:
            extracted_days.append(j)
    mean = df_cleaned.loc[(df['date'] >= extracted_days[0]) & (df['date'] <= extracted_days[-1])].mean().value
    mean_months_2016.append(mean)

mean_months_2017 = []

for i in np.array([1,2,3,4,5,6,7,8,9,10,11,12]):
    a = ('%02d' % i)
    month_2017 = '2017-' + a
    extracted_days = []
    for j in df_cleaned['date']:
        if month_2017 in j:
            extracted_days.append(j)
    mean = df_cleaned.loc[(df['date'] >= extracted_days[0]) & (df['date'] <= extracted_days[-1])].mean().value
    mean_months_2017.append(mean)

mean_months_2018 = []

for i in np.array([1,2,3,4,5,6,7,8,9,10,11,12]):
    a = ('%02d' % i)
    month_2018 = '2018-' + a
    extracted_days = []
    for j in df_cleaned['date']:
        if month_2018 in j:
            extracted_days.append(j)
    mean = df_cleaned.loc[(df['date'] >= extracted_days[0]) & (df['date'] <= extracted_days[-1])].mean().value
    mean_months_2018.append(mean)

mean_months_2019 = []

for i in np.array([1,2,3,4,5,6,7,8,9,10,11,12]):
    a = ('%02d' % i)
    month_2019 = '2019-' + a
    extracted_days = []
    for j in df_cleaned['date']:
        if month_2019 in j:
            extracted_days.append(j)
    mean = df_cleaned.loc[(df['date'] >= extracted_days[0]) & (df['date'] <= extracted_days[-1])].mean().value
    mean_months_2019.append(mean)

months = ['January', 'February', 'March', 'April',
          'May', 'June', 'July', 'August',
          'September', 'October', 'November', 'December']

data_2016 = [0,0,0,0] + mean_months_2016

d = {'Months': months, '2016': data_2016, '2017': mean_months_2017, '2018': mean_months_2018, '2019': mean_months_2019}

df1 = pd.DataFrame(data = d)

df1 = pd.melt(df1, id_vars=['Months'], value_vars=['2016', '2017', '2018', '2019'],
        var_name='Years', value_name='Average Page Views')


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    #df_bar = None
    
    global df1


    # Draw bar plot

    g = sns.catplot(x='Years', y='Average Page Views', hue='Months', data = df1, kind='bar', height=5, aspect=1, legend_out = False)

    fig = g.fig



    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    # df_box = df.copy()
    # df_box.reset_index(inplace=True)
    # df_box['year'] = [d.year for d in df_box.date]
    # df_box['month'] = [d.strftime('%b') for d in df_box.date]

    global df1

    months_label = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    

    fig = plt.figure(figsize=(15, 5))

    ax = fig.add_subplot(121)
    sns.boxplot(x = 'Years', y = 'Average Page Views', data = df1, ax = ax).set(xlabel='Year', ylabel='Page Views')
    ax.yaxis.set_ticklabels(["0","20000","40000","60000","80000","100000","120000","140000","160000","180000","200000"]) 
    ax.set(ylim=(0, 160000))
    ax.yaxis.set_major_locator(MultipleLocator(20000))
    ax.title.set_text("Year-wise Box Plot (Trend)")

    ax1 = fig.add_subplot(122)
    sns.boxplot(x = 'Months', y = 'Average Page Views', data = df1, ax = ax1).set(xlabel='Month', ylabel='Page Views')
    ax1.set_xticklabels(months_label)
    ax1.yaxis.set_ticklabels(["0","20000","40000","60000","80000","100000","120000","140000","160000","180000","200000"]) 
    ax1.yaxis.set_major_locator(MultipleLocator(20000))
    ax1.set(ylim=(0, 160000))
    ax1.title.set_text("Month-wise Box Plot (Seasonality)")



    # Draw box plots (using Seaborn)





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
