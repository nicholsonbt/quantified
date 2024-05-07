from typing import Union, Dict, overload

from quantified.utils.baseunit import BaseUnit



class Units:
    def __init__(self, components: Dict[BaseUnit, int]):
        self._components = components

    @property
    def components(self):
        return self._components