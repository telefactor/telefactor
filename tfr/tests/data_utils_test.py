import re

from tfr import data_utils


class DescribeNameToId:
    def it_works(self):
        result = data_utils.name_to_id("@Horse.*Cow+ ")
        assert re.fullmatch(r".+:.+:.+", result)
        prefix, name, ts = result.split(":")
        assert prefix == "G"
        assert name == "horse-cow"
        assert re.fullmatch(r"\d+", ts)
