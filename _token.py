import findbyid


@findbyid.findByID
class Token:
    def __init__(self, regex: str, repr: str):
        super().__init__()

        self.regex = regex
        self.repr = repr

