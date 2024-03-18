from cx_Freeze import setup, Executable

setup(
    name = "CurrencyConverter",
    version = "1.0",
    description = "Currency Converter",
    executables = [Executable("currencyConverter.py")]
    
)