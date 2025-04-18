from openai import OpenAI


def get_sentiment(text: list) -> list:


    """
    Analyzes a list of text strings and classifies the sentiment
    of each string as positve, neutral, negative or irrelevant using Open AI API
    Makes sure the input is a list of strings first and if not text and not equal to a string
    return an error messages saying Wrong input. text must be an array of strings. Strings will
    be strip of white space and /n and appended it to a empty list

    """
    if not text:
        return "Wrong input. text must be an array of strings."
    for i in text:
        if type(i)!=str:
            return "Wrong input. text must be an array of strings."
    #for i in text:
     #   if not isinstance(i,str):
      #      return "Wrong input"
     
    


    system_prompt = """You are a assistant with authority on categorizing sentiments for customer reviews.
    The categories are negative, positive, neutral, and irrelevant. 
    """

    prompt = f"""
    For each line of text in the string below, please categorize the review
    as either positive, neutral, negative, or irrelevant.
    Use only a one-word response per line. Do not include any numbers.
    {text}"""
    

    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
	   { "role": "assistant",  "content": system_prompt },
       { "role": "user",  "content": prompt }
    ]
    
)

 #display the output
    modified_list = response.choices[0].message.content.split("\n")
    strip_list = []
    for sentiment in modified_list:
        sentiment = sentiment.strip()
        strip_list.append(sentiment)
    print(strip_list)    
    
    return strip_list
    
    


    #pass
#in_data = [
 #     "I will never buy another brand again, I love this ring",
  # #   "It's an ok ring. Some features could be better but for the price its fine.",
   #   "its a ring",
     # "Bought this ring and it came broken. rip-off."
   # ]
#error_data1 = []
#error_data2 = [1, 2, 3, 4, 5]
#print(get_sentiment(in_data))
#for i in error_data2:
   # print(type(i))
