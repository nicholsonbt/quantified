from typing import Union, Optional, overload
from numbers import Number





"""
Definitions:
    Quantity:       A physical quantity (such as length or mass).
    BaseQuantity:   A set of physical quantities from which all other
                    physical quantities can be derived.
    Units:          A standard amount of some physical quantity.
  

"""


# class BaseQuantity:
#     def __init__(self, name, description, definition):
#         self.name = name
#         self.description = description
#         self.definition = definition


#     @property
#     def is_base(self):
#         return True



# class Qunatity(BaseQuantity):
#     def __init__(self, name, description=None, definition=None):
#         BaseQuantity.__init__(self, name, description, definition)


#     @property
#     def is_base(self):
#         return False


class BaseUnit:
    def __init__(self, symbol, name, plural=None):
        if not plural:
            plural = name + "s"

        self.symbol = symbol
        self.name = name
        self.plural = plural

    def __str__(self):
        return self.symbol
    
    def __repr__(self):
        return f"Base Unit: {self.name} / {self.plural} ({self.symbol})"




class Quantity:
    @overload
    def __init__(self, name: str, symbol: str, base_unit: 'BaseUnit'):
        pass

    @overload
    def __init__(self, components: dict):
        pass

        
    def __init__(self, *args):
        self._name = None
        self._symbol = None
        self._base_unit = None
        self._components = {}
        

        if isinstance(args[0], str) and isinstance(args[1], str) and isinstance(args[2], BaseUnit):
            self._name = args[0]
            self._symbol = args[1]
            self._base_unit = args[2]
            
        elif isinstance(args[0], dict):
            self._components = args[0]


    @property
    def components(self):
        if self._name is None:
            return self._components
        
        return {self: 1}
    

    def set_name(self, name):
        self.name = name


    def __truediv__(self, other):
        assert(isinstance(other, Quantity))
        a = self.components
        b = other.components

        reciprocal = {k: -v for k, v in b.items()}
        components = Quantity.__combine_dicts(a, reciprocal)
        return Quantity(components)
    

    def __mul__(self, other):
        assert(isinstance(other, Quantity))
        a = self.components
        b = other.components

        components = Quantity.__combine_dicts(a, b)
        return Quantity(components)
    

    def __pow__(self, modulo):
        assert(isinstance(modulo, int) and not self._name is None)

        if modulo != 0:
            components = {self: modulo}
        else:
            components = {}

        return Quantity(components)


    @staticmethod
    def __combine_dicts(a, b):
        components = {k: a.get(k, 0) + b.get(k, 0) for k in set(a) | set(b)}
        return {k: v for k, v in components.items() if v != 0}
    


    @staticmethod
    def format(k, v, attr):
        k_val = str(getattr(k, attr))

        if v == 1:
            return k_val
        
        return f"{k_val}^{str(v)}"



    def __str__(self):
        attr = "_base_unit"

        if getattr(self, attr) is None:
            components = [Quantity.format(k, v, attr) for k, v in self._components.items()]
            return " * ".join(components)
        
        return str(getattr(self, attr))
    
    def __repr__(self):
        attr = "_name"

        if getattr(self, attr) is None:
            components = [Quantity.format(k, v, attr) for k, v in self._components.items()]
            return " * ".join(components)
        
        return str(getattr(self, attr))


class DerivedQuantity:
    pass











# class Quantity:
#     def __init__(self, name, description, definition):
#         self.name = name
#         self.description = description
#         self.definition = definition
#         self.symbols = {}


#     def add_unit(self, symbol, name, metric=False):
#         pass





# class Units:
#     """ A unit:

#     A unit is a standard amount of some physical quantity.
#     """
#     def __init__(self, units: str, quantity: Optional[Quantity]):
#         pass


# class BaseUnit(Unit):
#     def __init__(self, symbol: str, name: str, quantity: Quantity)







# class Quantified:
#     @overload
#     def __init__(self, value: str):
#         raise NotImplementedError()
    
#     @overload
#     def __init__(self, magnitude: Number):
#         raise NotImplementedError()
    
#     @overload
#     def __init__(self, value: str, quantity: Quantity):
#         raise NotImplementedError()
    
#     @overload
#     def __init__(self, magnitude: Union[Number, str], units: Union[Units, str]):
#         raise NotImplementedError()
    
#     @overload
#     def __init__(self, magnitude: Union[Number, str], units: str, quantity: Quantity):
#         raise NotImplementedError()
    
#     def __init__(self, arg_0, arg_1=None, arg_2=None):
#         print(arg_0, arg_1, arg_2)




# Unitless = Quantity("Unitless", None, None)
# Mass = Quantity("Mass", None, None)
# Mass.add_unit("g", "gram", metric=True)
# Length = Quantity("Length", None, None)


# Length.add_unit("ft", "foot", metric=False, plural="feet")

# Quantified()



























# class Unit:
#     def __init__(self, name, symbol):
#         self.name = name
#         self.symbol = symbol


# class Units:
#     Feet = Unit(("foot", "feet"), "ft")
#     Metres = Unit("meter", "m")




# class Measurement:
#     def __init__(self):
#         pass





# class Length(Measurement):
#     def __init__(self, *args):
#         if len(args) == 1:
#             if isinstance(args[0], str):
#                 pass




# class Quantified:
#     def __init__(self, magnitude, units=None):
#         self.magnitude = magnitude

#         if not units is None:
#             self.units = units
        
#         assert(hasattr(self, "units"))


#     def __repr__(self):
#         if isinstance(self.units.name, tuple):
#             name = " / ".join(self.units.name)
#         else:
#             name = self.units.name + "(s)"
#         return f"Magnitude: {self.magnitude},\nName: {name},\nSymbol: {self.units.symbol},"
    
#     def __str__(self):
#         return f"{self.magnitude} {self.units.symbol}"
    

#     @overload
#     @staticmethod
#     def parse(magnitude: Union[int, float], units: str):
#         pass

#     @overload
#     @staticmethod
#     def parse(value: str):
#         pass

#     @staticmethod
#     def parse(*args):
#         import re

#         if len(args) == 1:
#             try:
#                 match = re.match("^[0-9]+[.]?[0-9]*", args[0]).group(0)
#             except AttributeError:
#                 match = None
            
#             if match:
#                 magnitude = float(match)
#                 unit_str = args[0][len(match):].strip()
#             else:
#                 magnitude = 1.0
#                 unit_str = args[0].strip()

#         elif len(args) == 2:
#             magnitude = float(args[0])
#             unit_str = args[1]

#         else:
#             raise ValueError("too many parameters")
        
#         subclass = Quantified.get_subclass(unit_str)

#         return subclass(magnitude)
    
#     @property
#     def units_list(self):
#         return [self.units.symbol]
    

#     @staticmethod
#     def get_subclass(units: str):
#         for subclass in Quantified.__subclasses__():
#             if units in subclass(0).units_list:
#                 return subclass
            










# class MetricPrefix:
#     def __init__(self, name, power):
#         self.name = name
#         self.power = power


# class MetricMixin:
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

#     def __init__(self):
#         pass

#     @property
#     def units_list(self):
#         return [self.units.symbol] + [prefix + self.units.symbol for prefix in MetricMixin._PREFIXES]



# class Metre(MetricMixin, Quantified):
#     units = Units.Metres


#     def __init__(self, magnitude):
#         MetricMixin.__init__(self)
#         Quantified.__init__(self, magnitude)



# class Foot(Quantified):
#     units = Units.Feet

#     def __init__(self, magnitude):
#         Quantified.__init__(self, magnitude)


# print("----")
# x = Quantified.parse(5.2, "ft")
# print(x)
# print("----")
# x = Quantified.parse("5.2km")
# print(repr(x))
# print("----")
# Quantified.parse("ft")


# x = Length(5, "ft")
# x = Length(5, Unit("foot", "ft"))
# x = Length(5, Foot)
# x = Length("5 ft")
# x = Length(Foot(5))


# x = Foot(5)

# print(repr(x))
# print(str(x))


# class Quantity:
#     metric_symbol = "m"

#     symbols = {
#         "m" : 1,
#     }

#     def __init__(self, name, base_symbol, description, power=0):
#         self.name = name
#         self.base_symbol = base_symbol
#         self.description = description

#     def add_symbols(self, symbol, conversion):
#         pass


# class Symbol:
#     def __init__(self, *units):
#         self.units = units








# class Value:
#     def __init__(self, quantity, units):
#         self.quantity = quantity
#         self.units = units

#     def is_singular_units(self):
#         return True


# class DerivedMeasurement:
#     def __init__(self, name, value, measurement):
#         self.name = name
#         self.value = value
#         self.measurement = measurement

#         # if self.value.is_singular_units():
#         #     assert(measurement == self.value.units)
        

# class BaseMeasurement:
#     def __init__(self, name, measurement):
#         self.name = name
#         self.measurement = measurement






# METRIC_BASES = {
#     "g" : BaseMeasurement("gram", "mass"),
#     "m" : BaseMeasurement("metre", "length"),
#     "s" : BaseMeasurement("second", "time"),
#     "A" : BaseMeasurement("ampere", "electric current"),
#     "K" : BaseMeasurement("kelvin", "thermodynamic temperature"),
#     "mol" : BaseMeasurement("mole", "amout of substance"),
#     "cd" : BaseMeasurement("candela", "luminous intensity"),
# }


# PREFIXES = {
#     "Q" : MetricPrefix("quetta", 30),
#     "R" : MetricPrefix("ronna", 27),
#     "Y" : MetricPrefix("yotta", 24),
#     "Z" : MetricPrefix("zetta", 21),
#     "E" : MetricPrefix("exa", 18),
#     "P" : MetricPrefix("peta", 15),
#     "T" : MetricPrefix("tera", 12),
#     "G" : MetricPrefix("giga", 9),
#     "M" : MetricPrefix("mega", 6),
#     "k" : MetricPrefix("kila", 3),
#     "h" : MetricPrefix("hecto", 2),
#     "da" : MetricPrefix("deca", 1),
#     "d" : MetricPrefix("deci", -1),
#     "c" : MetricPrefix("centi", -2),
#     "m" : MetricPrefix("milli", -3),
#     "u" : MetricPrefix("micro", -6),
#     "n" : MetricPrefix("nano", -9),
#     "p" : MetricPrefix("pico", -12),
#     "f" : MetricPrefix("femto", -15),
#     "a" : MetricPrefix("atto", -18),
#     "z" : MetricPrefix("zepto", -21),
#     "y" : MetricPrefix("yocto", -24),
#     "r" : MetricPrefix("ronto", -27),
#     "q" : MetricPrefix("quecto", 30),
# }


# DERIVED = {
#     "t" : DerivedMeasurement("tonne", Value(1, "Mg"), "mass")
# }


# def parse_mult(units):
#     s = units.split("*")

#     return [parse_div(un) for un in s]

# def parse_div(units):
#     s = units.split("/")

#     return [parse_pow(s[0])] + [parse_pow(f"{un}^-1") for un in s[1:]]

# def parse_pow(units):
#     s = units.split("^")
#     k = s[0]
#     p = 1
#     for i in s[1:]:
#         p *= int(i)

#     pos = p >= 0
#     p = abs(p)

#     print(parse_unit(k))

#     print(k, p, pos)


# def parse_unit(units):
#     pass


# def parse(units):
#     return parse_mult(units)


    


# parse("kg*m/s^2")
# # parse("kg*m*s^-2")
# # parse("kg/m/s^2")
# # parse("m^2/s^2")
# # parse("m^2*s^-2")