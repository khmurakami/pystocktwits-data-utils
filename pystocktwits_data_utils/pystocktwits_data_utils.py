from pystocktwits import Streamer

import requests
import json
import csv
import pandas as pd
import numpy

# Helper functions placed here for nowself.
# Need to optimize later once I figure out better programming

# Take json and nump it into a file
# Takes in file name and the raw json
# file name needs to be .jsons
def return_json_file(raw_json, file_name):
    with open(file_name, "w") as data_file:
        json.dump(raw_json, data_file, indent=4, sort_keys=True)
    return True

#Return only a msg
def get_most_recent_msg_by_user(user_id):
    twit = Streamer()
    raw_json = twit.get_user_msgs(user_id)
    recent_msg = raw_json['messages'][0]['body']
    return recent_msg

#Return only a msg
def get_most_recent_msg_by_symbol_id(symbol_id):
    twit = Streamer()
    raw_json = twit.get_symbol_msgs(symbol_id)
    recent_msg = raw_json['messages'][0]['body']
    return recent_msg

#Return only sentiment
def get_most_recent_sentiment_by_user(user_id):
    twit = Streamer()
    raw_json = twit.get_user_msgs(user_id)
    recent_sentiment = raw_json['messages'][0]['entities']
    return recent_sentiment

#Return only sentiment
def get_most_recent_sentiment_by_symbol_id(symbol_id):
    twit = Streamer()
    raw_json = twit.get_symbol_msgs(symbol_id)
    recent_sentiment =  raw_json['messages'][0]['entities']
    return recent_sentiment

#Return a dict with msg to senitment
def get_all_msgs_with_sentiment_by_symbol_id(symbol_id):
    msgs = []
    sentiment = []
    twit = Streamer()
    raw_json = twit.get_symbol_msgs(symbol_id = symbol_id, limit=1)
    messages_data = raw_json['messages']
    for message in messages_data:
        msgs.append(message.get("body"))
        sentiment.append(message.get("entities"))
    #sentiment_dict = {msgs[i]: sentiment[i] for i in range(len(msgs))}
    return msgs, sentiment

#Return a dict with msg to sentiment
def get_all_msgs_with_sentiment_by_user_id(user_id):
    msgs = []
    sentiment = []
    twit = Streamer()
    raw_json = twit.get_user_msgs(user_id = user_id, limit=1)
    messages_data = raw_json['messages']
    for message in messages_data:
        msgs.append(message.get("body"))
        sentiment.append(message.get("entities"))
    #sentiment_dict = {msgs[i]: sentiment[i] for i in range(len(msgs))}
    #body = messages_data['body']
    #entities = messages_data['entities']['sentiment']
    return msgs, sentiment

#Using this for temp use
def dict_to_dataframe(dict):
    dataframe = pd.DataFrame(dict)
    return dataframe

#Using this for temp use. Got it from here https://stackoverflow.com/questions/8685809/writing-a-dictionary-to-a-csv-file-with-one-line-for-every-key-value
def dict_to_csv(dict, download_path):
    with open('{}'.format(download_path)) as csv_file:
        reader = csv.reader(csv_file)
        mydict = dict(reader)

def dataframe_to_csv(dataframe, download_path):
    dataframe.to_csv('{}'.format(download_path), index=False, header=False)

# Takes in a list of strings that you need to parse by.
def dict_to_subdict(wanted_keys):
    #wanted_keys = ['l', 'm', 'n'] # The keys you want
    wanted_keys = wanted_keys
    output = dict((k, bigdict[k]) for k in wanted_keys if k in bigdict)
    return output

# Ex: [{'sentiment': {'basic': 'Bullish'}}, {'sentiment': None}]
def extract_sentiment_statements(list_of_sentiment_json):
    example = []
    for i in this:
        if i['sentiment'] is None:
            example.append(i['sentiment'])
        elif i is not None and i['sentiment'] is not None:
            print(i['sentiment']['basic'])
            example.append(i['sentiment']['basic'])
    return example

def textblob_simple_sentiment(msg):
    textblob_sentiment = TextBlob(msg)
    test = textblob_sentiment.sentiment.polarity
    return test

def textblob_sentiment_list(list):
    twitter_sentiment = []
    for i in list_of_msgs:
        twitter_sentiment.append(textblob_simple_sentiment(i))
    return twitter_sentiment


# stocktwit_csv_create('test.csv', 'AAPL', 10, 3)
def stocktwit_csv_create(csv_name, company_id, msg_range, time_delay, header_names):
    csv_name = str(csv_name)
    company_id = str(company_id)
    with open(csv_name, 'w') as f:
	    f.write("msgs, stock_sentiment, twitter_senitment \n")

    for i in range(0, msg_range):
        time.sleep(time_delay)
        list_of_msgs, list_of_sentiment_json = get_all_msgs_with_sentiment_by_symbol_id(company_id)
        list_of_twitter_sentiment = textblob_sentiment_list(list_of_msgs)
        list_of_sentiment = extract_sentiment_statements(list_of_sentiment_json)
        with open(csv_name, 'a', newline='') as f:
            writer=csv.writer(f)
            data = list(zip(list_of_msgs, list_of_sentiment, list_of_twitter_sentiment))
            for row in data:
                row = list(row)
                print(row)
                writer.writerow(row)



if __name__ == '__main__':
    twit = Streamer()
    #print(get_most_recent_msg_by_user("1190"))
    #print(get_most_recent_sentiment_by_user("190"))
    #print(get_most_recent_msg_by_symbol_id("AMZN"))
    #print(get_most_recent_sentiment_by_symbol_id("AMZN"))
    #output = twit.get_user_msgs("1190")
    #print(get_all_msgs_with_sentiment_by_user("190"))
    output = get_all_msgs_with_sentiment_by_symbol_id("AMZN")
    test = dict_to_dataframe(output)
    print(test)
    #dataframe_to_csv(test, 'test.csv')
