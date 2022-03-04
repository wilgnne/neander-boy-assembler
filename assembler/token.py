'''
    A token is a single unit of data that is passed to the assembler.
'''

class Token:
    '''
    Token class.

    Attributes:
        type (str): The type of the token.
        value (str): The value of the token.
    '''

    def __init__(self, type, value):
        '''
        Constructor.

        Args:
            type (str): The type of the token.
            value (str): The value of the token.
        '''
        self.type = type
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
