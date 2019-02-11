from pystocktwits import Streamer
from textblob import TextBlob

import requests
import json
import csv
import pandas as pd


def return_json_file(raw_json, file_name):

    """
    return_json_file is a function that takes in the raw_json and makes it into a nicely formatted json file which I used for debugging purposes like how the json is nested.

    param raw_json(json object): Takes in a json object.
    param file_name(string): file_name is the name of the file name you want to write too.

    return True: Return True if the function executed properly.
    """

    # Open file with the ability to write to the file
    with open(file_name, "w") as data_file:
        json.dump(raw_json, data_file, indent=4, sort_keys=True)

    return True

def get_most_recent_msg_by_user(user_id):

    """
    get_most_recent_msg_by_user: Get the most recent msg by queried by the user_id

    param user_id(string): User id of the user in stocktwits

    return recent_msg(string): The most recent msg
    """

    twit = Streamer()
    raw_json = twit.get_user_msgs(user_id)

    # Parse out the raw json by the json format
    recent_msg = raw_json['messages'][0]['body']

    return recent_msg

def get_most_recent_msg_by_symbol_id(symbol_id):

    """
    get_most_recent_msg_by_symbol_id: Get the most recent msg posted in the company stocktwit

    param symbol_id(string): Symbol id of the company in stocktwits. Ex: 'AAPL'

    return recent_msg(string): The most recent msg
    """

    twit = Streamer()
    raw_json = twit.get_symbol_msgs(symbol_id)

    # Parse out the raw json by the json format
    recent_msg = raw_json['messages'][0]['body']

    return recent_msg

def get_most_recent_sentiment_by_user(user_id):

    """
    get_most_recent_sentiment_by_user: Get the most recent sentiment that the user posted

    param user_id(string): User id of the user in stocktwits.

    return recent_sentiment(dict): The most sentiment posted
    """

    twit = Streamer()
    raw_json = twit.get_user_msgs(user_id)

    # Parse out the raw json by the json format
    recent_sentiment = raw_json['messages'][0]['entities']

    return recent_sentiment

def get_most_recent_sentiment_by_symbol_id(symbol_id):

    """
    get_most_recent_sentiment_by_symbol_id: Get the most recent sentiment that the user posted

    param symbol_id(string): Symbol id of the company in stocktwits.

    return recent_sentiment(dict): The most sentiment posted
    """

    twit = Streamer()
    raw_json = twit.get_symbol_msgs(symbol_id)

    # Parse out the raw json by the json format
    recent_sentiment =  raw_json['messages'][0]['entities']

    return recent_sentiment

def get_all_msgs_with_sentiment_by_symbol_id(symbol_id, limit=0):

    """
    get_all_msgs_with_sentiment_by_symbol_id: Get both sentiment and msgs by symbol id. Limit is 30

    param symbol_id(string): Symbol id of the company in stocktwits.
    param limit(int): Amount of msgs and sentiment you want to see. Limit is 30.

    return msgs(list): List of msgs
    return sentiment(list of json): List of sentiment json
    """

    # Create lists to append the parsed out json too.
    msgs = []
    sentiment = []

    twit = Streamer()
    raw_json = twit.get_symbol_msgs(symbol_id = symbol_id, limit=limit)

    # Get the message body in a list
    messages_data = raw_json['messages']

    # Iterate through all of the "body" and "entities" json and append to list
    for message in messages_data:
        msgs.append(message.get("body"))
        sentiment.append(message.get("entities"))

    return msgs, sentiment

def get_all_msgs_with_sentiment_by_user_id(user_id, limit=0):

    """
    get_all_msgs_with_sentiment_by_user_id: Get both sentiment and msgs by user id. Limit is 30

    param user_id(string): user_id id of the company in stocktwits.
    param limit(int): Amount of msgs and sentiment you want to see. Limit is 30.

    return msgs(list): List of msgs
    return sentiment(list of json): List of sentiment json
    """

    # Create lists to append the parsed out json too.
    msgs = []
    sentiment = []

    twit = Streamer()
    raw_json = twit.get_user_msgs(user_id = user_id, limit=limit)

    # Get the message body in a list
    messages_data = raw_json['messages']

    # Iterate through all of the "body" and "entities" json and append to list
    for message in messages_data:
        msgs.append(message.get("body"))
        sentiment.append(message.get("entities"))

    return msgs, sentiment

# Ex: [{'sentiment': {'basic': 'Bullish'}}, {'sentiment': None}]
def extract_sentiment_statements_basic(list_of_sentiment_json):

    """
    extract_sentiment_statements_basic: Takes a list of json stocktwits sentiment and outputs a list of parsed sentiments. Only works with basic stocktwits avaliable twits

    param list_of_sentiment_json(list of json): user_id id of the company in stocktwits.

    return parsed_sentiment(list of strings): List of parsed sentiment strings
    """

    parsed_sentiments = []

    # Iterate through the list of json
    for i in list_of_sentiment_json:
        # If the sentiment is None append and don't error out
        if i['sentiment'] is None:
            parsed_sentiments.append(i['sentiment'])
        # If the sentiment is not None then parse it out.
        elif i is not None and i['sentiment'] is not None:
            parsed_sentiments.append(i['sentiment']['basic'])

    return parsed_sentiments


def textblob_sentiment_polarity(msg):

    """
    textblob_sentiment_polarity: Take in a string and give you the sentiment polarity based on textblob

    param msg(string): String of what you want to find the polarity of

    return sentiment_polarity(string): sentiment polarity of the input
    """

    # Create a textblob
    textblob_sentiment = TextBlob(msg)
    sentiment_polarity = textblob_sentiment.sentiment.polarity

    return sentiment_polarity

def textblob_sentiment_list(list_of_msgs):

    """
    textblob_sentiment_polarity_list: Take in a list to find all polarties

    param list_of_msgs(string): a list of strings of what you want to find the polarity of

    return sentiment_polarity_list(list of strings): sentiment polarity of the list
    """

    sentiment_polarity_list = []

    for i in list_of_msgs:
        sentiment_polarity_list.append(textblob_simple_sentiment(i))

    return sentiment_polarity_list

# This needs to be cleaned up
def stocktwit_csv_create(csv_name, company_id, msg_range, time_delays, limit=30):

    """
    stocktwit_csv_create: Create a dataset based on the symbol id in the form of a csv

    param csv_name(string): Has to end with .csv. Name of the CSV you want to create
    param company_id(string): The Company Symbol. Ex: 'AAPL'
    param msg_range(int): How many times you want this to execute
    param time_delays(int): Delay before API Call
    param limit(int): How many msgs to get when executing call
    """

    csv_name = str(csv_name)
    company_id = str(company_id)
    with open(csv_name, 'w') as f:
	    f.write("msgs, stock_sentiment, twitter_senitment \n")

    for i in range(0, msg_range):
        time.sleep(time_delay)
        list_of_msgs, list_of_sentiment_json = get_all_msgs_with_sentiment_by_symbol_id(symbol_id=company_id, limit=limit)
        list_of_twitter_sentiment = textblob_sentiment_list(list_of_msgs)
        list_of_sentiment = extract_sentiment_statements(list_of_sentiment_json)
        with open(csv_name, 'a', newline='') as f:
            writer=csv.writer(f)
            data = list(zip(list_of_msgs, list_of_sentiment, list_of_twitter_sentiment))
            for row in data:
                row = list(row)
                print(row)
                writer.writerow(row)
