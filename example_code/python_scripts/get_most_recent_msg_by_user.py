#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pystocktwits_data_utils import PyStockTwitData

data = PyStockTwitData()

recent_msg = data.get_most_recent_msg_by_user('170')

print(recent_msg)

# Sample Output
# @howardlindzon Thanks man. How did you get so good at this?
