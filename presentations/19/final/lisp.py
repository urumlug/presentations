# TOKENIZER

def tokenize(code):
    """
    Convert a string of code into a list of tokens.

    Args:
        code (str): The input LISP code as a string

    Returns:
        list: A list of token strings

    Example:
        tokenize("(+ 1 2)") -> ['(', '+', '1', '2', ')']
    """
    # Add spaces around parentheses so they become separate tokens
    # "(+ 1 2)" becomes " ( + 1 2 ) "
    code = code.replace('(', ' ( ')
    code = code.replace(')', ' ) ')

    # Split by whitespace and filter out empty strings
    tokens = code.split()

    return tokens


# PARSER

def parse(tokens):
    """
    Parse a list of tokens into an Abstract Syntax Tree (AST).

    Args:
        tokens (list): List of token strings

    Returns:
        The parsed expression (nested lists and atoms)

    Example:
        parse(['(', '+', '1', '2', ')']) -> ['+', 1, 2]
    """
    # Keep track of position using a list so we can modify it in nested functions
    position = [0]

    def peek():
        """Look at current token without consuming it"""
        return tokens[position[0]]

    def consume():
        """Get current token and move to next"""
        token = tokens[position[0]]
        position[0] += 1
        return token

    def parse_expression():
        """
        Parse a single expression (either an atom or a list).
        This is the main recursive function.
        """
        token = peek()

        if token == '(':
            return parse_list()
        else:
            return parse_atom(consume())

    def parse_list():
        """
        Parse a list expression.
        A list starts with '(' and ends with ')'.
        """
        consume()  # Skip the '('

        result = []

        # Keep parsing until we hit ')'
        while peek() != ')':
            result.append(parse_expression())

        consume()  # Skip the ')'

        return result

    def parse_atom(token):
        """
        Parse an atom (number or symbol).
        """
        # Try to convert to integer
        try:
            return int(token)
        except ValueError:
            # Try to convert to float
            try:
                return float(token)
            except ValueError:
                # It's a symbol
                return token

    # Start parsing from the first token
    return parse_expression()


# EVALUATOR

def eval_expression(expr):
    """
    Evaluate an expression.

    Args:
        expr: The expression to evaluate (from the AST)

    Returns:
        The result of evaluating the expression

    Example:
        eval_expression(['+', 1, 2]) -> 3
        eval_expression(['+', 1, ['*', 2, 3]]) -> 7
    """
    # Case 1: If it's a number, just return it
    if isinstance(expr, (int, float)):
        return expr

    # Case 2: If it's a list, evaluate it
    if isinstance(expr, list):
        # First element is the operator
        operator = expr[0]

        # Rest are operands
        operands = expr[1:]

        # Recursively evaluate all operands
        values = []
        for operand in operands:
            values.append(eval_expression(operand))

        # Apply the operator
        if operator == '+':
            return sum(values)

        elif operator == '-':
            if len(values) == 1:
                return -values[0]  # Unary minus
            result = values[0]
            for val in values[1:]:
                result -= val
            return result

        elif operator == '*':
            result = 1
            for val in values:
                result *= val
            return result

        elif operator == '/':
            result = values[0]
            for val in values[1:]:
                result /= val
            return result

        else:
            raise Exception(f"Unknown operator: {operator}")

    # If we get here, something went wrong
    raise Exception(f"Cannot evaluate: {expr}")


# REPL (Read-Eval-Print Loop)

def repl():
    """
    Run the Read-Eval-Print Loop.
    This allows interactive use of the interpreter.
    """
    print("=" * 50)
    print("Welcome to the LISP Interpreter!")
    print("=" * 50)
    print("Type LISP expressions and see the results.")
    print("Examples:")
    print("  (+ 1 2)")
    print("  (* 3 4)")
    print("  (+ 1 (* 2 3))")
    print("\nType 'exit' or 'quit' to leave.")
    print("=" * 50)
    print()

    while True:
        try:
            # Read: Get input from user
            user_input = input("lisp> ")

            # Check for exit commands
            if user_input.lower() in ['exit', 'quit']:
                print("Goodbye!")
                break

            # Skip empty input
            if not user_input.strip():
                continue

            # Tokenize: Convert string to tokens
            tokens = tokenize(user_input)
            print(f"Tokens: {tokens}")

            # Parse: Convert tokens to AST
            ast = parse(tokens)
            print(f"AST: {ast}")

            # Eval: Evaluate the AST
            result = eval_expression(ast)

            # Print: Show the result
            print(f"=> {result}")
            print()

        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")
            print()


# MAIN

if __name__ == "__main__":
    repl()
