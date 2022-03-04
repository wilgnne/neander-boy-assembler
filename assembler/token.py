'''
    A token is a single unit of data that is passed to the assembler.
'''
import enum


class TokenType(enum.Enum):
    '''
    Token types.
    '''
    SEGMENT = 1
    LABEL = 2
    WORD = 3
    ADDR = 4
    UPCODE = 5
    IMEDIATE = 6
    REFERENCE = 7


DATA_TYPES = [TokenType.WORD, TokenType.ADDR]
INITIALIZABLE_DATA_TYPES = [TokenType.WORD]

class Token:
    '''
    Token class.

    Attributes:
        type (str): The type of the token.
        value (str): The value of the token.
    '''

    def __init__(self, type_: TokenType, value: str):
        '''
        Constructor.

        Args:
            type (str): The type of the token.
            value (str): The value of the token.
        '''
        self.type = type_
        self.value = value

    def __str__(self):
        '''
        String representation of the token.

        Returns:
            str: The string representation of the token.
        '''
        return f'({self.type} {self.value})'

    def __repr__(self):
        '''
        String representation of the token.

        Returns:
            str: The string representation of the token.
        '''
        return self.__str__()
