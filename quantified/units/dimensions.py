


from quantified import Dimension


## Base dimensions:
Time = Dimension("time", "T")
Length = Dimension("length", "L")
Mass = Dimension("mass", "M")
Current = Dimension("current", "I")
Temperature = Dimension("temperature", "\u03F4")
ChemicalAmount = Dimension("chemical amount", "N")
LuminousIntensity = Dimension("luminous intensity", "J")

## Derived dimensions:
Frequency = Time**-1
