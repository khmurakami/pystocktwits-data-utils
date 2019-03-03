#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pystocktwits_data_utils import PyStockTwitData

import panda as pd

data = PyStockTwitData()

# Get all msgs from this company that is specified
list_of_msgs, list_of_sentiment_json = (
    data.get_all_msgs_with_sentiment_by_symbol_id("VEEV"))

# Parse out the Bullish, Bearish, or None Sentiment
list_of_sentiment = (
    data.extract_sentiment_statements_basic(list_of_sentiment_json))

# Create a Dataframe
dataframe = pd.DataFrame(
    {
        'msg': list_of_msgs,
        'sentiment': list_of_sentiment
    }
)

# Print to see dataframe and save
print(dataframe)
dataframe.to_csv('../sample_csv_output/pystockdataset.csv')
