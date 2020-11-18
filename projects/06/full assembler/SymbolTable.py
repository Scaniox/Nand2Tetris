
symbol_table = {"SP"    :   0,
                "LCL"   :   1,
                "ARG"   :   2,
                "THIS"  :   3,
                "THAT"  :   4,
                "SCREEN":   16384,
                "KBD"   :   24576}

#procedurally adding registers:
for register in range(16) :
    symbol_table[f"R{register}"] = register

def addEntry(symbol, address): # adds symbol address pair to symbol table
    symbol_table[symbol] = address

def contains(symbol): # returns (bool) if symbol table has symbol
    return symbol in symbol_table

def GetAddress(symbol): #returns (int) which address symbol is associated to
    return symbol_table[symbol]
