





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