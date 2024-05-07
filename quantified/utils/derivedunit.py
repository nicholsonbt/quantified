from typing import Union, Dict, overload

from quantified.utils.baseunit import BaseUnit


class DerivedUnit(BaseUnit):
    @overload
    def __init__(self, name: str, symbol: str, base_unit: BaseUnit, base_per_derived: float, plural: str=None):
        ...

    @overload
    def __init__(self, name: str, symbol: str, unit_components: Dict[BaseUnit, int], base_per_derived: float=1, plural: str=None):
        ...


    def __init__(self, name, symbol, arg_0, base_per_derived=1, *, plural=None):
        BaseUnit.__init__(self, name, symbol, plural=plural)

        if isinstance(arg_0, dict):
            self._components = arg_0
        
        elif issubclass(arg_0.__class__, BaseUnit):
            self._components = arg_0.components

        else:
            raise Exception()
        
        self._base_per_derived = base_per_derived




if __name__ == "__main__":
    m = BaseUnit("meter", "m")
    s = BaseUnit("second", "s")

    # ft = DerivedUnit("foot", "ft", m, 0.3048, plural="feet")

    # knot = DerivedUnit("knot", "knot", m/s, 0.514444)

    m**2

    # print(m.name)
    # print(ft.name)