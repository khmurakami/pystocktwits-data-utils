#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pystocktwits_data_utils import PyStockTwitData

data = PyStockTwitData()

company_list = ['AAPL', 'VEEV', 'DECK', 'MSFT', 'AMZN']

data.stocktwit_csv_textblob_list_create("../sample_csv_output/"
                                        "stocktwit_csv__list_create_multi.csv",
                                        company_list, 30, 5, limit=30)
