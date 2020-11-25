# modules
from pathlib import Path
import tokenizer

# statics
token_type_convert_table = {"KEYWORD"       :   "keyword",
                            "SYMBOL"        :   "symbol",
                            "IDENTIFIER"    :   "identifier",
                            "INT_CONST"     :   "integerConstant",
                            "STRING_CONST"  :   "stringConstant"}

# set up files
input_name = Path(input("input file name: "))
input_file = input_name.open()
output_file = open(input_name.stem + "T" + ".xml", "w")

#set up tokenizer
tokenizer.constructor(input_file)

output_file.write("<tokens>\n")

# go through each token processing it
while tokenizer.hasMoreTokens():
    tokenizer.advance()

    token_type = tokenizer.tokenType()
    # open type
    output_file.write(f"<{token_type_convert_table[token_type]}> ")
    # value
    if token_type == "KEYWORD":
        output_file.write(tokenizer.keyWord().lower())
    elif token_type == "SYMBOL":
        output_file.write(tokenizer.symbol())
    elif token_type == "IDENTIFIER":
        output_file.write(tokenizer.identifier())
    elif token_type == "INT_CONST":
        output_file.write(str(tokenizer.intVal()))
    elif token_type == "STRING_CONST":
        output_file.write(tokenizer.stringVal())
    # close type
    output_file.write(f" </{token_type_convert_table[token_type]}>\n")


output_file.write("</tokens>\n")

input_file.close()
output_file.close()
