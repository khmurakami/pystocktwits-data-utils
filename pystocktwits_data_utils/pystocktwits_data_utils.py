#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pystocktwits import Streamer
from .utils import textblob_sentiment_list

import csv
import time


class PyStockTwitData():

    def __init__(self):

        self.streamer = Streamer()

    def get_most_recent_msg_by_user(self, user_id):

        """Get the most recent msg by queried by the user_id

        Args:
            user_id (string): User id of the user in stocktwits

        Return:
            recent_msg (string): The most recent msg

        """

        twit = self.streamer
        raw_json = twit.get_user_msgs(user_id)

        # Parse out the raw json by the json format
        recent_msg = raw_json['messages'][0]['body']

        return recent_msg

    def get_most_recent_msg_by_symbol_id(self, symbol_id):

        """Get the most recent msg posted in the company stocktwit

        Args:
            symbol_id (string): Symbol id of the company in stocktwits.
                               Ex: 'AAPL'

        Return
            recent_msg (string): The most recent msg

        """

        twit = self.streamer
        raw_json = twit.get_symbol_msgs(symbol_id)

        # Parse out the raw json by the json format
        recent_msg = raw_json['messages'][0]['body']

        return recent_msg

    def get_most_recent_sentiment_by_user(self, user_id):

        """Get the most recent sentiment that the user posted

        Args:
            user_id (string): User id of the user in stocktwits.

        Return:
            recent_sentiment (dict): The most sentiment posted
        """

        twit = self.streamer
        raw_json = twit.get_user_msgs(user_id)

        # Parse out the raw json by the json format
        recent_sentiment = raw_json['messages'][0]['entities']

        return recent_sentiment

    def get_most_recent_sentiment_by_symbol_id(self, symbol_id):

        """ Get the most recent sentiment that the user posted

        Args:
            symbol_id (string): Symbol id of the company in stocktwits.

        Return:
            recent_sentiment (dict): The most sentiment posted
        """

        twit = self.streamer
        raw_json = twit.get_symbol_msgs(symbol_id)

        # Parse out the raw json by the json format
        recent_sentiment = raw_json['messages'][0]['entities']

        return recent_sentiment

    def get_all_msgs_with_sentiment_by_symbol_id(self, symbol_id, limit=0):

        """Get both sentiment and msgs by symbol id. Limit is 30

        Args:
            symbol_id (string): Symbol id of the company in stocktwits.
            limit (int): Amount of msgs and sentiment you want to see.
                         Limit is 30.

        Return:
             msgs(list): List of msgs
             sentiment(list of json): List of sentiment json

        """

        # Create lists to append the parsed out json too.
        msgs = []
        sentiment = []

        twit = self.streamer
        raw_json = twit.get_symbol_msgs(symbol_id=symbol_id, limit=limit)

        # Get the message body in a list
        messages_data = raw_json['messages']

        # Iterate all of the "body" and "entities" json and append to list
        for message in messages_data:
            msgs.append(message.get("body"))
            sentiment.append(message.get("entities"))

        return msgs, sentiment

    def get_all_msgs_with_sentiment_by_user_id(self, user_id, limit=30):

        """Get both sentiment and msgs by user_id. Limit is 30

        Args:
            user_id (string): user_id id of the company in stocktwits.
            limit (int): Amount of msgs and sentiment you want to see.
                         Limit is 30.

        Return:
             msgs(list): List of msgs
             sentiment(list of json): List of sentiment json

        """

        # Create lists to append the parsed out json too.
        msgs = []
        sentiment = []

        twit = self.streamer
        raw_json = twit.get_user_msgs(user_id=user_id, limit=limit)

        # Get the message body in a list
        messages_data = raw_json['messages']

        # Iterate all of the "body" and "entities" json and append to list
        for message in messages_data:
            msgs.append(message.get("body"))
            sentiment.append(message.get("entities"))

        return msgs, sentiment

    # Ex: [{'sentiment': {'basic': 'Bullish'}}, {'sentiment': None}]
    def extract_sentiment_statements_basic(self, list_of_sentiment_json):

        """Takes a list of json stocktwits sentiment and outputs a list of
        parsed sentiments. Only works with basic stocktwits avaliable twits

        Args:
            list_of_sentiment_json (list of json): user_id id of the company

        Return:
            parsed_sentiment (list of strings): List of parsed sentiment
                                                strings
        """

        # Check if the input is empty
        if len(list_of_sentiment_json) is None:
            raise Exception("The json list is empty")

        # List to contain parsed_sentiment
        parsed_sentiments = []

        # Iterate through the list of json
        for sentiment in list_of_sentiment_json:

            # If the sentiment is None append and don't error out
            if sentiment['sentiment'] is None:
                parsed_sentiments.append(sentiment['None'])

            # If the sentiment is not None then parse it out.
            elif sentiment is not None and sentiment['sentiment'] is not None:
                parsed_sentiments.append(sentiment['sentiment']['basic'])

        return parsed_sentiments

    def stocktwit_csv_create(self, csv_name, company_id, loop_limit,
                             time_delay, limit=30):

        """Create a dataset based on the symbol id in the form of a csv

        Args:
            csv_name (string): Has to end with .csv. Name of the CSV
                               you want to create
            company_id (string): The Company Symbol. Ex: 'AAPL'
            loop_limit(int): How many times you want this to execute
            time_delays(int): Delay before API Call in seconds
            limit(int): How many msgs to get when executing call

        """

        print("To end this function, use Control+C or wait for loop limit\n")

        # Create a CSV
        with open(csv_name, 'w') as f:
            f.write("msgs, stock_sentiment \n")

        # Instead of infinite loop, just set range
        for i in range(0, loop_limit):

            # Set delay for calling again in seconds
            time.sleep(time_delay)
            list_of_msgs, list_of_sentiment_json = (
                self.get_all_msgs_with_sentiment_by_symbol_id(
                    symbol_id=company_id, limit=limit))

            list_of_sentiment = self.extract_sentiment_statements(
                                list_of_sentiment_json)

            # After getting the list of sentiment, append to CSV
            with open(csv_name, 'a', newline='') as f:
                writer = csv.writer(f)

                # Zip to append by list to append by columns
                data = list(zip(list_of_msgs, list_of_sentiment))
                for row in data:
                    row = list(row)
                    writer.writerow(row)
                    print("Wrote Row")

    def stock_csv_list_create(self, csv_name, company_list,
                              loop_limit, time_delay, limit=30):

        """Create a dataset based on the symbol id in the form of a csv

        Args:
            csv_name (string): Has to end with .csv. Name of the CSV
                               you want to create
            company_list (list): The Company Symbol. Ex: 'AAPL'
            loop_limit(int): How many times you want this to execute
            time_delays(int): Delay before API Call in seconds
            limit(int): How many msgs to get when executing call

        """

        print("To end this function, use Control+C or wait for loop limit\n")

        # Create a CSV
        with open(csv_name, 'w') as f:
            f.write("msgs, stock_sentiment \n")

        # Instead of infinite loop, just set range
        for i in range(0, loop_limit):

            # Set delay for calling again in seconds
            time.sleep(time_delay)

            for company in company_list:

                list_of_msgs, list_of_sentiment_json = (
                    self.get_all_msgs_with_sentiment_by_symbol_id(
                        symbol_id=company, limit=limit))

                list_of_sentiment = self.extract_sentiment_statements(
                                    list_of_sentiment_json)

                # After getting the list of sentiment, append to CSV
                with open(csv_name, 'a', newline='') as f:
                    writer = csv.writer(f)

                    # Zip to append by list to append by columns
                    data = list(zip(list_of_msgs, list_of_sentiment))
                    for row in data:
                        row = list(row)
                        writer.writerow(row)
                        print("Wrote Row")

    def stocktwit_csv_textblob_list_create(self, csv_name, company_list,
                                           loop_limit, time_delay, limit=30):

        """Create a dataset based on the symbol id in the form of a csv with
           textblob sentiment info

        Args:
            csv_name (string): Has to end with .csv. Name of the CSV
                               you want to create
            company_id (string): The Company Symbol. Ex: 'AAPL'
            loop_limit(int): How many times you want this to execute
            time_delays(int): Delay before API Call in seconds
            limit(int): How many msgs to get when executing call

        """

        print("To end this function, use Control+C or wait for loop limit\n")

        # Create a CSV
        with open(csv_name, 'w') as f:
            f.write("msgs, stock_sentiment, twitter_senitment \n")

        # Instead of infinite loop, just set range
        for i in range(0, loop_limit):

            # Set delay for calling again in seconds
            time.sleep(time_delay)

            for company in company_list:

                list_of_msgs, list_of_sentiment_json = (
                    self.get_all_msgs_with_sentiment_by_symbol_id(
                        symbol_id=company, limit=limit))

                list_of_twitter_sentiment = textblob_sentiment_list(
                                            list_of_msgs)

                list_of_sentiment = self.extract_sentiment_statements(
                                    list_of_sentiment_json)

                # After getting the list of sentiment, append to CSV
                with open(csv_name, 'a', newline='') as f:
                    writer = csv.writer(f)

                    # Zip to append by list to append by columns
                    data = list(zip(list_of_msgs, list_of_sentiment,
                                    list_of_twitter_sentiment))

                    for row in data:
                        row = list(row)
                        writer.writerow(row)
                        print("Wrote Row")
