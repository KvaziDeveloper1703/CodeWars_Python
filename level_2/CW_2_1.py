'''
Given a mathematical expression as a string, return its numerical result.

Rules:
    - Numbers can be integers or decimals;
    - Supported operators: +, -, *, /;
        - * and / have higher precedence than + and -;
        - Operations with the same precedence are evaluated left-to-right.
    - Parentheses () may be nested to any depth;
    - Whitespace may appear anywhere or be absent;
    - A minus sign used for negation (-) is never separated by spaces.

Дано математическое выражение в виде строки. Нужно вернуть результат вычисления в виде числа.

Правила:
    - Числа могут быть целыми или десятичными;
    - Поддерживаемые операторы: +, -, *, /;
        - * и / выполняются раньше, чем + и -;
        - При равном приоритете — слева направо.
    - Скобки () могут быть вложенными;
    - Пробелы допускаются в любом месте;
    - Знак минус (-) для отрицания не отделяется пробелами.
'''

def calc(expression):
    expression = expression.replace(' ', '')

    def parse_expression(inner_expression):
        tokens = []
        current_number = ''
        position = 0

        while position < len(inner_expression):
            symbol = inner_expression[position]

            if symbol.isdigit() or symbol == '.':
                current_number += symbol

            elif symbol in '+-*/':
                if current_number != '' and current_number != '-':
                    tokens.append(float(current_number))
                    current_number = ''
                if symbol == '-' and (position == 0 or inner_expression[position - 1] in '+-*/('):
                    current_number = '-'
                else:
                    tokens.append(symbol)

            elif symbol == '(':
                nesting_depth = 1
                closing_position = position + 1
                while closing_position < len(inner_expression):
                    if inner_expression[closing_position] == '(':
                        nesting_depth += 1
                    elif inner_expression[closing_position] == ')':
                        nesting_depth -= 1
                        if nesting_depth == 0:
                            break
                    closing_position += 1
                value_in_parentheses = parse_expression(inner_expression[position + 1:closing_position])
                if current_number == '-':
                    value_in_parentheses = -value_in_parentheses
                    current_number = ''
                tokens.append(value_in_parentheses)
                position = closing_position

            position += 1

        if current_number != '' and current_number != '-':
            tokens.append(float(current_number))

        index = 0
        while index < len(tokens):
            if tokens[index] == '*':
                result = tokens[index - 1] * tokens[index + 1]
                tokens[index - 1:index + 2] = [result]
                index -= 1
            elif tokens[index] == '/':
                result = tokens[index - 1] / tokens[index + 1]
                tokens[index - 1:index + 2] = [result]
                index -= 1
            else:
                index += 1

        index = 0
        while index < len(tokens):
            if tokens[index] == '+':
                result = tokens[index - 1] + tokens[index + 1]
                tokens[index - 1:index + 2] = [result]
                index -= 1
            elif tokens[index] == '-':
                result = tokens[index - 1] - tokens[index + 1]
                tokens[index - 1:index + 2] = [result]
                index -= 1
            else:
                index += 1

        return tokens[0]

    return parse_expression(expression)