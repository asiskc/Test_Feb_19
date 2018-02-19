'''Q4. Create a Temperature class. Make two methods :
      a. convertFahrenheit - It will take Celsius and will print it into Fahrenheit.
      b. convertCelsius - It will take Fahrenheit and will convert it into Celsius.
'''

class Temperature:
    def covertFahrenheit(celsius):
        return (celsius*(9/5))+32

    def convertcelsius(fahrenheit):
        return (fahrenheit-32)*(5/9)


s= Temperature
print(s.convertcelsius(45))
print(s.covertFahrenheit(35))