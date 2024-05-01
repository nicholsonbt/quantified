from typing import Union, Optional, overload, Dict
from numbers import Number

# class MetricFactory:
#     class MetricPrefix:
#         def __init__(self, name, power):
#             self.name = name
#             self.power = power

#     _PREFIXES = {
#         "Q" : MetricPrefix("quetta", 30),
#         "R" : MetricPrefix("ronna", 27),
#         "Y" : MetricPrefix("yotta", 24),
#         "Z" : MetricPrefix("zetta", 21),
#         "E" : MetricPrefix("exa", 18),
#         "P" : MetricPrefix("peta", 15),
#         "T" : MetricPrefix("tera", 12),
#         "G" : MetricPrefix("giga", 9),
#         "M" : MetricPrefix("mega", 6),
#         "k" : MetricPrefix("kila", 3),
#         "h" : MetricPrefix("hecto", 2),
#         "da" : MetricPrefix("deca", 1),
#         "d" : MetricPrefix("deci", -1),
#         "c" : MetricPrefix("centi", -2),
#         "m" : MetricPrefix("milli", -3),
#         "u" : MetricPrefix("micro", -6),
#         "n" : MetricPrefix("nano", -9),
#         "p" : MetricPrefix("pico", -12),
#         "f" : MetricPrefix("femto", -15),
#         "a" : MetricPrefix("atto", -18),
#         "z" : MetricPrefix("zepto", -21),
#         "y" : MetricPrefix("yocto", -24),
#         "r" : MetricPrefix("ronto", -27),
#         "q" : MetricPrefix("quecto", 30),
#     }

#     @staticmethod
#     def generate_metric(name: str, symbol: str, derived: Dict['Quantity': int]=None):
#         quantities = [Quantity(name, symbol)]

#         for symbol_prefix, prefix in MetricFactory._PREFIXES.items():
#             quantities.append(prefix.name + name, symbol_prefix + symbol)




class Conversion:
    def __init__(self):
        pass


class LinearConversion(Conversion):
    def __init__(self, scale):
        self._scale


class Units:
    def __init__(self, name: str=None, symbol: str=None, plural: str=None, derivation: Dict['Units', int]={}):
        if plural is None:
            plural = name + "s"

        self._name = name
        self._symbol = symbol
        self._plural = plural
        self._derivation = derivation


    @property
    def symbol(self):
        if self._symbol is None:
            pass
        else:
            return self._symbol
        
    @property
    def name(self):
        if self._name is None:
            pass
        else:
            return self._name
        
    @property
    def plural_name(self):
        if self._plural is None:
            pass
        else:
            return self._plural


class BaseUnits(Units):
    def __init__(self, name: str, symbol: str, plural: str=None):
        Units.__init__(self, name=name, symbol=symbol, plural=plural)


class DerivedUnits(Units):
    def __init__(self, derivation: Dict['Units', int], name: str=None, symbol: str=None, plural: str=None):
        Units.__init__(self, name=name, symbol=symbol, plural=plural, derivation=derivation)
        pass



class Quantity:
    @overload
    def __init__(self, name: str, symbol: str, plural: str=None):
        ...

    @overload
    def __init__(self, derived: Dict['Quantity': int]):
        ...

    @overload
    def __init__(self, name: str, symbol: str, derived: Dict['Quantity': int]):
        ...


    def __init__(self, *args):
        self.name = "length"
        self.symbol = "L"
        self.coherent_units = "m"
        self.additional_units = {
            "mm" : LinearConversion(1000)
        }

    @overload
    def add_units(self, name: str, symbol: str, conversion: Conversion):


length = Quantity("length", "L", "meters", "m")
length.add_units


# Meter = Quantity("meter", "m", metric=True)
# Foot = Quantity("foot", "ft", plural="feet")
# Second = Quantity("second", "s", metric=True)
# Gram = Quantity("gram", "g", metric=True)

""" Definitions:
    - Unit: A generic unit. It should have a name, a symbol, and functions to convert to and from the CoherentUnit.
    - BaseUnit: A base unit.
    - AtomicUnit: A unit that can't be seperated into smaller units. (reverse is compound)
    - DerivedUnit: A unit derived from base units.
    - CoherentUnit: A unit where the conversion is 1.




height = Measurement("5.2 um") -> Measurement (Length): 0.0000052 m
height("mm") -> 0.0052

height.quantity -> Quantity("length", "L")
height.units -> Units("meter", "m")
height.magnitude -> 0.0000052


Conversions.add_conversion(derivation="ft", coherent="m", from_)

Conversions.get_convert(from_="m", to_="ft")




Length = Quantity("length", "L", "meter", "m")

# 1000 mm in 1 m
Length.add_units("millimeter", "mm", LinearConversion(1000))

Conversion(coherent="m", derivation="mm", to_units)
"""








# class LinearConversion:
#     def __init__(self, scale):
#         self._scale = scale

#     def from_coherent(self):
#         return lambda coherent: coherent * self._scale
    
#     def to_coherent(self):
#         return lambda noncoherent: noncoherent / self.scale






# class Units:
#     @overload
#     def __init__(self, name, symbol):
#         # Base units (so also coherent)
#         ...
    
#     @overload
#     def __init__(self, name, symbol):
#         # Base units (so also coherent)
#         ...

















# class CoherentUnits:
#     def __init__(self, name, symbol):
#         self.name = name
#         self.symbol = symbol
#         self.plural = name + "s"
#         self.from_ = None
#         self.to_ = None


# class IncoherentUnits:
#     def __init__(self, name, symbol, plural=None):
#         pass




# class DerivedUnits:
#     def __init__(self, name, symbol, plural=None):
#         pass