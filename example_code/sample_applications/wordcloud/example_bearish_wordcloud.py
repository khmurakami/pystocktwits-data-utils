#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pystocktwits_data_utils.utils import preprocess_punc
from pystocktwits_data_utils.utils import extract_bearish_msgs_from_pd
from wordcloud import WordCloud

import matplotlib.pyplot as plt
import pandas as pd

# Read in the CSV created by data utils by comma
stock_twit_pd = pd.read_table("../../sample_csv_output/"
                              "stocktwit_csv_create_VEEV.csv", sep=",")

result = extract_bearish_msgs_from_pd(stock_twit_pd)

# Convert the pandas series into a list
msgs_list = result.values.tolist()

# Preprocess each entry in the msgs to clear punctuation
preprocess_list = []
for msg in msgs_list:
    preprocess_list.append(preprocess_punc(str(msg)))

# Concatenate everything in the list to a giant string
string_list = ''.join(preprocess_list)

# Remove all digits from the string
result = ''.join([i for i in string_list if not i.isdigit()])


# Create word cloud
word_cloud = WordCloud(width=512, height=512,
                       background_color='white').generate(result)
plt.figure(figsize=(10, 8), facecolor='white', edgecolor='blue')
plt.imshow(word_cloud)
plt.axis('off')
plt.tight_layout(pad=0)
plt.show()
