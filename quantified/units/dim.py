from typing import Union, Optional, overload, Dict
from numbers import Number





class Unit:
    def __init__(self, name: str, symbol: str, plural=None):
        if plural is None:
            plural = name + "s"

        self.singular = name
        self.plural = plural
        self.symbol = symbol


    @property
    def name(self):
        if self.plural == self.singular:
            return self.singular
        
        n = len(self.singular)
        if self.plural[:n] == self.singular:
            return f"{self.singular}({self.plural[n:]})"
        
        return f"{self.singular}/{self.plural}"
    

    def __str__(self):
        return f"{self.name} [{self.symbol}]"
    

    def __repr__(self):
        return "Unit:\n - Name: {self.name},\n - Symbol: {self.symbol},"



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
                texts.append("per " + unit.singular + power)

            elif i < tp:
                texts.append(unit.singular + power)
            
            else:
                texts.append(unit.name + power)
        
        return " ".join(texts)
    
    def generate_symbol(self):
        units = self.units[::-1]
        powers = self.powers[::-1]

        texts = []
        for i, unit in enumerate(units):
            text = unit.symbol
            pow = powers[i]

            if pow == 0:
                continue

            elif pow != 1:
                text += str(pow)

            texts.append(text)

        return Interpret.powerify(" ".join(texts))

            
        



class Dimension:
    """
    Attributes
    ----------
    name:   The name of the dimension.
    symbol: The symbol representing the dimension.

    





    Methods
    -------


    """
    @overload
    def __init__(self, name: str, symbol: str, unit_name: str, unit_symbol: str, unit_plural: Optional[str]=None, base_symbol: Optional[str]=None):
        pass

    @overload
    def __init__(self, name: str, symbol: str, dimension: 'Dimension'):
        pass

    @overload
    def __init__(self, dimensions: Dict['Dimension', int]):
        pass


    def __init__(self,
                 arg_0 : Union[str, Dict['Dimension', int]],
                 arg_1 : str=None,
                 arg_2 : Union[str, 'Dimension']=None,
                 arg_3 : str=None,
                 arg_4 : str=None,
                 arg_5 : str=None):
        
        self._name = None
        self._symbol = None
        self._components = None
        self._coherent_unit = None
        self._additional_units = []

        if isinstance(arg_0, str) and isinstance(arg_1, str):
            self._name = arg_0
            self._symbol = arg_1

            if (isinstance(arg_2, str) and
                    isinstance(arg_3, str) and
                    isinstance(arg_4, (str, type(None))) and
                    isinstance(arg_5, (str, type(None)))):

                self._coherent_unit = Unit(arg_2, arg_3, plural=arg_4)
            
            elif (isinstance(arg_2, Dimension) and
                    isinstance(arg_3, type(None)) and
                    isinstance(arg_4, type(None)) and
                    isinstance(arg_5, type(None))):
                
                self._components = arg_2.components
            
            else:
                raise Exception()
            
        elif (isinstance(arg_0, dict) and
                isinstance(arg_2, type(None)) and
                isinstance(arg_3, type(None)) and
                isinstance(arg_4, type(None)) and
                isinstance(arg_5, type(None))):
            
            self._components = arg_0
        
        else:
            raise Exception()
        

    @property
    def is_named(self):
        return not self._name is None
    
    @property
    def is_atomic(self):
        return self._components is None
        
    
    @property
    def name(self):
        if self.is_named:
            return self._name
        
        if self.is_atomic:
            return None
        
        return self.base_name
    
    @property
    def symbol(self):
        if self.is_named:
            return self._symbol
        
        if self.is_atomic:
            return None
        
        return self.base_symbol

    @property
    def base_name(self):
        return self._get_base_attr("_name")
    
    @property
    def base_symbol(self):
        return self._get_base_attr("_symbol")
    

    @property
    def base_unit_symbol(self):
        units = {k._coherent_unit: v for k, v in self.base_components.items()}
        generator = UnitTextGenerator(units)
        return generator.generate_symbol()
    
    @property
    def base_unit_name(self):
        units = {k._coherent_unit: v for k, v in self.base_components.items()}
        generator = UnitTextGenerator(units)
        return generator.generate_name()
    
    @property
    def components(self):
        if self._components is None:
            return {self: 1}
        
        return self._components
    

    def _get_base_attr(self, attr):
        def get_attr(dim, pow, attr):
            value = getattr(dim, attr)

            if pow == 1:
                return value
            return value + str(pow)
        
        bases = self.base_components
        text = " ".join([get_attr(dim, pow, attr) for dim, pow in bases.items()])
        return Interpret.powerify(text)
    
    


    @property
    def base_components(self):
        """
        Example
        -------
        >>> Mass = Dimension("mass", "M", "gram", "g", "kg")
        Dimension:
         - Name: mass,
         - Symbol: M,
         - Units: kilogram(s) [kg],
         - Base Units: kilogram(s) [kg],
         - Derivations:
             - kilogram(s) [kg],
         - Additional Units:
             - gram(s) [g],
             - tonne(s) [t],
             - milligram(s) [mg],
            ...

        >>> Time = Dimension("time", "T", "second", "s")
        Dimension:
         - Name: time,
         - Symbol: T,
         - Units: second(s) [s],
         - Base Units: second(s) [s],
         - Derivations:
             - second(s) [s],
         - Additional Units:
             - hour(s) [h],
             - millisecond(s) [ms],
             - nanosecond(s) [ns],
            ...

        >>> Length = Dimension("length", "L", "metre", "m")
        Dimension:
         - Name: length,
         - Symbol: L,
         - Units: metre(s) [m],
         - Base Units: metre(s) [m],
         - Derivations:
             - metre(s) [m],
         - Additional Units:
             - kilometre(s) [km],
             - foot/feet [ft],
             - mile(s) [mi],
            ...

        >>> Velocity = Dimension("velocity", "v", Length/Time)
        Dimension:
         - Name: velocity,
         - Symbol: v,
         - Units: metre(s) per second [m s-1],
         - Base Units: metre(s) per second [m s-1],
         - Derivations:
             - metre(s) per second [m s-1],
         - Additional Units:
             - kilometre(s) per second [km s-1],
             - foot/feet per hour [ft h-1],
             - mile(s) per nanosecond [mi ns-1],
            ...

        >>> Acceleration = Dimension("acceleration", "a", Velocity/Time)
        Dimension:
         - Name: acceleration,
         - Symbol: a,
         - Units: metre(s) per second squared [m s-2],
         - Base Units: metre(s) per second squared [m s-2],
         - Derivations:
             - metre(s) per second squared [m s-2],
         - Additional Units:
             - kilometre(s) per second squared [km s-2],
             - foot/feet per hour per minute [ft h-1 min-1],
             - mile(s) per nanosecond squared [mi ns-2],
            ...


        >>> Force = Dimension("force", "F", "newton", "N", Mass*Acceleration)
        Dimension:
         - Name: force,
         - Symbol: F,
         - Units: newton(s) [N],
         - Base Units: kilogram-metre(s) per second squared [kg m s-2],
         - Derivations:
             - newton(s) [N],
             - kilogram-metre(s) per second squared [kg m s-2],
         - Additional Units:
            ...

        >>> Area = Dimension("area", "\x1B[3mA\x1B[0m", Length**2)
        Dimension:
         - Name: area,
         - Symbol: \x1B[3mA\x1B[0m,
         - Units: square metre(s) [m^2],
         - Base Units: square metres [m^2],
         - Derivations:
             - square metres [m^2],
         - Additional Units:
            ...

        >>> Pressure = Dimension("pressure", "\x1B[3mP\x1B[0m", "pascal", "Pa", Force/Area)
        Dimension:
         - Name: pressure,
         - Symbol: \x1B[3mP\x1B[0m,
         - Units: newton(s) per metre squared [N m^-2],
         - Base Units: kilogram(s) per meter per second squared [kg m^-1 s^-2]
         - Derivations:
             - newton(s) per metre squared [N m^-2],
             - kilogram(s) per metre per second squared [kg m^-1 s-2],
         - Additional Units:
            ...


        >>> Length.base_units
        # Length is atomic, so returns {Length.base_unit : 1}
        {
            Unit(metre, m) : 1
        }

        >>> Time.base_units
        # Time is atomic, so returns {Time.base_unit : 1}
        {
            Unit(second, s) : 1
        }

        >>> Mass.base_units
        # Mass is atomic, so returns {Mass.base_unit : 1}
        {
            Unit(kilogram, kg) : 1
        }

        >>> Velocity.base_units
        # Velocity isn't atomic, so returns the combination of
        # dimension.base_units * power for each <dimension-power> pair
        # in Velocity._components.
        # Velocity._components = {Length : 1, Time: -1}, so this is
        # Length.base_units * 1 + Time.base_units * -1:
        # {
        #   Unit(metre, m) : 1
        # } * 1 + {
        #   Unit(second, s) : 1
        # } * -1
        # which is:
        # {
        #   Unit(metre, m) : 1
        # } + {
        #   Unit(second, s) : -1
        # }
        {
            Unit(metre, m) : 1,
            Unit(second, s) : -1,
        }

        >>> Acceleration.base_units
        # Acceleration isn't atomic, so returns the combination of
        # dimension.base_units * power for each <dimension-power> pair
        # in Acceleration._components.
        # Acceleration._components = {Velocity : 1, Time: -1}, so this
        # is Velocity.base_units * 1 + Time.base_units * -1 which is
        # {
        #   Unit(metre, m) : 1
        #   Unit(second, s) : -1
        # } * 1 + {
        #   Unit(second, s) : 1
        # } * -1
        # which is:
        # {
        #   Unit(metre, m) : 1
        #   Unit(second, s) : -1
        # } + {
        #   Unit(second, s) : -1
        # }
        {
            Unit(metre, m) : 1,
            Unit(second, s) : -2,
        }


        >>> Area.base_units
        # Area isn't atomic, so returns the combination of
        # dimension.base_units * power for each <dimension-power> pair
        # in Area._components.
        # Area._components = {Length : 2}, so this is
        # Length.base_units * 2:
        # {
        #   Unit(metre, m) : 1
        # } * 2
        # which is:
        # {
        #   Unit(metre, m) : 2
        # }
        {
            Unit(metre, m) : 2,
        }

        >>> Force.base_units
        # Force isn't atomic, so returns the combination of
        # dimension.base_units * power for each <dimension-power> pair
        # in Force._components.
        # Force._components = {Mass : 1, Acceleration: 1}, so this
        # is Mass.base_units * 1 + Acceleration.base_units * 1 which is
        # {
        #   Unit(kilogram, kg) : 1
        # } * 1 + {
        #   Unit(metre, m) : 1
        #   Unit(second, s) : -2
        # } * 1
        # which is:
        # {
        #   Unit(kilogram, kg) : 1
        # } + {
        #   Unit(metre, m) : 1
        #   Unit(second, s) : -2
        # }
        {
            Unit(kilogram, kg) : 1,
            Unit(metre, m) : 1,
            Unit(second, s) : -2,
        }


        >>> Pressure.base_units
        # Pressure isn't atomic, so returns the combination of
        # dimension.base_units * power for each <dimension-power> pair
        # in Pressure._components.
        # Pressure._components = {Force : 1, Area: -1}, so this
        # is Force.base_units * 1 + Area.base_units * -1 which is
        # {
        #   Unit(kilogram, kg) : 1,
        #   Unit(metre, m) : 1,
        #   Unit(second, s) : -2,
        # } * 1 + {
        #   Unit(metre, m) : 2
        # } * -1
        # which is:
        # {
        #   Unit(kilogram, kg) : 1,
        #   Unit(metre, m) : 1,
        #   Unit(second, s) : -2,
        # } + {
        #   Unit(metre, m) : -2
        # }
        {
            Unit(kilogram, kg) : 1,
            Unit(metre, m) : -1,
            Unit(second, s) : -2,
        }





        >>> Pressure.base_units
        {
            Force : 1,
            Area : -1,
        }

        >>> Force.base_units
        {
            Mass : 1,
            Acceleration : 1,
        }

        >>> Area._components
        {
            Length : 2,
        }

        >>> Acceleration._components
        {
            Velocity : 1,
            Time : -1,
        }

        >>> Velocity._components
        {
            Length : 1,
            Time : -1,
        }
        """

        if self.is_atomic:
            return {self : 1}

        
        dic = dict()
        for dim, pow in self._components.items():
            dic = Dimension.__combine_dicts(
                dic,
                {k: v*pow for k, v in dim.base_components.items()},
            )

        return dic
    

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




        
    def __str__(self):
        return self.name
    

    def __repr__(self):
        """
        Dimension:
         - Name: length,
         - Symbol: L,
         - Base Unit: meter(s) [m],
         - Additional Possible Units: kilometer(s) [km], centimeter(s) [cm], foot/feet (ft),
        """
        return f"{self.base_unit_name} [{self.base_unit_symbol}]"




Length = Dimension("length", "L", "meter", "m")
Time = Dimension("time", "T", "second", "s")
Mass = Dimension("mass", "M", "kilogram", "kg")

Velocity = Length / Time
Acceleration = Velocity / Time
Force = Mass * Acceleration
Area = Length**2
Pressure = Force / Area



print(Pressure.base_name)
print(Pressure.base_symbol)
print(Pressure.base_unit_name)
print(Pressure.base_unit_symbol)
print(repr(Pressure))







# print(Interperet.as_symbols({Length:1, Time:-1}))

