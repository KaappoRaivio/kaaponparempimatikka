import re


class RegexDict(dict):
    def __init__(self, _dict):
        temp = {}
        for key, value in _dict.items():
            # import pdb; pdb.set_trace()
            temp[rf"^{key}$"] = value

        super().__init__(**temp)

    def __getitem__(self, item):
        for key in sorted(self, key=len, reverse=True):
            if re.match(key, item):
                return dict.__getitem__(self, key)
                # return key
        else:
            return None
