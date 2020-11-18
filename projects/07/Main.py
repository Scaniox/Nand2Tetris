# main coordinating controlling file
import Parser, CodeWriter

# set up files
input_name = input("input virtual machine program: ")
input_file = open(input_name, "r")
output_file = open(f"{input_name[:-2]}asm", "w")

# initalise parser
Parser.initialise(input_file)
input_file.close()

# initialse codewriter
CodeWriter.initialise(output_file, input_name)

#main loop
while Parser.hasMoreCommands():
    Parser.advance() # set up current command

    command_type = Parser.commandType()

    if command_type == "C_ARITHMETIC": # write an arithmetic command
        CodeWriter.writeArithmetic(Parser.arg1())

    elif command_type in ["C_PUSH", "C_POP"]: # write push/pop command
        CodeWriter.WritePushPop(command_type, Parser.arg1(), Parser.arg2())

CodeWriter.close()
