#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pystocktwits import Streamer
from pystocktwits_data_utils import *

# Get all msgs from this company that is specified
list_of_msgs, list_of_sentiment_json = get_all_msgs_with_sentiment_by_symbol_id("VEEV")

# Parse out the Bullish, Bearish, or None Sentiment
list_of_sentiment = extract_sentiment_statements_basic(list_of_sentiment_json)

# Create a Dataframe
dataframe = pd.DataFrame(
    {'msg': list_of_msgs,
     'sentiment': list_of_sentiment
    })

# Print to see dataframe and save
print(dataframe)
dataframe.to_csv('pystockdataset2.csv')
