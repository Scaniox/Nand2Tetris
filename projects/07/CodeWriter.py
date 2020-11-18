# generates .asm code from the parsed commands

#code for each arithmetic operation
arithmetic_conversion_table = {

"add"   :
"""//add
@SP
A=M-1
D=M
M=0
@SP
M=M-1
A=M-1
M=D+M
""",

"sub"   :
"""//sub
@SP
A=M-1
D=M
M=0
@SP
M=M-1
A=M-1
M=M-D
""",

"neg"   :
"""//neg
@SP
A=M-1
M=-M
""",

"eq"    :
"""//eq
@SP
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
M=-1
(FALSE{0})
""",

"gt"    :
"""//gt
@SP
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
M=-1
(FALSE{0})
""",

"lt"    :
"""//lt
@SP
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
M=-1
(FALSE{0})
""",

"and"   :
"""//and
@SP
A=M-1
D=M
M=0
@SP
M=M-1
A=M-1
M=D&M
""",

"or"    :
"""//or
@SP
A=M-1
D=M
M=0
@SP
M=M-1
A=M-1
M=D|M
""",

"not"   :
"""//not
@SP
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
command_index = 0

def initialise(output_file_, file_name_): # initialse output file
    global output_file, file_name

    file_name = file_name_
    output_file = output_file_


def writeArithmetic(command): # write an arithemtic command to output_file
    global output_file, command_index

    output_file.write(arithmetic_conversion_table[command].format(command_index))
    command_index += 1 # used for lables to make them unique


def WritePushPop(command, segment, index): # perform stack manipulation operations
    global output_file, file_name

    if command == "C_PUSH":
        output_file.write(f"//push {segment} {index}\n")
        # load value into D
        if segment in ["local", "argument", "this", "that"]:
            output_file.write(f"@{segment_convert_table[segment]}\nD=M\n@{index}\nA=D+A\nD=M\n")

        elif segment == "constant":
            output_file.write(f"@{index}\nD=A\n")

        elif segment == "static":
            output_file.write(f"@{file_name}.{index}\nD=M\n")

        elif segment == "temp":
            output_file.write(f"@{5+int(index)}\nD=M\n")

        elif segment == "pointer":
            output_file.write(f"@{3+int(index)}\nD=M\n")

        # store value onto stack
        output_file.write("@SP\nA=M\nM=D\n@SP\nM=M+1\n")


    elif command == "C_POP":
        output_file.write(f"//pop {segment} {index}\n")

        # relative addressing required adding index to the base holding location to store that value, then subtracting the index again
        if segment in ["local", "argument", "this", "that"]:
            output_file.write(f"@{index}\nD=A\n@{segment_convert_table[segment]}\nM=D+M\n@SP\nA=M-1\nD=M\nM=0\n@{segment_convert_table[segment]}\nA=M\nM=D\n@SP\nM=M-1\n@{index}\nD=A\n@{segment_convert_table[segment]}\nM=M-D\n")
        else: # other methods can share a stack recall method
            # take value of from stack and put into D
            output_file.write("@SP\nM=M-1\nA=M\nD=M\n")

            # store to correct memory segment
            if segment == "static":
                output_file.write(f"@{file_name}.{index}\nM=D\n")

            elif segment == "temp":
                output_file.write(f"@{5+int(index)}\nM=D\n")

            elif segment == "pointer":
                output_file.write(f"@{3+int(index)}\nM=D")



def close(): # closes output_file
    global output_file
    output_file.close()
