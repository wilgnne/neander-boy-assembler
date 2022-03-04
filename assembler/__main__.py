'''
    Entry point for the assembler.
'''

import argparse

from assembler import compile_source


def get_args():
    '''
    Get the arguments from the command line.
    '''

    # Create the parser
    my_parser = argparse.ArgumentParser(
        description='A simple assembler for the Neander-Boy architecture.')

    # Add the arguments
    my_parser.add_argument('input_file',
                           metavar='input_file',
                           type=str,
                           help='The assembly file to be assembled.')

    my_parser.add_argument('-o',
                           metavar='output_file',
                           type=str,
                           default='out.bin',
                           help='The output file to be generated.')

    my_parser.add_argument('-d',
                           action='store_true',
                           help='Active debuger.')

    return my_parser.parse_args()


def main(input_file: str, o: str, d: bool):
    '''
    Entry point for the assembler.
    '''

    with open(input_file, 'r', encoding='utf-8') as assembly_file:
        code = assembly_file.read()

    compiled_code = compile_source(code, debuger=d)

    with open(o, "wb") as out_file:
        out_file.write(compiled_code)


args = get_args()
main(**args.__dict__)
