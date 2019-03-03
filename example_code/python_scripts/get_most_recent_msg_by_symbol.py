#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pystocktwits_data_utils import PyStockTwitData

data = PyStockTwitData()

recent_msg = data.get_most_recent_msg_by_symbol_id('AAPL')

print(recent_msg)

# Sample Output
# $AAPL i&#39;d love to have a 1,000 shares of this at $150 average.
