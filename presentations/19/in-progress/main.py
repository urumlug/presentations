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
    # TODO: Implement the parser
    # Hint: You'll need helper functions for:
    # - Tracking position in the token list
    # - Parsing expressions (atoms or lists)
    # - Parsing lists (handling '(' and ')')
    # - Parsing atoms (converting strings to numbers or symbols)
    pass


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
    # TODO: Implement the evaluator
    # Hint: Consider these cases:
    # - If expr is a number, return it
    # - If expr is a list, evaluate the operator and operands
    # - Handle operators: +, -, *, /
    pass


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
