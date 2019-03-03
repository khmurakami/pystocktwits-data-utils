# pystocktwits_data_utils

[![Build Status](https://travis-ci.com/khmurakami/pystocktwits_data_utils.svg?branch=master)](https://travis-ci.com/khmurakami/pystocktwits_data_utils)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![CodeFactor](https://www.codefactor.io/repository/github/khmurakami/pystocktwits_data_utils/badge)](https://www.codefactor.io/repository/github/khmurakami/pystocktwits_data_utils)
![GitHub All Releases](https://img.shields.io/github/downloads/khmurakami/pystocktwits_data_utils/total.svg)
[![HitCount](http://hits.dwyl.com/khmurakami/pystocktwits_data_utils.svg)](http://hits.dwyl.com/khmurakami/pystocktwits_data_utils)



Data Tools for the JSON outputs from the pystocktwits wrapper to create datasets. This was made separate from the main repo because only includes wrappers for the web calls to stocktwits and it can be expanded on for the oauth tools.

Link to main repo: https://github.com/khmurakami/pystocktwits

# Install

```shell
$ git clone https://github.com/khmurakami/pystocktwits_data_utils.git
$ git pull --recurse-submodules
$ cd pystocktwits_data_utils
$ python3 setup.py install
$ cd pystocktwtis
$ python setup.py install
```

## Update Submodule
```shell
$ git submodule update --remote --merge
```

# Using this Library

#### Example of getting all of the sentiment and creating a dataframe from it.

```python
from pystocktwits_data_utils import PyStockTwitData

data = PyStockTwitData()

# Get all msgs from this company that is specified
list_of_msgs, list_of_sentiment_json = data.get_all_msgs_with_sentiment_by_symbol_id("AAPL")

# Parse out the Bullish, Bearish, or None Sentiment
list_of_sentiment = data.extract_sentiment_statements(list_of_sentiment_json)

# Create a Dataframe
dataframe = pd.DataFrame(
    {'msg': list_of_msgs,
     'sentiment': list_of_sentiment
    })

# Print to see dataframe and save
print(dataframe)
dataframe.to_csv('pystocktwitsdataset.csv')
```

#### Leaving your computer on and collecting data into a CSV

```python

from pystocktwits_data_utils import PyStockTwitData

data = PyStockTwitData()

# This needs to be cleaned up

# Create a CSV named VEEV.csv
# Get the company VEEV
# Get the recent 30 messages
# Wait 600 seconds before checking again
# Set limit messages to 30
data.stocktwit_csv_create("VEEV.csv", "VEEV", 30, 600, limit=30):

```

Example Result

| msg                                                                              | sentiment |
|----------------------------------------------------------------------------------|-----------|
| $VEEV that was the 110 bounce I called for but it happened very fast             | Bullish   |
| #Update(17),$VEEV Feb-15 105 Calls Up +206%.,since alerted on: Jan 23. Peak 262% | Bullish   |

## TODO
- Make better README.md
- Add timestamp to csv generator
- Add Company ID to csv generator

## Links/Credits

- IcyFlames CSV Duplicates Removal with no new libraries: https://stackoverflow.com/questions/15741564/removing-duplicate-rows-from-a-csv-file-using-a-python-script
- Git ignore was used from this repo: https://github.com/github/gitignore/blob/master/Python.gitignore
