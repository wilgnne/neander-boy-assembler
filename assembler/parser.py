'''
    A parser definition
'''

from assembler.node import Node

def populate_symbol_table(node: Node, simbol_table: dict):
    '''
    Populate the symbol table.
    '''
    if node.value.type == 'LABEL':
        simbol_table[node.value.value] = None
    for child in node.children:
        populate_symbol_table(child, simbol_table)

    return simbol_table

DECODER = {
    'NOP': 0b0000_0000,
    'STA': 0b0000_0001,
    'LDA': 0b0000_0010,
    'ADD': 0b0000_0011,
    'OR' : 0b0000_0100,
    'AND': 0b0000_0101,
    'NOT': 0b0000_0110,
    'SUB': 0b0000_0111,
    'JMP': 0b0000_1000,
    'JN': 0b0000_1001,
    'JZ': 0b0000_1010,
    'JNZ': 0b0000_1011,
    'LDI': 0b0000_1110,
    'HLT': 0b0000_1111,
}

def parser(node: Node, simbol_table: dict = None, mem = None):
    '''
    Parser.
    '''
    if simbol_table is None:
        simbol_table = {}
        simbol_table = populate_symbol_table(node, simbol_table)

    if mem is None:
        mem = []
        if 'main' in simbol_table.keys():
            mem.append(DECODER['JMP'])
            mem.append(None)

    if node.value.type == 'DATA':
        for child in node.children:
            if child.value.type == 'LABEL':
                mem.append(child.children[0].value.value)
                simbol_table[child.value.value] = len(mem) - 1
    elif node.value.type == 'LABEL':
        if simbol_table[node.value.value] is None:
            simbol_table[node.value.value] = len(mem)
    elif node.value.type == 'UPCODE':
        upcode = DECODER[node.value.value]
        mem.append(upcode)

        for child in node.children:
            if child.value.type == 'LABEL':
                mem.append(simbol_table[child.value.value])
            elif child.value.type == 'IMEDIATE':
                mem.append(child.value.value)

    for child in node.children:
        parser(child, simbol_table, mem)

    if 'main' in simbol_table.keys():
        mem[1] = simbol_table['main']

    return simbol_table, mem
