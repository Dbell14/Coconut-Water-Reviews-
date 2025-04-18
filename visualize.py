import matplotlib.pyplot as plt


def make_plot(sentiments: list) -> list:
    """
    Assigned each sentiment count to a variable. Then plotted those to 
    a graph per the variable of each sentiment.
    """
    print(f'{sentiments = }')

    a= sentiments.count ("positive")
    b= sentiments.count ("negative")
    c= sentiments.count ("neutral")
    d= sentiments.count ("irrelevant")

    print(a, b, c, d)


    fig, ax = plt.subplots()
    ax.bar(["positive", "negative", "neutral", "irrelevant"], [a,b,c,d])
    ax.set_title("Test Plot")
    ax.set_xlabel("Sentiments")
    ax.set_ylabel("Number of Sentiments")
    fig.savefig("images/graphed_sentiments")
 

