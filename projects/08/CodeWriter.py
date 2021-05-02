# generates .asm code from the parsed commands

#code for each arithmetic operation
arithmetic_conversion_table = {

"add"   :
"""@SP // add
A=M-1
D=M
M=0
@SP
M=M-1
A=M-1
M=D+M
""",

"sub"   :
"""@SP // sub
A=M-1
D=M
M=0
@SP
M=M-1
A=M-1
M=M-D
""",

"neg"   :
"""@SP // neg
A=M-1
M=-M
""",

"eq"    :
"""@SP // eq
A=M-1
D=M
M=0
@SP
M=M-1
A=M-1
D=M-D
M=0
@FALSE{0}
D;JNE
@SP
A=M-1
M=1
(FALSE{0})
""",

"gt"    :
"""@SP // gt
A=M-1
D=M
M=0
@SP
M=M-1
A=M-1
D=M-D
M=0
@FALSE{0}
D;JLE
@SP
A=M-1
M=1
(FALSE{0})
""",

"lt"    :
"""@SP // lt
A=M-1
D=M
M=0
@SP
M=M-1
A=M-1
D=M-D
M=0
@FALSE{0}
D;JGE
@SP
A=M-1
M=1
(FALSE{0})
""",

"and"   :
"""@SP // and
A=M-1
D=M
M=0
@SP
M=M-1
A=M-1
M=D&M
""",

"or"    :
"""@SP // or
A=M-1
D=M
M=0
@SP
M=M-1
A=M-1
M=D|M
""",

"not"   :
"""@SP // not
A=M-1
M=!M
"""
}

# conversion table for segments and their truncations
segment_convert_table  = {  "local"     :   "LCL",
                            "argument"  :   "ARG",
                            "this"      :   "THIS",
                            "that"      :   "THAT"}


# variables used during execution
output_file = None
file_name = None
current_function = None
command_index = 0 # used to make arithmetic bool commands labels unique
return_address_counter = 0 # used to make return labels(assembly) after function calls unique

def initialise(output_file_): # initialse output file
    global output_file

    output_file = output_file_
    output_file.truncate(0)


def writeArithmetic(command): # write an arithemtic command to output_file
    global output_file, command_index

    output_file.write(arithmetic_conversion_table[command].format(command_index))
    command_index += 1 # used for lables to make them unique


def WritePushPop(command, segment, index): # perform stack manipulation operations
    global output_file, file_name

    if command == "C_PUSH":
        # load value into D
        if segment in ["local", "argument", "this", "that"]:
            output_file.write(f"@{segment_convert_table[segment]} // push {segment} {index}\nD=M\n@{index}\nA=D+A\nD=M\n")

        elif segment == "constant":
            output_file.write(f"@{index} // push {segment} {index}\nD=A\n")

        elif segment == "static":
            output_file.write(f"@{file_name}.{index} // push {segment} {index}\nD=M\n")

        elif segment == "temp":
            output_file.write(f"@{5+int(index)} // push {segment} {index}\nD=M\n")

        elif segment == "pointer":
            output_file.write(f"@{3+int(index)} // push {segment} {index}\nD=M\n")

        # store value onto stack
        output_file.write("@SP\nA=M\nM=D\n@SP\nM=M+1\n")

    elif command == "C_POP":
        # relative addressing required adding index to the base holding location to store that value, then subtracting the index again
        if segment in ["local", "argument", "this", "that"]:
            output_file.write(f"@{index} // pop {segment} {index}\nD=A\n@{segment_convert_table[segment]}\nM=D+M\n@SP\nA=M-1\nD=M\nM=0\n@{segment_convert_table[segment]}\nA=M\nM=D\n@SP\nM=M-1\n@{index}\nD=A\n@{segment_convert_table[segment]}\nM=M-D\n")
        else: # other methods can share a stack recall method
            # take value of from stack and put into D
            output_file.write(f"@SP // pop {segment} {index}\nM=M-1\nA=M\nD=M\n")

            # store to correct memory segment
            if segment == "static":
                output_file.write(f"@{file_name}.{index}\nM=D\n")

            elif segment == "temp":
                output_file.write(f"@{5+int(index)}\nM=D\n")

            elif segment == "pointer":
                output_file.write(f"@{3+int(index)}\nM=D\n")


def close(): # closes output_file
    global output_file
    output_file.close()


def setFileName(fileName):
    global file_name
    file_name = fileName
    #print(f"New file name: {file_name}")


def writeInit(call_sys):
    output_file.write("@256 //boostrap code\nD=A\n@SP\nM=D\n")
    if call_sys:
        #print("calling Sys.init 0")
        writeCall("Sys.init", 0)
        output_file.write("@None&ret.0\n0;JMP\n")


def writeLabel(label): # write a label which is filename.function%label
    output_file.write(f"({file_name}.{current_function}${label})\n")


def writeGoto(label): # jump to label
    output_file.write(f"// goto\n@{file_name}.{current_function}${label}\n0;JMP\n")


def writeIf(label):
    # pop value off stack
    # jump to label if value is -1 else do nothing
    output_file.write(f"@SP // if goto\nM=M-1\nA=M\nD=M\n@{file_name}.{current_function}${label}\nD;JGT\n")


def writeFunction(functionName, numArgs):
    global current_function
    current_function = functionName

    #print(f"writefunction: {functionName}")

    output_file.write(f"({functionName}) // function\n")
    for i in range(int(numArgs)):
        WritePushPop("C_PUSH", "constant", 0)


def writeCall(functionName, numArgs):
    global return_address_counter

    # calculate return address
    return_address = f"{current_function}&ret.{return_address_counter}"
    return_address_counter += 1
    # push return address
    output_file.write(f"@{return_address} // call {functionName} //save return address\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n")

    # push other parts of frame
    for frame_part in ["LCL", "ARG", "THIS" ,"THAT"]:
        output_file.write(f"@{frame_part} //saving frame ({frame_part})\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n")

    # move ARG
    output_file.write(f"@SP //move ARG\nD=M\n@5\nD=D-A\n@{int(numArgs)}\nD=D-A\n@ARG\nM=D\n")
    # move LCL
    output_file.write(f"@SP //move LCL\nD=M\n@LCL\nM=D\n")

    # jump to executing the function
    output_file.write(f"@{functionName}\n0;JMP\n")

    # write return address label in assembly
    output_file.write(f"({return_address})\n")


def writeReturn():
    # store end of frame address in R13
    output_file.write("@LCL // return\nD=M\n@R13\nM=D\n")
    # store return address in R14 (value of LCL is still in D)
    output_file.write("@5\nA=D-A\nD=M\n@R14\nM=D\n")
    # move return value to ARG 0
    output_file.write("@SP\nA=M-1\nD=M\n@ARG\nA=M\nM=D\n")
    # move stack pointer
    output_file.write("@ARG // return stack pointer\nD=M+1\n@SP\nM=D\n")

    # return memory segments
    for frame_part in ["THAT", "THIS", "ARG", "LCL"]:
        output_file.write(f"@R13 // return memory segment {frame_part}\nM=M-1\nA=M\nD=M\n@{frame_part}\nM=D\n")

    # jump to return address
    output_file.write(f"@R14 // jump to return address\nA=M\n0;JMP\n")
