


class Name:
    SINGULAR = 0
    PLURAL = 1
    COMBINED = 2

    def __init__(self, singular: str, symbol: str, plural: str=None):
        self._singular = singular
        self._symbol = symbol
        self._plural = plural


    @property
    def symbol(self):
        return self._symbol

    
    @property
    def singular(self):
        return self._singular
    

    @property
    def plural(self):
        if self._plural is None:
            return self._singular + "s"
        
        return self._plural
    

    @property
    def combined(self):
        n = len(self.singular)

        if self.plural == self.singular:
            return self.singular
        
        if n < len(self.plural) and self.plural[:n] == self.singular:
            return f"{self.singular}({self.plural[n:]})"
        
        return f"{self.singular}/{self.plural}"


    def get_name(self, format_: int):
        if format_ == Name.SINGULAR:
            return self.singular
        
        if format_ == Name.PLURAL:
            return self.plural
        
        return self.combined
        
