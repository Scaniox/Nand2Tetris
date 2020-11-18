# main program
# modules
from pathlib import Path
import CompilationEngine, sys

# file arguments
try:
    input_name = sys.argv[1]
except IndexError:
    input_name = input("input program name or directory: ")

print(f"parsing {input_name}")

input_files = Path(input_name)

# validate input file
if not(input_files.exists()):
    print("file/ folder doesn't exist")
    exit()

if input_files.is_file():# is a single file
    output_file = input_files.parent / f"{input_files.stem}.xml"
    CompilationEngine.constructor(input_files, output_file)
    CompilationEngine.CompileClass()

else: # is a directory
    output_directory = input_files.parent / f"{input_files.name} parsed"

    if output_directory.exists(): # if the directory already exists clear it
        for file in output_directory.iterdir():
            file.unlink()
    else:                   # if the directory doesn't already exist create it
        output_directory.mkdir()

    for file in input_files.iterdir():
        output_file = output_directory / f"{file.stem}.xml"
        CompilationEngine.constructor(file, output_file)
        CompilationEngine.CompileClass()
