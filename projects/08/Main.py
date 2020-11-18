# main coordinating controlling file
import Parser, CodeWriter, os, sys
from pathlib import Path

command_writing_table = {   "C_ARITHMETIC"  :   "CodeWriter.writeArithmetic(Parser.arg1())",
                            "C_PUSH"        :   "CodeWriter.WritePushPop(command_type, Parser.arg1(), Parser.arg2())",
                            "C_POP"         :   "CodeWriter.WritePushPop(command_type, Parser.arg1(), Parser.arg2())",
                            "C_LABEL"       :   "CodeWriter.writeLabel(Parser.arg1())",
                            "C_GOTO"        :   "CodeWriter.writeGoto(Parser.arg1())",
                            "C_IF"          :   "CodeWriter.writeIf(Parser.arg1())",
                            "C_FUNCTION"    :   "CodeWriter.writeFunction(Parser.arg1(), Parser.arg2())",
                            "C_CALL"        :   "CodeWriter.writeCall(Parser.arg1(),Parser.arg2())",
                            "C_RETURN"      :   "CodeWriter.writeReturn()"}

# input file/ files
input_directory = Path(sys.argv[1])#input("input virtual machine program: "))
if input_directory.is_dir():
    files_to_process = input_directory.iterdir()
    output_file = open(input_directory / f"{input_directory.stem}.asm", "w")

else:
    files_to_process = [input_directory]
    output_file = open(input_directory.parent / f"{input_directory.stem}.asm", "w")

# detect if it has a Sys file in input_directory:
call_sys = False
for file in input_directory.iterdir():
    if file.stem == "Sys":
        call_sys = True

# initialse codewriter
CodeWriter.initialise(output_file)
CodeWriter.writeInit(call_sys)

for input_file in files_to_process:

    if input_file.suffix == ".vm": # only process .vm files

        # initalise parser for this file
        Parser.initialise(input_file)

        # initialise codewriter for this file
        CodeWriter.setFileName(input_file.stem)

        #main loop
        while Parser.hasMoreCommands():
            Parser.advance() # set up current command

            command_type = Parser.commandType() # find what kind of command this is
            #print(f"command type: {command_type}\narg1: {Parser.arg1()}\narg2: {Parser.arg2()}")

            exec(command_writing_table[command_type]) # run the correct CodeWriter function

CodeWriter.close()
