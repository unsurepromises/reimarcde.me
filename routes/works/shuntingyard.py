import re
from flask import Blueprint, render_template, request

shuntingyard_bp = Blueprint('shuntingyard', __name__)
shunting_yard_bp = shuntingyard_bp


class ShuntingYard:
    def precedence(self, operator):
        if operator in ('+', '-'):
            return 1
        elif operator in ('*', '/'):
            return 2
        elif operator == '^':
            return 3
        return 0

    def tokenize(self, expr: str):
        if not expr or not expr.strip():
            raise ValueError("Expression is empty.")

        illegal = re.findall(r'[^a-zA-Z0-9+\-*/^().\s]', expr)
        if illegal:
            raise ValueError(f"Invalid character(s): {' '.join(sorted(set(illegal)))}")

        raw_tokens = re.findall(r'\d*\.?\d+|[a-zA-Z_]\w*|[+\-*/^()]', expr)
        raw_tokens = [t for t in raw_tokens if t]
        if not raw_tokens:
            raise ValueError("Expression is empty.")

        # Insert implicit '*' tokens
        tokens = []
        for i, token in enumerate(raw_tokens):
            if i > 0:
                prev = raw_tokens[i - 1]
                prev_is_operand = bool(re.match(r'^\d*\.?\d+$|^[a-zA-Z_]\w*$', prev))
                curr_is_operand = bool(re.match(r'^\d*\.?\d+$|^[a-zA-Z_]\w*$', token))

                if (prev_is_operand and token == '(') or \
                   (prev == ')' and token == '(') or \
                   (prev == ')' and curr_is_operand):
                    tokens.append('*')

            tokens.append(token)

        open_brackets = 0
        for token in tokens:
            if token == '(':
                open_brackets += 1
            elif token == ')':
                open_brackets -= 1
                if open_brackets < 0:
                    raise ValueError("Mismatched parentheses in expression.")
        if open_brackets != 0:
            raise ValueError("Mismatched parentheses in expression.")

        return tokens

    def shunting_yard(self, tokens):
        output_queue = []
        operator_stack = []

        for token in tokens:
            if token not in ('+', '-', '*', '/', '^', '(', ')'):
                output_queue.append(token)
            elif token == '(':
                operator_stack.append(token)
            elif token == ')':
                while operator_stack and operator_stack[-1] != '(':
                    output_queue.append(operator_stack.pop())
                if not operator_stack:
                    raise ValueError("Mismatched parentheses in expression.")
                operator_stack.pop()
            else:
                while (operator_stack and operator_stack[-1] != '(' and (
                    self.precedence(operator_stack[-1]) > self.precedence(token) or
                    (self.precedence(operator_stack[-1]) == self.precedence(token) and token != '^')
                )):
                    output_queue.append(operator_stack.pop())
                operator_stack.append(token)

        while operator_stack:
            op = operator_stack.pop()
            if op in ('(', ')'):
                raise ValueError("Mismatched parentheses in expression.")
            output_queue.append(op)

        return output_queue

    def convert(self, expression: str) -> str:
        tokens = self.tokenize(expression)
        postfix_tokens = self.shunting_yard(tokens)
        return ' '.join(postfix_tokens)


@shuntingyard_bp.route('/works/shunting-yard', methods=['GET', 'POST'])
@shuntingyard_bp.route('/shunting-yard', methods=['GET', 'POST'])
def shunting_yard_view():
    result = None
    error = None
    expression = ''

    if request.method == 'POST':
        expression = request.form.get('expression') or request.form.get('inputString') or request.form.get('expr') or ''
        expression = expression.strip()
        if not expression:
            error = "Please enter an infix expression."
        else:
            try:
                converter = ShuntingYard()
                result = converter.convert(expression)
            except ValueError as e:
                error = str(e)

    return render_template(
        'shuntingyard.html',
        expression=expression,
        result=result,
        error=error,
        message=error
    )
