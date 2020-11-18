import Parser, Code, SymbolTable

# read assembly file
assembly_file = open("Pong.asm", "r")
assembly_file_lines_list = assembly_file.readlines()
assembly_file.close()

# output file
output_file = open("Pong.hack", "w")
output_file.truncate(0) # clear output file

#first pass: get label symbols
current_memory_location = 0 # keep track of ROM locations
Parser.initialise(assembly_file_lines_list)
while True :

    if Parser.commandType() == "L_COMMAND" :
        label = Parser.symbol()[:-1]
        SymbolTable.addEntry(label, current_memory_location)
    else :# increment current memory location as it is a translated command
        current_memory_location += 1


    # escape loop if there are no more commands
    if Parser.hasMoreCommands():
        Parser.advance()

    else:
        break


# second pass: generates the code and gets variable symbols
current_variable_location = 16 # keep track of RAM locations
Parser.initialise(assembly_file_lines_list)
while True :

    if Parser.commandType() == "A_COMMAND" : # if currently dealing with an A command

        symbol = Parser.symbol()

        if not(symbol[:1].isdigit()) :   #resolve variable
            if not(SymbolTable.contains(symbol)) : # it is a new variable
                SymbolTable.addEntry(symbol, current_variable_location)
                current_variable_location += 1

            # convert to integer address
            symbol = SymbolTable.GetAddress(symbol)

        binary_symbol = bin(int(symbol))
        string_binary_symbol = binary_symbol[2:].zfill(15)

        output_file.write(f"0{string_binary_symbol}\n")


    elif Parser.commandType() == "C_COMMAND" : # if currently dealing with a C command
        dest = Code.dest(Parser.dest())
        comp = Code.comp(Parser.comp())
        jump = Code.jump(Parser.jump())

        output_file.write(f"111{comp}{dest}{jump}\n")

    # escape loop if there are no more commands
    if Parser.hasMoreCommands():
        Parser.advance()

    else:
        break


output_file.close()
