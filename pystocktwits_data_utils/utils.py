#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from textblob import TextBlob


import json


def textblob_sentiment_polarity(msg):

    """Take in a string and give you the sentiment polarity based on textblob

    Args:
        msg(string): String of what you want to find the polarity of

    Return:
        sentiment_polarity(string): sentiment polarity of the input

    """

    # Create a textblob
    textblob_sentiment = TextBlob(msg)
    sentiment_polarity = textblob_sentiment.sentiment.polarity

    return sentiment_polarity


def textblob_sentiment_list(list_of_msgs):

    """Take in a list to find all polarties

    Args:
        list_of_msgs(string): a list of strings of what you want to
                              find the polarity of.

    Return:
        sentiment_polarity_list(list of strings): sentiment polarity of
                                                  the list.

    """
    # Check if the input is empty
    if len(list_of_msgs) is None:
        raise Exception("The json list is empty")

    sentiment_polarity_list = []

    for i in list_of_msgs:
        sentiment_polarity_list.append(textblob_sentiment_polarity(i))

    return sentiment_polarity_list


def return_json_file(raw_json, file_name):

    """function that takes in the raw_json and makes it into a
       nicely formatted json file

    Args:
        raw_json(json object): Takes in a json object.
        file_name(string): file_name is the name of the file name you want to
                           write too.

    Return:
        True: Return True if the function executed properly.

    """

    # Open file with the ability to write to the file
    with open(file_name, "w") as data_file:
        json.dump(raw_json, data_file, indent=4, sort_keys=True)

    return True


def delete_duplicates_in_csv(input_csv_file, output_csv_file):

    input_csv = open(input_csv_file, 'r')
    output_csv = open(output_csv_file, 'w')

    listLines = []

    for line in input_csv:
        if line in listLines:
            continue
        else:
            output_csv.write(line)
            listLines.append(line)

    output_csv.close()
    input_csv.close()
