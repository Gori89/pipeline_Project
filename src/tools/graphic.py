import matplotlib.pyplot as plt
import pandas as pd


def createFig(df,df_weather,cont):
    df["Rain"]=df_weather.loc[df.index.date,'rain'].values
    fig= plt.figure(figsize=(10, 6))
    ax1 = fig.add_subplot()

    color = 'tab:blue'
    ax1.set_ylabel("Rain [l/m2]", color=color)  
    ax1.plot(df.index, df.Rain, color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()

    color = 'tab:red'
    ax2.set_xlabel("Time")
    ax2.set_ylabel(cont, color=color)
    ax2.plot(df.index, df[cont], color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    fig.savefig("../Output/fig.png")