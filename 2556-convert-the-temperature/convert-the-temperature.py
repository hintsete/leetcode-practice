class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kelvin=273.15+celsius
        fahrenheit=9/5*(celsius)+32
        return(kelvin,fahrenheit)
        