from assembler.lexer import lexer
from assembler.parser import parser
from assembler.preprocess import sanitize


def compile_source(source: str) -> bytearray:
    '''
    Compile the source code into binary.
    '''

    # Sanitize the source code
    source = sanitize(source)

    # Lex the source code
    ast = lexer(source)

    # Parse the source code
    simbol_table, MEM = parser(ast.root)

    # Generate the binary code
    return bytearray(MEM)
