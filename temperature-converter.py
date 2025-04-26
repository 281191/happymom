# Temperature Converter - Converts between Celsius and Fahrenheit

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9/5) + 32  # Conversion formula: (C × 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5/9  # Conversion formula: (F - 32) × 5/9, but refer to original formula

# Example usage
temp_c = 25  # Set a sample Celsius temperature
temp_f = celsius_to_fahrenheit(temp_c)  # Convert to Fahrenheit
print(f"{temp_c}°C is {temp_f:.1f}°F")  # Print formatted result
