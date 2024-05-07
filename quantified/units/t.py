





# meter = BaseUnits("meter", "m")
# second = BaseUnits("second", "s")


class Conversion:
    def __init__(self, from_, to_):
        self.__from = from_
        self.__to = to_


    def from_base(self, value=None):
        if value is None:
            return self.__from
        
        return self.__from(value)


    def to_base(self, value=None):
        if value is None:
            return self.__to
        
        return self.__to(value)




class LinearConversion(Conversion):
    def __init__(self, k):
        Conversion.__init__(self, lambda base: base * k, lambda derived: derived / k)


class AffineConversion(Conversion):
    def __init__(self, c, k=1):
        Conversion.__init__(self, lambda base: base * k + c, lambda derived: (derived - c) / k)










# length.set_base("meter", "m")
# length.add_units("foot", "ft", LinearConversion(3.28084))


# temperature.set_base("kelvin", "K")
# temperature.add_units("degrees celcius", "*C", AffineConversion(-273.15, 0))

feet = 2
celcius = 21.5

a = LinearConversion(3.28084)
b = AffineConversion(-273.15)

print(a.to_base(feet))
print(b.to_base(celcius))


# Dimension:
# Type: <base or derived>
# Name: <name> <?base_names?>
# Symbol: <symbol> <?base_symbols?>
# Base Units: <name> <symbol>

## Examples:

# Dimension:
# Type: base
# Name: length
# Symbol: L
# Base Units: meters (m)

# Dimension:
# Type: derived
# Name: velocity (length / time)
# Symbol: L / T
# Base Units: meters per second (m/s)






# Atomic Units:
# Type: <base or derived>
# Name: <name>
# Symbol: <symbol> <?base_symbols?>

## Examples

# Atomic Units:
# Type: base
# Name: meter(s)
# Symbol: m

# Atomic Units:
# Type: base
# Name: foot / feet
# Symbol: ft

# Atomic Units:
# Type: derived
# Name: newton(s)
# Symbol: N (kg m / s^2)




# Composite Units:
# Type: <base or derived>
# Name: <base names>
# Symbol: <symbol> <base symbols>






# Units:
# Type: <atomic or composite>
# Name: <atomic name or ???>
# Symbol: <atomic symbol or ???>


## Examples:
# Units:
# Type: Atomic (Base)
# Name: meter(s)
# Symbol: m

# Units:
# Type: Atomic (Derived)
# Name: newton(s)
# Symbol: N (kg m / s^2)

# Units:
# Type: Composite (Base)
# Name: meter(s) per second
# Symbol: m / s

# Units:
# Type: Composite (Derived)
# Name: newton second(s)
# Symbol: N s (kg m / s)