from typing import Union, Optional, overload, Dict
from numbers import Number

class AtomicUnits:
    def __init__(self, name: str, symbol: str):
        pass



class Dimension:
    def __init__(self, name):
        self._name = name




class BaseDimension(Dimension):
    def __init__(self, name: str, symbol: str, unit_name: str, unit_symbol: str):
        self._name = name
        self._symbol = symbol
        self._base_units = AtomicUnits(unit_name, unit_symbol)

    @property
    def name(self):
        return self._name
    
    @property
    def symbol(self):
        if hasattr(self, self._symbol):
            return self._symbol
        
    @property
    def base_units(self):
        return self._base_units



    def __repr__(self) -> str:
        return f"Base Dimension:\n - Name: {self._name}"
        # BaseDimension:
        # Name: length
        # Symbol: L
        # Base Units: meters (m)

        # DerivedDimension:
        # Name: velocity
        # Base Dimensions: length (L), time (T)
        # Symbol: L / T
        # Base Units: meters per second (m/s)







class DerivedDimension(Dimension):
    @overload
    def __init__(self, component_dimensions: Dict['Dimension', int]):
        pass






    @overload
    def __init__(self, name: str, component_dimensions: Dict['Dimension', int]):
        """_summary_

        _extended_summary_

        Parameters
        ----------
        name : str
            The name of the dimension.
        component_dimensions : Dict[&#39;Dimension&#39;, int]
            A set of Dimensions and their respective powers.

        Examples
        --------
        >>> DerivedDimension("velocity", {Length : 1, Time : -1})

        """
        pass


    @overload
    def __init__(self, name: str, dimension: 'DerivedDimension'):
        pass






    @overload
    def __init__(self, name: str, unit_name: str, unit_symbol: str, component_dimensions: Dict['Dimension', int]):
        pass


    @overload
    def __init__(self, name: str, unit_name: str, unit_symbol: str, dimension: 'DerivedDimension'):
        pass



    


    def __init__(self):
        pass




if __name__ == "__main__":
    length = BaseDimension("length", "L", "meter", "m")
    time = BaseDimension("time", "T", "second", "s")
    mass = BaseDimension("mass", "M", "gram", "g")

    velocity = DerivedDimension("velocity", "" {length:1, time:-1})
    acceleration = length / time**2

    force = DerivedDimension("force", "N", mass * length / time**2)
