#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pystocktwits_data_utils.utils import preprocess_punc

import pandas as pd

# Get the CSV as a pandas dataframe
stock_twits_pd = pd.read_csv("../sample_csv_output/stocktwit_csv_create_VEEV.csv", sep=",")

# Get the header of the CSV
msg = stock_twit_pd[['msgs']]

# Get the list of the CSV
msgs_list = msg.values.tolist()

# Get a single message for testing
word = msgs_list[0][0]

# Use preprocess_punc to remove grammar
punc_check = preprocess_punc(word)
print(punc_check)
