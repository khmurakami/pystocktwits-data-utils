#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pystocktwits_data_utils import PyStockTwitData

data = PyStockTwitData()

example = [{'sentiment': {'basic': 'Bullish'}}, {'sentiment': None}]
parsed_sentiment = data.extract_sentiment_statements_basic(example)

print(parsed_sentiment)

# Sample Output
# ['Bullish', 'None']
