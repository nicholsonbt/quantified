from typing import Union, Optional, overload

# Quantity("5 ft")
# Quantity(5, "ft")




class Unit:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol


class Units:
    Feet = Unit(("foot", "feet"), "ft")
    Metres = Unit("meter", "m")




class Measurement:
    def __init__(self):
        pass





class Length(Measurement):
    def __init__(self, *args):
        if len(args) == 1:
            if isinstance(args[0], str):
                pass




class Quantified:
    def __init__(self, magnitude, units=None):
        self.magnitude = magnitude

        if not units is None:
            self.units = units
        
        assert(hasattr(self, "units"))


    def __repr__(self):
        if isinstance(self.units.name, tuple):
            name = " / ".join(self.units.name)
        else:
            name = self.units.name + "(s)"
        return f"Magnitude: {self.magnitude},\nName: {name},\nSymbol: {self.units.symbol},"
    
    def __str__(self):
        return f"{self.magnitude} {self.units.symbol}"
    

    @overload
    @staticmethod
    def parse(magnitude: Union[int, float], units: str):
        pass

    @overload
    @staticmethod
    def parse(value: str):
        pass

    @staticmethod
    def parse(*args):
        import re

        if len(args) == 1:
            try:
                match = re.match("^[0-9]+[.]?[0-9]*", args[0]).group(0)
            except AttributeError:
                match = None
            
            if match:
                magnitude = float(match)
                unit_str = args[0][len(match):].strip()
            else:
                magnitude = 1.0
                unit_str = args[0].strip()

        elif len(args) == 2:
            magnitude = float(args[0])
            unit_str = args[1]

        else:
            raise ValueError("too many parameters")
        
        subclass = Quantified.get_subclass(unit_str)

        return subclass(magnitude)
    
    @property
    def units_list(self):
        return [self.units.symbol]
    

    @staticmethod
    def get_subclass(units: str):
        for subclass in Quantified.__subclasses__():
            if units in subclass(0).units_list:
                return subclass
            










class MetricPrefix:
    def __init__(self, name, power):
        self.name = name
        self.power = power


class MetricMixin:
    _PREFIXES = {
        "Q" : MetricPrefix("quetta", 30),
        "R" : MetricPrefix("ronna", 27),
        "Y" : MetricPrefix("yotta", 24),
        "Z" : MetricPrefix("zetta", 21),
        "E" : MetricPrefix("exa", 18),
        "P" : MetricPrefix("peta", 15),
        "T" : MetricPrefix("tera", 12),
        "G" : MetricPrefix("giga", 9),
        "M" : MetricPrefix("mega", 6),
        "k" : MetricPrefix("kila", 3),
        "h" : MetricPrefix("hecto", 2),
        "da" : MetricPrefix("deca", 1),
        "d" : MetricPrefix("deci", -1),
        "c" : MetricPrefix("centi", -2),
        "m" : MetricPrefix("milli", -3),
        "u" : MetricPrefix("micro", -6),
        "n" : MetricPrefix("nano", -9),
        "p" : MetricPrefix("pico", -12),
        "f" : MetricPrefix("femto", -15),
        "a" : MetricPrefix("atto", -18),
        "z" : MetricPrefix("zepto", -21),
        "y" : MetricPrefix("yocto", -24),
        "r" : MetricPrefix("ronto", -27),
        "q" : MetricPrefix("quecto", 30),
    }

    def __init__(self):
        pass

    @property
    def units_list(self):
        return [self.units.symbol] + [prefix + self.units.symbol for prefix in MetricMixin._PREFIXES]



class Metre(MetricMixin, Quantified):
    units = Units.Metres


    def __init__(self, magnitude):
        MetricMixin.__init__(self)
        Quantified.__init__(self, magnitude)



class Foot(Quantified):
    units = Units.Feet

    def __init__(self, magnitude):
        Quantified.__init__(self, magnitude)


print("----")
x = Quantified.parse(5.2, "ft")
print(x)
print("----")
x = Quantified.parse("5.2km")
print(repr(x))
print("----")
Quantified.parse("ft")


x = Length(5, "ft")
x = Length(5, Unit("foot", "ft"))
x = Length(5, Foot)
x = Length("5 ft")
x = Length(Foot(5))


x = Foot(5)

print(repr(x))
print(str(x))


class Quantity:
    metric_symbol = "m"

    symbols = {
        "m" : 1,
    }

    def __init__(self, name, base_symbol, description, power=0):
        self.name = name
        self.base_symbol = base_symbol
        self.description = description

    def add_symbols(self, symbol, conversion):
        pass


class Symbol:
    def __init__(self, *units):
        self.units = units








class Value:
    def __init__(self, quantity, units):
        self.quantity = quantity
        self.units = units

    def is_singular_units(self):
        return True


class DerivedMeasurement:
    def __init__(self, name, value, measurement):
        self.name = name
        self.value = value
        self.measurement = measurement

        # if self.value.is_singular_units():
        #     assert(measurement == self.value.units)
        

class BaseMeasurement:
    def __init__(self, name, measurement):
        self.name = name
        self.measurement = measurement






METRIC_BASES = {
    "g" : BaseMeasurement("gram", "mass"),
    "m" : BaseMeasurement("metre", "length"),
    "s" : BaseMeasurement("second", "time"),
    "A" : BaseMeasurement("ampere", "electric current"),
    "K" : BaseMeasurement("kelvin", "thermodynamic temperature"),
    "mol" : BaseMeasurement("mole", "amout of substance"),
    "cd" : BaseMeasurement("candela", "luminous intensity"),
}


PREFIXES = {
    "Q" : MetricPrefix("quetta", 30),
    "R" : MetricPrefix("ronna", 27),
    "Y" : MetricPrefix("yotta", 24),
    "Z" : MetricPrefix("zetta", 21),
    "E" : MetricPrefix("exa", 18),
    "P" : MetricPrefix("peta", 15),
    "T" : MetricPrefix("tera", 12),
    "G" : MetricPrefix("giga", 9),
    "M" : MetricPrefix("mega", 6),
    "k" : MetricPrefix("kila", 3),
    "h" : MetricPrefix("hecto", 2),
    "da" : MetricPrefix("deca", 1),
    "d" : MetricPrefix("deci", -1),
    "c" : MetricPrefix("centi", -2),
    "m" : MetricPrefix("milli", -3),
    "u" : MetricPrefix("micro", -6),
    "n" : MetricPrefix("nano", -9),
    "p" : MetricPrefix("pico", -12),
    "f" : MetricPrefix("femto", -15),
    "a" : MetricPrefix("atto", -18),
    "z" : MetricPrefix("zepto", -21),
    "y" : MetricPrefix("yocto", -24),
    "r" : MetricPrefix("ronto", -27),
    "q" : MetricPrefix("quecto", 30),
}


DERIVED = {
    "t" : DerivedMeasurement("tonne", Value(1, "Mg"), "mass")
}


def parse_mult(units):
    s = units.split("*")

    return [parse_div(un) for un in s]

def parse_div(units):
    s = units.split("/")

    return [parse_pow(s[0])] + [parse_pow(f"{un}^-1") for un in s[1:]]

def parse_pow(units):
    s = units.split("^")
    k = s[0]
    p = 1
    for i in s[1:]:
        p *= int(i)

    pos = p >= 0
    p = abs(p)

    print(parse_unit(k))

    print(k, p, pos)


def parse_unit(units):
    pass


def parse(units):
    return parse_mult(units)


    


parse("kg*m/s^2")
# parse("kg*m*s^-2")
# parse("kg/m/s^2")
# parse("m^2/s^2")
# parse("m^2*s^-2")