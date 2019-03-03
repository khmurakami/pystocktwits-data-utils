#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pystocktwits_data_utils import PyStockTwitData
from pystocktwits_data_utils.utils import textblob_sentiment_polarity

import unittest


class TestDataUtilsMethods(unittest.TestCase):

    def test_get_most_recent_msg_by_user(self):

        data = PyStockTwitData()

        recent_msg = data.get_most_recent_msg_by_user('170')

        # Since the recent msg always changes, just testing if a string
        # is returned

        self.assertEqual(type('test'), type(recent_msg))

    def test_get_most_recent_msg_by_symbol_id(self):

        data = PyStockTwitData()

        recent_msg = data.get_most_recent_msg_by_symbol_id('AAPL')

        # Since the recent msg always changes, just testing if a string
        # is returned

        self.assertEqual(type('test'), type(recent_msg))

    def test_get_most_recent_sentiment_by_user(self):

        data = PyStockTwitData()
        recent_sentiment = data.get_most_recent_sentiment_by_user('170')

        # Since the recent msg always changes, just testing if a dict
        # is returned

        self.assertEqual(type({}), type(recent_sentiment))

    def test_get_most_recent_sentiment_by_symbol(self):

        data = PyStockTwitData()

        recent_sentiment = data.get_most_recent_sentiment_by_symbol_id('AAPL')

        # Since the recent msg always changes, just testing if a dict
        # is returned
        self.assertEqual(type({}), type(recent_sentiment))

    def test_get_all_msgs_with_sentiment_by_user_id(self):

        data = PyStockTwitData()

        msgs, sentiment = data.get_all_msgs_with_sentiment_by_user_id(
                            '170', limit=3)

        # Check if the length equals the limit
        self.assertEqual(3, len(msgs))
        self.assertEqual(3, len(sentiment))

    def test_get_all_msgs_with_sentiment_by_symbol_id(self):

        data = PyStockTwitData()

        msgs, sentiment = data.get_all_msgs_with_sentiment_by_symbol_id(
                            'AAPL', limit=3)

        # Check if the length equals the limit
        self.assertEqual(3, len(msgs))
        self.assertEqual(3, len(sentiment))

    def test_extract_sentiment_statements_basic(self):

        data = PyStockTwitData()

        # Use an example json that this statement parses
        example = [{'sentiment': {'basic': 'Bullish'}}, {'sentiment': None}]
        parsed_sentiment = data.extract_sentiment_statements_basic(example)

        # Check if the parser gets Bullish and None
        self.assertEqual('Bullish', parsed_sentiment[0])
        self.assertEqual(None, parsed_sentiment[1])

    def test_textblob_sentiment_polarity(self):

        example = 'hi'
        sentiment_polarity = textblob_sentiment_polarity(example)

        self.assertEqual(type(3.0), type(sentiment_polarity))


if __name__ == '__main__':
    unittest.main()
