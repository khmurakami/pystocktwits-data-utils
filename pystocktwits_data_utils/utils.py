#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from nltk.tokenize import word_tokenize
from textblob import TextBlob

import json
import pandas as pd
import re


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


def extract_bullish_msgs_from_csv(input_csv, file_name):

    """Get all the bullish statements from the input CSV

    Args:
        input_csv (string): Path to the CSV
        rows (int): Limit for rows to extract
        download (bool)(optional): If you want to download the CSV
        file_path (string)(optional): If download is true

    Return:
        True

    """

    input_pd = pd.read_table(input_csv, sep=",")

    query_result = input_pd.query('stock_sentiment=="Bullish"')['msgs']
    bullish_csv = pd.DataFrame(query_result.values, columns=["msgs"])
    bullish_csv.to_csv(file_name)


def extract_bullish_msgs_from_pd(input_pd):

    """Get all the bullish statements from the input Pandas Dataframe

    """

    query_result = input_pd.query('stock_sentiment=="Bullish"')['msgs']
    bullish_pd = pd.DataFrame(query_result.values, columns=["msgs"])

    return bullish_pd


def extract_bearish_msgs_from_csv(input_csv, file_name):

    """Get all the bearish statements from the input CSV

    Args:
        input_csv (string): Path to the CSV
        rows (int): Limit for rows to extract
        download (bool)(optional): If you want to download the CSV
        file_path (string)(optional): If download is true

    Return:
        bull_list (list): list of all bullish statements

    """

    input_pd = pd.read_table(input_csv, sep=",")

    query_result = input_pd.query('stock_sentiment=="Bearish"')['msgs']
    bearish_csv = pd.DataFrame(query_result.values, columns=["msgs"])
    bearish_csv.to_csv(file_name)


def extract_bearish_msgs_from_pd(input_pd):

    """Get all the bullish statements from the input Pandas Dataframe

    """

    query_result = input_pd.query('stock_sentiment=="Bearish"')['msgs']
    bearish_pd = pd.DataFrame(query_result.values, columns=["msgs"])

    return bearish_pd


def preprocess_stopwords(twit, stopwords):

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


def preprocess_punc(twit):

    """Clean Punctuation

    Args:
        twit (string): Input Twit
        punc_list (list of strings): List of Punctuation

    Return:
        preprocess_twit

    """

    if type(twit) is not str:
        raise Exception("This is not a string")

    url_free = re.sub(r'http\S+', '', twit)
    punc_free_twit = re.sub(r'[^\w\s_]+', '', url_free).strip()

    return punc_free_twit


def preprocess_company_symbols(twit):

    """Clean the company symbols

    """
    pass


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
