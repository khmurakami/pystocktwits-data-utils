# pystocktwits_data_utils

Data Tools for the JSON outputs from the pystocktwits wrapper to create datasets. This was made separate from the main repo because the main repo can still expand to using other functions.

# Install

```shell
$ git clone https://github.com/khmurakami/pystocktwits_data_utils.git
$ cd pystocktwits_data_utils
$ python3 setup.py install
```

## Update Submodule
```shell
$ git submodule update --remote --merge
```

# Using this Library

Example of getting all of the sentiment and creating a dataframe from it.

```python
from pystocktwits import Streamer
from pystocktwits_data_utils import *

import requests
import json
import csv
import numpy as np
import pandas as pd

# Get all msgs from this company that is specified
list_of_msgs, list_of_sentiment_json = get_all_msgs_with_sentiment_by_symbol_id("AAPL")

# Parse out the Bullish, Bearish, or None Sentiment
list_of_sentiment = extract_sentiment_statements(list_of_sentiment_json)

# Create a Dataframe
dataframe = pd.DataFrame(
    {'msg': list_of_msgs,
     'sentiment': list_of_sentiment
    })

# Print to see dataframe and save
print(dataframe)
dataframe.to_csv('pystocktwitsdataset.csv')
```

# TODO
- Finish Test Cases
- Clean automatic csv generator
- Make more examples
- Make better README.md

## References

Git ignore was used from this repo: https://github.com/github/gitignore/blob/master/Python.gitignore
