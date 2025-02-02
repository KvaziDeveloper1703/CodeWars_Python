"""
When you buy something, you're often asked whether your credit card number, phone number, or answer to a secret question is still correct.
To prevent someone from looking over your shoulder, these details are masked.

Your task is to write a function maskify that replaces all but the last four characters with #.

Examples:
"4556364607935616" → "############5616"
"64607935616" → "#######5616"
"1" → "1"
"" → ""

Обычно при покупке чего-либо вас спрашивают, актуальны ли ваши данные — номер кредитной карты, телефон или ответ на секретный вопрос.
Но, чтобы защитить личную информацию от посторонних глаз, эти данные замаскированы.

Ваша задача — написать функцию maskify, которая заменяет все символы, кроме последних четырёх, на #.

Примеры:
"4556364607935616" → "############5616"
"64607935616" → "#######5616"
"1" → "1"
"" → ""
"""

def maskify(cc):
    if len(cc) <= 4:
        return cc

    masked_part = "#" * (len(cc) - 4)
    visible_part = cc[-4:]
    return masked_part + visible_part

print(maskify("4556364607935616"))
print(maskify("64607935616"))
print(maskify("1"))
print(maskify(""))
print(maskify("123456"))