import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df=pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig,ax = plt.subplots()
    plt.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea   Level'])

    # Create first line of best fit
    res=linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])

    df_predicted=pd.DataFrame(pd.Series(np.arange(2014,2051)), columns=['Year'])
    df_predicted['CSIRO Adjusted Sea Level']=res.intercept + res.slope*df_predicted['Year']
    df1=pd.concat([df,df_predicted]).reset_index(drop=True)

  
    # Create second line of best fit
    df_filtered=df.loc[(df['Year']>=2000)]
    res2=linregress(x=df_filtered['Year'], y=df_filtered['CSIRO Adjusted Sea Level'])

    df_predicted2=pd.DataFrame(pd.Series(np.arange(2014,2051)), columns=['Year'])
    df_predicted2['CSIRO Adjusted Sea Level']=res2.intercept + res2.slope*df_predicted2['Year']
    
    df2=pd.concat([df_filtered,df_predicted2]).reset_index(drop=True)

    # Add labels and title
    fig, (ax, ax1) = plt.subplots(1,2)
    fig.set_figheight(10)
    fig.set_figwidth(20)
    
    ax.scatter(df1['Year'], y=df1['CSIRO Adjusted Sea Level'], label='original line')
    ax.plot(df1['Year'], res.intercept + res.slope*df1['Year'], 'r', label='fitted line')
    ax.set_title("Rise in Sea Level")
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
  
  
    ax1.scatter(df2['Year'], y=df2['CSIRO Adjusted Sea Level'], label='original line')
    ax1.plot(df2['Year'], res2.intercept + res2.slope*df2['Year'], 'r', label='fitted line')
    ax1.legend()
    ax1.set_title("Rise in Sea Level")
    ax1.set_xlabel("Year")
    ax1.set_ylabel("Sea Level (inches)")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
