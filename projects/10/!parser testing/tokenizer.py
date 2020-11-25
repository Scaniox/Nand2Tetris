# splits input into tokens and categorises them

# statics
keywords = ['class' , 'constructor' , 'function' , 'method' ,
            'field' , 'static' , 'var' , 'int' , 'char' , 'boolean' ,
            'void' , 'true' , 'false' , 'null' , 'this' , 'let' , 'do' ,
            'if' , 'else' , 'while' , 'return']

symbols = [ '{' , '}' , '(' , ')' , '[' , ']' , '.' , ',' , ';' , '+' , '-' , '*' ,
            '/' , '&', "|", ',' , '<' , '>' , '=' , '~']

# convert for xml
token_convert_table = { "<"  : "&lt;",
                        ">"  : "&gt;",
                        '"' : "&quot;",
                        "&" : "&amp;"}

# globals
tokens = []
current_index = 0
current_token_type = ""
current_token_value = ""
current_token_place = ""

def constructor(input_file): # takes in an input file and sets up the program
    global tokens, current_index
    # reset state
    tokens.clear()
    current_index = 0
    line_index = 0

    # iterate through input one char at a time and store tokens
    input_text = input_file.read_text()
    input_name = input_file.stem

    char_index = 0
    while char_index < len(input_text):
        current_char = input_text[char_index]

        if current_char == "\n":
            line_index += 1

        # string comprehension
        if current_char == '"' :
            start_index = char_index
            char_index = input_text.find('"', start_index+1)
            # get correct slice of string
            tokens.append({"value" : input_text[start_index: char_index+1], "place" : f"{input_name} line: {line_index}"})

        # // comments
        elif current_char == "/" and char_index+1 < len(input_text) and input_text[char_index+1] == "/":
            char_index = input_text.find("\n", char_index+1)

        # /** comments
        elif current_char == "/" and char_index+2 < len(input_text) and input_text[char_index:char_index+3] == "/**":
            char_index = input_text.find("*/", char_index+3)+1

        # symbols
        elif current_char in symbols:
            tokens.append({"value" : current_char, "place" : f"{input_name} line: {line_index}"})

        # other chars
        elif not(current_char in [" ", "\n", "\t"]):
            start_index = char_index
            while(not(input_text[char_index] in symbols+[" ","\n","\t"])):
                char_index += 1
            char_index -= 1 # makes sure char after indentifier end is not missed

            tokens.append({"value" : input_text[start_index:char_index+1], "place" : f"{input_name}, line: {line_index}"})

        char_index += 1


def hasMoreTokens(): # returns bool of if there are more tokens
    return current_index < len(tokens)


def advance(): # moves onto the next token
    global current_index, current_token_value, current_token_type, current_token_place

    current_token_value = tokens[current_index]["value"]
    current_token_place = tokens[current_index]["place"]
    # classify current token
    if current_token_value in keywords:
        current_token_type = "KEYWORD"

    elif current_token_value in symbols:
        current_token_type = "SYMBOL"

    elif current_token_value[0] == '"':
        current_token_type = "STRING_CONST"

    elif current_token_value[0].isnumeric():
        current_token_type = "INT_CONST"

    else: # identifier
        current_token_type = "IDENTIFIER"

    current_index += 1


def tokenType(): # returns type of current token
    return current_token_type


def keyWord(): # returns (string) of key word the current is token  (where applicable)
    return current_token_value.upper()


def symbol(): # returns (char) of character which is current token (where applicable)
    if current_token_value in token_convert_table.keys():
        return token_convert_table[current_token_value]
    else:
        return current_token_value


def identifier(): # returns (string) of identifier which is current token (where applicable)
    return current_token_value


def intVal(): # returns (int) of number which is current token (where applicable)
    return int(current_token_value)


def stringVal(): # returns (string) of string which is current token (where applicable)
    return current_token_value[1:-1]
