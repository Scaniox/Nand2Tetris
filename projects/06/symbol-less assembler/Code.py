comp_lookup_table = {   "0"     :   "0101010",
                        "1"     :   "0111111",
                        "-1"    :   "0111010",
                        "D"     :   "0001100",
                        "A"     :   "0110000",
                        "!D"    :   "0001101",
                        "!A"    :   "0110001",
                        "-D"    :   "0001111",
                        "-A"    :   "0110011",
                        "D+1"   :   "0011111",
                        "A+1"   :   "0110111",
                        "D-1"   :   "0001110",
                        "A-1"   :   "0110010",
                        "D+A"   :   "0000010",
                        "D-A"   :   "0010011",
                        "A-D"   :   "0000111",
                        "D&A"   :   "0000000",
                        "D|A"   :   "0010101",
                        "M"     :   "1110000",
                        "!M"    :   "1110001",
                        "-M"    :   "1110011",
                        "M+1"   :   "1110111",
                        "M-1"   :   "1110010",
                        "D+M"   :   "1000010",
                        "D-M"   :   "1010011",
                        "M-D"   :   "1000111",
                        "D&M"   :   "1000000",
                        "D|M"   :   "1010101"   }

jump_lookup_table = {   "null"  :   "000",
                        "JGT"   :   "001",
                        "JEQ"   :   "010",
                        "JGE"   :   "011",
                        "JLT"   :   "100",
                        "JNE"   :   "101",
                        "JLE"   :   "110",
                        "JMP"   :   "111"   }


def dest(mnemonic): # return (string of 3 bits) destination in binary encoding
    return f"{1 if 'A' in mnemonic else 0}{1 if 'D' in mnemonic else 0}{1 if 'M' in mnemonic else 0}"


def comp(mnemonic): # return (string of 7 bits) computation in binary encoding
    return comp_lookup_table[mnemonic]


def jump(mnemonic): # return (string of 3 bits) jump in binary encoding
    return jump_lookup_table[mnemonic]
