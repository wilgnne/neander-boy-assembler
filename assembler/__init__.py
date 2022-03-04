'''
    __init__.py
'''

from assembler.lexer import lexer
from assembler.parser import parser
from assembler.preprocess import sanitize


def compile_source(source: str, debuger=False) -> bytearray:
    """
    Compiles the source code into a byte array.
    :param source: The source code to be compiled.
    :param debuger: Whether or not to print debug information.
    :return: The byte array of the compiled code.
    """
    # Preprocess the source code.
    source = sanitize(source)

    # Lex the source code.
    tokens = lexer(source)

    if debuger:
        print('TOKENS:', tokens, '\n')

    # Parse the source code.
    ast, simbol_table = parser(tokens)

    if debuger:
        print('SIMBOL TABLE:', simbol_table, '\n')
        ast.print_tree()

    # Compile the source code.
    return bytearray(ast.compile(simbol_table, debuger))
