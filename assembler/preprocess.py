'''
    Preprocess the input file.
'''

import re

def sanitize(entry: str) -> str:
    '''
    Sanitize the input string.
    '''
    REMOVE_COMMENTS_REGEX = r"(?=;).*(?=$)"
    TRAILING_WHITE_SPACES_REGEX = r"(^[ |\t]+)|([ \t]+$)"

    NO_COMMENTS = re.sub(REMOVE_COMMENTS_REGEX, '', entry, 0, re.MULTILINE)
    NO_TRAILING_WHITE_SPACES = re.sub(
        TRAILING_WHITE_SPACES_REGEX, '', NO_COMMENTS, 0, re.MULTILINE)

    return NO_TRAILING_WHITE_SPACES
