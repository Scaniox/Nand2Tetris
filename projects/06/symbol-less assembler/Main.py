import Parser, Code

# initialse
assembly_file = open("MaxL.asm", "r")
Parser.initialise(assembly_file)

# output file
output_file = open("MaxL.hack", "w")
output_file.truncate(0)

while True :

    if Parser.commandType() == "A_COMMAND" : # if currently dealing with an A command
        string_binary_symbol = bin(int(Parser.symbol()))[2:].zfill(15)
        output_file.write(f"0{string_binary_symbol}\n")

    elif Parser.commandType() == "C_COMMAND" : # if currently dealing with a C command
        dest = Code.dest(Parser.dest())
        comp = Code.comp(Parser.comp())
        jump = Code.jump(Parser.jump())

        output_file.write(f"111{comp}{dest}{jump}\n")

    if Parser.hasMoreCommands():
        Parser.advance()

    else:
        break


assembly_file.close()
output_file.close()
