# import re

from tfr import data_utils


class DescribeClean:
    def it_works(self):
        result = data_utils.clean("@Horse.*Cow+ ")
        assert result == 'horse-cow'
