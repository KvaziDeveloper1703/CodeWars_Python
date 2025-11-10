'''
You need to write a Morse code decoder for a wired electrical telegraph.

The telegraph works with two wires:
- When the key is pressed → record 1;
- When the key is released → record 0.

Thus, the received message is represented as a binary string consisting of 0s and 1s.

Morse Timing Rules:
- Dot (.) - 1 time unit;
- Dash (-) - 3 time units;
- Pause between dots/dashes - 1 time unit;
- Pause between letters - 3 time units;
- Pause between words - 7 time units.

Implement two functions:
1. decodeBits(bits):
- Takes a binary string of 0s and 1s.
- Detects the time unit and converts it to Morse symbols:
    - . → dot;
    - - → dash;
    - ' ' → space between letters;
    - ' ' → space between words.
- Ignore leading and trailing zeros.

2. decodeMorse(morseCode):
- Takes the output of decodeBits;
- Returns a human-readable decoded text.

Тебе нужно написать декодер азбуки Морзе для проводного электрического телеграфа.

Телеграф работает с двумя проводами:
- Когда ключ нажат → записывается 1;
- Когда ключ отпущен → записывается 0.

Таким образом, полученное сообщение представлено в виде двоичной строки, состоящей из 0 и 1.

Правила временных интервалов Морзе:
- Точка (.) — 1 единица времени;
- Тире (-) — 3 единицы времени;
- Пауза между точками и тире — 1 единица времени;
- Пауза между буквами — 3 единицы времени;
- Пауза между словами — 7 единиц времени.

Реализуй две функции:
1. decodeBits(bits):
- Принимает двоичную строку из 0 и 1;
- Определяет длительность одной временной единицы и преобразует строку в символы Морзе:
    - . → точка;
    - - → тире;
    - ' ' → пробел между буквами;
    - ' ' → пробел между словами.
- Игнорирует лишние нули в начале и конце строки.

2. decodeMorse(morseCode):
- Принимает результат работы decodeBits;
- Возвращает человеко-читаемый текст.
'''

MORSE_CODE = {
    '.-': 'A',
    '-...': 'B',
    '-.-.': 'C',
    '-..': 'D',
    '.': 'E',
    '..-.': 'F',
    '--.': 'G',
    '....': 'H',
    '..': 'I',
    '.---': 'J',
    '-.-': 'K',
    '.-..': 'L',
    '--': 'M',
    '-.': 'N',
    '---': 'O',
    '.--.': 'P',
    '--.-': 'Q',
    '.-.': 'R',
    '...': 'S',
    '-': 'T',
    '..-': 'U',
    '...-': 'V',
    '.--': 'W',
    '-..-': 'X',
    '-.--': 'Y',
    '--..': 'Z',

    '-----': '0',
    '.----': '1',
    '..---': '2',
    '...--': '3',
    '....-': '4',
    '.....': '5',
    '-....': '6',
    '--...': '7',
    '---..': '8',
    '----.': '9',

    '.-.-.-': '.',
    '--..--': ',',
    '..--..': '?',
    '.----.': "'",
    '-.-.--': '!',
    '-..-.': '/',
    '-.--.': '(',
    '-.--.-': ')',
    '.-...': '&',
    '---...': ':',
    '-.-.-.': ';',
    '-...-': '=',
    '.-.-.': '+',
    '-....-': '-',
    '..--.-': '_',
    '.-..-.': '"',
    '...-..-': '$',
    '.--.-.': '@',

    '...---...': 'SOS'
}

from itertools import groupby

def decode_bits(bits):
    bits = bits.strip('0')

    groups = []
    for key, group in groupby(bits):
        group_string = ''.join(group)
        groups.append(group_string)

    lengths = [len(g) for g in groups]
    unit = min(lengths)

    bits = bits.replace('111' * unit, '-')
    bits = bits.replace('0000000' * unit, '   ')
    bits = bits.replace('000' * unit, ' ')
    bits = bits.replace('1' * unit, '.')
    bits = bits.replace('0' * unit, '')

    return bits

def decode_morse(morse_code):
    words = morse_code.strip().split('   ')
    decoded_words = []

    for word in words:
        letters = word.split(' ')
        decoded_letters = [MORSE_CODE.get(letter, '') for letter in letters]
        decoded_words.append(''.join(decoded_letters))

    return ' '.join(decoded_words)