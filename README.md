# Colors Python Library
### What is Colors?
Colors is library for adding different colors to the terminal of your script
### What is can Colors do?
Colors has 3 different types of terminal: basic, 8-bit, and true color (RGB)  
Basic color has black, red, green, yellow, blue, magenta, cyan and white.  
8-bit color is 256 different colors.  
True color is RGB having more than 16-million colors.

## Documentation
First import the module
```powershell
pip install Colors
```
or
```powershell
python -m pip install colors
```

To use basic color:
```python
import Colors

colored_text = Colors.ColorString("Example")
print(colored_text.green())  # Type in any color listed above
```

For 8-bit color:
```python
import Colors

colored_text = Colors.ColorString8Bit("Example")
print(colored_text.color(128)) # Or any number from 0-255
```

For true color:
```python
import Colors

colored_text = Colors.RGBString("Example")
print(colored_text.color(128, 128, 128)) # Choose any number from 0-255 for each channel
```
