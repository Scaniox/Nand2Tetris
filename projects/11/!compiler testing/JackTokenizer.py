                                                                                # splits input into tokens and categorises them
keywords = ['class' , 'constructor' , 'function' , 'method' ,                   # statics
            'field' , 'static' , 'var' , 'int' , 'char' , 'boolean' ,
            'void' , 'true' , 'false' , 'null' , 'this' , 'let' , 'do' ,
            'if' , 'else' , 'while' , 'return']

symbols = [ '{' , '}' , '(' , ')' , '[' , ']' , '.' , ',' , ';' , '+' , '-' ,
            '*' , '/' , '&', "|", ',' , '<' , '>' , '=' , '~']

tokens = []                                                                     # globals
current_index = 0
current_token_type = ""
current_token_value = ""
current_token_place = ""

def constructor(input_file):                                                    # takes in an input file and pre processes it into tokens
    global tokens, current_index
    tokens.clear()                                                              # reset state
    current_index = 0                                                           # which token the we have advanced to so far

    input_text = input_file.read_text()                                         # iterate through input one char at a time and store tokens
    input_name = input_file.stem

    line_index = 1                                                              # parser's current line
    column_index = 0                                                            # how far into line current character is
    char_index = 0                                                              # parser's current character
    while char_index < len(input_text):                                         # parse the code into tokens and store tokens to provide when requested
        current_char = input_text[char_index]

        if current_char == "\n":
            line_index += 1
            column_index = 0

        elif current_char == '"' :                                              # string comprehension
            start_index = char_index
            char_index = input_text.find('"', start_index+1)
            column_index += char_index - start_index
            tokens.append({"value" : input_text[start_index: char_index+1],     # get correct slice of string
                           "place" : f"{input_name}, line: {line_index}:"
                                     f"{column_index}"})

        elif current_char == "/" and \
            char_index+1 < len(input_text) and \
            input_text[char_index+1] == "/" :                                   # // comments

            start_index = char_index                                            # figure out where we are after the comment
            char_index = input_text.find("\n", char_index+1)
            column_index += char_index - start_index
            line_index += 1
            column_index = 0

        elif current_char == "/" and \
            char_index+2 < len(input_text) and \
            input_text[char_index:char_index+3] == "/**" :                      # /** comments

            start_index = char_index                                            # figure out where we are after the comment
            char_index = input_text.find("*/", char_index+3)+1
            comment = input_text[start_index:char_index+1]
            line_index += comment.count("\n")
            column_index = len(comment.split("\n")[-1])

        elif current_char in symbols:                                           # symbols
            tokens.append({"value" : current_char,
                           "place" : f"{input_name}, line: {line_index}:"
                                     f"{column_index}"})

        elif current_char not in [" ", "\n", "\t"]:                             # identifiers
            start_index = char_index
            while(input_text[char_index] not in symbols + [" ","\n","\t"]):     # continue to the end of the identifier
                char_index += 1
                column_index += 1

            tokens.append({"value" : input_text[start_index:char_index],
                           "place" : f"{input_name}, line: {line_index}:"
                                     f"{column_index}"})
            char_index -= 1                                                     # makes sure char after identifier end is not skipped
            column_index -= 1

        char_index += 1
        column_index += 1


def hasMoreTokens():                                                            # returns bool of if there are more tokens
    return current_index < len(tokens)


def advance():                                                                  # moves onto the next token
    global current_index, current_token_value, \
           current_token_type, current_token_place

    current_token_value = tokens[current_index]["value"]
    current_token_place = tokens[current_index]["place"]

    if current_token_value in keywords:                                         # classify current token as keyword
        current_token_type = "KEYWORD"

    elif current_token_value in symbols:                                        # classify current token as symbol
        current_token_type = "SYMBOL"

    elif current_token_value[0] == '"':                                         # classify current token as string constant
        current_token_type = "STRING_CONST"

    elif current_token_value[0].isnumeric():                                    # classify current token as integer contant
        current_token_type = "INT_CONST"

    else:                                                                       # classify current token as identifier
        current_token_type = "IDENTIFIER"

    current_index += 1


def tokenType():                                                                # returns (string) type of current token
    return current_token_type


def keyWord():                                                                  # returns (string) key word the current is token  (where applicable)
    return current_token_value.upper()


def symbol():                                                                   # returns (char) character which is current token (where applicable)
    return current_token_value


def identifier():                                                               # returns (string) of identifier which is current token (where applicable)
    return current_token_value


def intVal():                                                                   # returns (int) of number which is current token (where applicable)
    return int(current_token_value)


def stringVal():                                                                # returns (string) of string which is current token (where applicable)
    return current_token_value[1:-1]
