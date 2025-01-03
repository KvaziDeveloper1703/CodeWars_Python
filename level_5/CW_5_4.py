"""
Complete the rgb function to convert RGB decimal values into their hexadecimal representation.

Examples:
Input: rgb(255, 255, 255) → Output: "FFFFFF"
Input: rgb(255, 255, 300) → Output: "FFFFFF" (300 is clamped to 255)
Input: rgb(0, 0, 0) → Output: "000000"
Input: rgb(148, 0, 211) → Output: "9400D3"

Доработайте функцию rgb, чтобы она преобразовывала значения RGB в шестнадцатеричное представление.

Примеры:
Ввод: rgb(255, 255, 255) → Вывод: "FFFFFF"
Ввод: rgb(255, 255, 300) → Вывод: "FFFFFF" (300 округляется до 255)
Ввод: rgb(0, 0, 0) → Вывод: "000000"
Ввод: rgb(148, 0, 211) → Вывод: "9400D3"

https://www.codewars.com/kata/513e08acc600c94f01000001
"""

def rgb(r, g, b):
    def clamp_and_convert(value):
        value = max(0, min(255, value))
        hex_value = hex(value)[2:]
        if len(hex_value) == 1:
            hex_value = '0' + hex_value
        return hex_value.upper()

    return clamp_and_convert(r) + clamp_and_convert(g) + clamp_and_convert(b)

print(rgb(255, 255, 255))