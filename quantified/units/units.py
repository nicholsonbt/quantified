from typing import Union, Optional, overload, Dict
from numbers import Number

class Conversion:
    pass


"""
Atomic: Named:  Coherent:	Code:	    Description:	                        Examples:
T	    T	    T	        BASE	    One of the 7 base units.	            Meter, second, mole, etc.
T	    T	    F	        CONV	    A conversion unit from a base unit.	    Hour, mile, millimole, etc.
T	    F	    T	        N/A	        N/A	                                    Atomic must be named.
T	    F	    F	        N/A	        N/A	                                    //
F	    T	    T	        DER1	    Named coherent, but not base.	        Newton, joule, watt, etc.
F	    T	    F	        CONV_DER1	A conversion unit from some DER1 unit.	Kilowatt, microjoule, etc.
F	    F	    T	        DER2	    Unnamed coherent.	                    Meters-per-second, etc.
F	    F	    F	        CONV_DER2	A conversion unit from some unit.	    Kmph, etc.
"""




class Units:
    """_summary_
        Initialises a unit that is: atomic, base and coherent.

        Parameters
        ----------
        name : str
            The name of the atomic unit.
        symbol : str
            The symbol of the atomic unit.
        plural : Optional[str], optional
            The plural name of the atomic unit, by default None.

        Examples
        --------
        >>>Units("meter", "m")
        Units:
            - Atomic: True,
            - Named: True,
            - Coherent: True,
            - Name: meter(s),
            - Symbol: m

        >>>Units("foot", "ft", plural="feet")
        Units:
            - Atomic: True,
            - Named: True,
            - Coherent: False,
            - Name: foot / feet,
            - Symbol: ft

        >>>Units("lux", "lx", plural="lux")
        Units:
            - Atomic: False,
            - Named: True,
            - Coherent: True,
            - Name: lux,
            - Symbol: lx (cd sr m^-2)

        Notes
        -----
        Base:
            - Definition:  The unit is one of the 7 base units.
            - Examples:    Second, meter, kilogram, ampere, kelvin, mole,
                        and candela.
            - Antonym:     A derived unit.

        Derived:
            - Definition:  The unit isn't one of the 7 base units.
            - Examples:    Hour, gram, newton, meters-per-second, etc.
            - Antonym:     A base unit.


        Atomic:
            - Definition:  The units dimension is a base dimension, meaning
                        it can't be split further.
            - Examples:    Meter, foot, second, day, tonne, etc.
            - Antonym:     A composite unit.

        Composite:
            - Definition:  The unit dimension is derived from other
                        dimensions.
            - Examples:    Newton (kg⋅m/s²), joule (kg⋅m²/s²), watt
                        (kg⋅m²/s³), etc.
            - Antonym:     An atomic unit.

            
        Named:
            - Definition:  The unit has a name. This is true for all
                        atomic units, and true for some derived units.
            - Examples:    Joule, meter, newton, kilowatt, etc.
            - Antonym:     An unnamed unit.

        Unnamed:
            - Definition:  The unit doens't have a name. This can only be
                        true for derived units, where the name is the
                        composite of the names of its derived units.
            - Examples:    Meter-per-second (m/s), newton-meter (N⋅m),
                        etc.
            - Antonym:     A named unit.


        Coherent:
            - Definition:  The unit can be represented by base units
                        without a numerical conversion.
            - Examples:    Meter (m), second (s), newton (kg⋅m/s²), etc.
                        etc.
            - Antonym:     An incoherent unit.

        Incoherent:
            - Definition:  The unit can't be represented by base units
                        without a numerical conversion.
            - Examples:    Kilometer (1000 m), hour (3600 s),
                        miles-per-hour (0.44704 m/s), etc.
            - Antonym:     A coherent unit.


        All base units are atomic, named and coherent.
        Any unit that isn't all three can't be a base unit.

    """


    @overload
    def __init__(self, name: str, symbol: str):
        ## BASE
        pass

    # @overload
    # def __init__(self, name: str, symbol: str, plural: str):
    #     ## BASE
    #     pass

    # @overload
    # def __init__(self, name: str, symbol: str, base: 'Units'):
    #     ## CONV
    #     pass

    # @overload
    # def __init__(self, name: str, symbol: str, base: 'Units', conversion: 'Conversion', plural: str):
    #     ## CONV, CONV_DER1
    #     pass

    # @overload
    # def __init__(self, name: str, symbol: str, composite: Dict['Units', int]):
    #     # DER1
    #     pass

    # @overload
    # def __init__(self, name: str, symbol: str, composite: Dict['Units', int], plural: str):
    #     # DER1
    #     pass

    # @overload
    # def __init__(self, name: str, symbol: str, composite: Dict['Units', int]):
    #     # DER1
    #     pass



#     def __init__(self, name, plural=None):
#         self._name = name
#         self._plural = plural

#     @property
#     def singular_name(self):
#         return self._name
    
#     @property
#     def plural_name(self):
#         if self._plural is None:
#             return self._name + "s"
        
#         return self._plural
    
#     @property
#     def name(self):
#         if self._plural is None:
#             return self._name + "(s)"
        
#         if self._name == self._plural:
#             return self._name
        
#         return f"{self._name} / {self._plural}"


# class AtomicUnits(Units):
#     def __init__(self, name, symbol, plural=None):
#         Units.__init__(self, name, plural=plural)
#         self._symbol = symbol


#     def __repr__(self):
#         return "Atomic Units:\n - Type: {self.type},\n - Name: {self.name},\n - Symbol: {self.symbol},"
    
#     @property
#     def name(self):

def get_super(power):
    assert(isinstance(power, int))
    text = str(power)

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




class Dimension:
    @overload
    def __init__(self, name: str, symbol: str):
        pass

    @overload
    def __init__(self, name: str, symbol: str, components: Dict['Dimension', int]):
        pass

    @overload
    def __init__(self, name: str, symbol: str, units: 'Dimension'):
        pass

    @overload
    def __init__(self, components: Dict['Dimension', int]):
        pass


    def __init__(self, *args):
        self._name = None
        self._symbol = None
        self._components = None

        if len(args) == 1:
            self._components = args[0]
        
        elif len(args) == 2:
            self._name, self._symbol = args

        elif len(args) == 3:
            self._name, self._symbol, dic = args

            if isinstance(dic, Dimension):
                dic = dic.components

            self._components = dic
        
        else:
            raise Exception()
        
    
    @property
    def is_atomic(self):
        return self._components is None
    
    @property
    def is_named(self):
        return not self._name is None

    
    @property
    def components(self):
        if self._components is None:
            return {self: 1}
        
        return self._components
    
    @property
    def name(self):
        if self._name is None:
            return " ".join([Dimension.format(unit, power, "name") for unit, power in self.components.items()])
        
        return self._name

    
    @property
    def symbol(self):
        if self._symbol is None:
            return " ".join([Dimension.format(unit, power, "symbol") for unit, power in self.components.items()])

        return self._symbol
    

    @property
    def atom_symbols(self):
        if self._components is None:
            return self._symbol
        
        return " ".join([Dimension.format(unit, power, "symbol") for unit, power in self.components.items()])
    

    @property
    def atom_names(self):
        if self._components is None:
            return self._name
        
        return " ".join([Dimension.format(unit, power, "name") for unit, power in self.components.items()])
    


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
    

    @staticmethod
    def format(unit, power, attr):
        text = getattr(unit, attr)

        if power == 1:
            return text
        
        return text + get_super(power)
    

    def __str__(self):
        return self.name
    
    def __repr__(self):
        atoms = " ".join([Dimension.format(unit, power, "name") for unit, power in self.components.items()])

        return "Dimension:\n" \
            f" - Atomic: {self.is_atomic},\n" \
            f" - Named: {self.is_named},\n" \
            f" - Name: {self.name},\n" \
            f" - Symbol: {self.symbol},\n" \
            f" - Atoms: {atoms},"



time = Dimension("time", "T")
length = Dimension("length", "L")
velocity = Dimension("velocity", "v", length / time)

print(time)
print(repr(length))
print(repr(velocity))

