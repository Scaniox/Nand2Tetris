# main program, acts as an input file handler, passing the inputs to the compilation engine

from pathlib import Path                                                        # modules
import CompilationEngine, sys

try:                                                                            #recieve command line argument for file and error if no arg recieved
    input_name = sys.argv[1]
except IndexError:
    input_name = input("input program directory: ")

print(f"parsing {input_name}")

input_files = Path(input_name)

if not(input_files.exists()):                                                   # validate input file and error if input file doesn't exist
    print("file or folder doesn't exist")
    exit()


if input_files.is_file():                                                       # is a single file
    output_file = input_files.parent / f"{input_files.stem}.vm"
    CompilationEngine.constructor(input_files, output_file)
    CompilationEngine.CompileClass()
    CompilationEngine.VMWriter.close()                                          # close VMWriter so it saves code


else:                                                                           # is a directory
    output_directory = input_files.parent / f"{input_files.name} parsed"

    if output_directory.exists():                                               #   if the directory already exists clear it
        for file in output_directory.iterdir():
            file.unlink()
    else:                                                                       #   if the directory doesn't already exist create it
        output_directory.mkdir()

    for file in input_files.iterdir():
        output_file = output_directory / f"{file.stem}.vm"
        CompilationEngine.constructor(file, output_file)
        CompilationEngine.CompileClass()
        CompilationEngine.VMWriter.close()                                      # close VMWriter so it saves code
