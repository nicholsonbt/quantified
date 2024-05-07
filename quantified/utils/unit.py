from typing import Optional, Dict

from quantified.utils.name import Name




class Interpret:
    @staticmethod
    def powerify(text: str):
        assert(isinstance(text, str))

        trans = {
            45: 8315,   # -
            48: 8304,   # 0
            49: 185,    # 1
            50: 178,    # 2
            51: 179,    # 3
            52: 8308,   # 4
            53: 8309,   # 5
            54: 8310,   # 6
            55: 8311,   # 7
            56: 8312,   # 8
            57: 8313,   # 9
        } 

        return text.translate(trans)
    

class UnitTextGenerator:
    def __init__(self, base_units: Optional[Dict['Unit', int]]=None):
        self.units = []
        self.powers = []

        if isinstance(base_units, dict):
            for unit, pow in base_units.items():
                self.insert(pow, unit)


    def insert(self, power, unit):
        for i, p in enumerate(self.powers):
            if power < p or (power == p and unit > self.units[i]):
                self.powers.insert(i, power)
                self.units.insert(i, unit)
                return
        
        self.powers.append(power)
        self.units.append(unit)


    def generate_name(self):
        units = self.units[::-1]
        powers = self.powers[::-1]

        tp = len(units)-1
        for i, pow in enumerate(powers):
            if pow < 0:
                tp = i -1
                break

        texts = []

        for i, unit in enumerate(units):
            pow = abs(powers[i])

            if pow == 1:
                power = ""

            elif pow == 2:
                power = " squared"

            elif pow == 3:
                power = " cubed"

            elif pow == 0:
                continue

            else:
                power = " to the power of " + str(pow)


            if i > tp:
                texts.append("per " + unit._name.get_name(Name.SINGULAR) + power)

            elif i < tp:
                texts.append(unit._name.get_name(Name.SINGULAR) + power)
            
            else:
                texts.append(unit._name.get_name(Name.COMBINED) + power)
        
        return " ".join(texts)
    
    
    def generate_symbol(self):
        units = self.units[::-1]
        powers = self.powers[::-1]

        texts = []
        for i, unit in enumerate(units):
            text = unit._name.symbol
            pow = powers[i]

            if pow == 0:
                continue

            elif pow != 1:
                text += str(pow)

            texts.append(text)

        return Interpret.powerify(" ".join(texts))


class Unit:
    BASE = 0
    DERIVED = 1


    def __init__(self, name=None, components=None):
        assert(not name is None or not components is None)
        self._name = name
        self._components = components


    #region Properties:
    @property
    def is_named(self):
        return not self._name is None
    

    @property
    def is_base(self):
        return self._components is None
    #endregion



    #region Get Components:
    def get_components(self, type_: int=1):
        if self.is_base or (type_ == Unit.DERIVED and self.is_named):
            return {self : 1}

        c0 = {}
        
        for component, power in self._components.items():
            c1 = {k: v*power for k, v in component.get_components(type_).items()}
            c0 = {k: c0.get(k, 0) + c1.get(k, 0) for k in set(c0) | set(c1)}
        
        return c0
    #endregion


    def get_generator(self, type_: int=1):
        components = self.get_components(type_)
        print(components)
        return UnitTextGenerator(components)


    #region Get Name:
    def get_name(self, type_: int=1):
        return self.get_generator(type_).generate_name()
    #endregion



    #region Get Symbol:
    def get_symbol(self, type_: int=1):
        return self.get_generator(type_).generate_symbol()
    #endregion





"""
m = BaseUnit("meter", "m")
s = BaseUnit("second", "s")
kg = BaseUnit("kilogram", "kg")

n = DerivedUnit("newton", "N", kg*m*s**-2)

ft = DerivedUnit("foot", "ft", m, 0.3048, plural="feet")


>>> m.symbol
m

>>> m.name
meter(s)

>>> str(m)
meter(s) [m]

>>> n.symbol
N

>>> n.derived_symbol
N

>>> n.base_symbol
kg m s-2

"""

if __name__ == "__main__":
    m = Unit(name=Name("foot", "m", "feet"))
    s = Unit(name=Name("second", "s"))
    kg = Unit(name=Name("kilogram", "kg"))
    v = Unit(components={kg: 2, m : 1, s : -3})
    print(v.get_name())

