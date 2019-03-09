#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pystocktwits_data_utils.utils import extract_bullish_msgs_from_pd

import pandas as pd

stock_twit_pd = pd.read_table("../sample_csv_output/"
                              "stocktwit_csv_create_VEEV.csv", sep=",")

result = extract_bullish_msgs_from_pd(stock_twit_pd)
print(result)
