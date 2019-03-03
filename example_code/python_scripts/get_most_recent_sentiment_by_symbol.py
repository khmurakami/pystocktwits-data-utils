#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pystocktwits_data_utils import PyStockTwitData
from pystocktwits_data_utils.utils import return_json_file

data = PyStockTwitData()

recent_msg = data.get_most_recent_sentiment_by_symbol_id('AAPL')

print(recent_msg)

return_json_file(recent_msg,
                 "../sample_json_output/get_most_recent_sentiment_by_symbol.json")
