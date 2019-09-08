import matplotlib.pyplot as plt


def createFig(df):
    fig, ax = plt.subplots()
    df.plot(y="BEN", ax=ax,figsize=(5,5))
    #plt.xticks(rotation='25')
    fig.savefig("fig.png")