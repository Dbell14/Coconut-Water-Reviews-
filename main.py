from label import get_sentiment
from visualize import make_plot

import json


def run(filepath: str):
    """
    Took in filepaht to a json file and extracted the reviews from the json file
    Used the get_sentiment () function to analyze each review and make_plot to show
    number of each sentiment. 
    """
    # open the json object
    with open(filepath, "r") as file:
        results = json.load(file)

    # extract the reviews from the json file
    extracted_reviews = results["results"]
    #print(extracted_reviews)

    # get a list of sentiments for each line using get_sentiment
    ended_sentiments = get_sentiment(extracted_reviews)

    # plot a visualization expressing sentiment ratio
    make_plot(ended_sentiments)


   # return sentiments
    print(ended_sentiments)
    sentiment_count = zip(extracted_reviews, ended_sentiments)
    #print(list(sentiment_count))
    for review, sentiments in sentiment_count:
        print(f"review:{review}\n sentiment:{sentiments}\n")
    
   
    return ended_sentiments


if __name__ == "__main__":
    print(run("data/raw/reviews.json"))


