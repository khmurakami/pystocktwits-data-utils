#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from nltk.tokenize import word_tokenize
from textblob import TextBlob

import json
import pandas as pd


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


def extract_bullish_from_csv(input_csv, rows=100,
                             download=False, file_path=None):

    """Get all the bullish statements from the input CSV

    Args:
        input_csv (string): Path to the CSV
        rows (int): Limit for rows to extract
        download (bool)(optional): If you want to download the CSV
        file_path (string)(optional): If download is true

    Return:
        bull_list (list): list of all bullish statements

    """

    df = pd.read_table(input_csv, sep=" ")
    stock_sentiment = df['stock_sentiment']

    return stock_sentiment


def extract_bearish_from_csv(input_csv, rows=100,
                             download=False, file_path=None):

    """Get all the bearish statements from the input CSV

    Args:
        input_csv (string): Path to the CSV
        rows (int): Limit for rows to extract
        download (bool)(optional): If you want to download the CSV
        file_path (string)(optional): If download is true

    Return:
        bull_list (list): list of all bullish statements

    """

    df = pd.read_table(input_csv, sep=" ")
    stock_sentiment = df['stock_sentiment']

    return stock_sentiment


def clean_stopwords(twit, stopwords):

    """Clean twit

    Args:
        twit (string): String you want to clean
        stopwords (list): list of stopwords

    Return:
        preprocess_twit (string): Cleaned String.

    """

    # Use NLTK to seperate each word in the sentence
    twit_tokens = word_tokenize(twit)

    preprocess_twit = []

    # Append words in the list based on the stopwords
    for token in twit_tokens:
        if token not in stopwords:
            preprocess_twit.append(token)

    return preprocess_twit


def clean_punctuation(twit, punc_list):

    """Clean Punctuation

    Args:
        twit (string): Input Twit
        punc_list (list of strings): List of Punctuation

    Return:
        preprocess_twit

    """


def clean_company_symbols(twit):

    """Clean the company symbols

    """


def create_wordcloud(string_list, filepath):

    """Create a word cloud from a list of strings

    Args:
        string_list (list): list of strings
        filepath (string): String of path to save file

    Return:
        True if it worked

    """


def delete_duplicates_in_csv(input_csv_file, output_csv_file):

    """Delete Duplicates in a CSV

    Args:
        input_csv_file: The CSV you want to delete the duplicates from

    Return:
        output_csv_file: The path you want to write the csv to ending
                         with the file name

    """

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
