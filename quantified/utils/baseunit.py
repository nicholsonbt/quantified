


class BaseUnit:
    def __init__(self, name: str, symbol: str, plural: str=None):
        self._name = name
        self._symbol = symbol
        self._plural = plural

    @property
    def singular_name(self):
        return self._name
    
    @property
    def plural_name(self):
        if self._plural is None:
            return self.singular_name + "s"
        
        return self._plural
    
    @property
    def name(self):
        n = len(self.singular_name)

        if self.plural_name == self.singular_name:
            return self.singular_name
        
        if n < len(self.plural_name) and self.plural_name[:n] == self.singular_name:
            return f"{self.singular_name}({self.plural_name[n:]})"
        
        return f"{self.singular_name}/{self.plural_name}"
    
    @property
    def symbol(self):
        return self._symbol
    
    @property
    def components(self):
        return {self : 1}
    

    def __truediv__(self, other):
        if issubclass(other.__class__, BaseUnit):
            reciprocal = {k: -v for k, v in other.components.items()}
            pass


    def __mul__(self, other):
        if issubclass(other.__class__, BaseUnit):
            components = {k : v*pow for k, v in self.components.items()}


    def __pow__(self, pow):
        if isinstance(pow, int):
            components = {k : v*pow for k, v in self.components.items()}




    def __truediv__(self, other):
        assert(isinstance(other, Dimension))
        a = self.components
        b = other.components

        reciprocal = {k: -v for k, v in b.items()}
        components = Dimension.__combine_dicts(a, reciprocal)
        return Dimension(components)
    

    def __mul__(self, other):
        assert(isinstance(other, Dimension))
        a = self.components
        b = other.components

        components = Dimension.__combine_dicts(a, b)
        return Dimension(components)
    

    def __pow__(self, modulo):
        assert(isinstance(modulo, int) and not self._name is None)

        if modulo != 0:
            components = {self: modulo}
        else:
            components = {}

        return Dimension(components)


    @staticmethod
    def __combine_dicts(a, b):
        components = {k: a.get(k, 0) + b.get(k, 0) for k in set(a) | set(b)}
        return {k: v for k, v in components.items() if v != 0}