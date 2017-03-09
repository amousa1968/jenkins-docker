# coding: utf-8

import unittest

from config_reader import ConfigReader

class TestConfigReader(unittest.TestCase):

    def setUp(self):
        self.config = ConfigReader("""
            <root>
                <person>
                    <name>fake</name>
                    <age>15</age>
                </person>
                <person>
                    <name>test</name>
                    <age>43</age>
                </person>
            </root>
            """)


    def test_get_names(self):
        self.assertEqual(self.config.get_names(), ['fake', 'test'])

    def test_get_ages(self):
        self.assertEqual(self.config.get_ages(), ['15', '43'])
