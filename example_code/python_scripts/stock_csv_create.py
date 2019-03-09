#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pystocktwits_data_utils import PyStockTwitData

data = PyStockTwitData()

data.stocktwit_csv_create("../sample_csv_output/stocktwit_csv_create_VEEV.csv",
                          "VEEV", 30, 5, limit=30)
