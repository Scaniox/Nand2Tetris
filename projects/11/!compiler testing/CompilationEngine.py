# makes use of tokenizer to output and compile jack grammar

import JackTokenizer as tokenizer, SymbolTable, VMWriter                        # modules
                                                                                # statics
symbol_convert_table = { "+" : "ADD",                                           # converts Jack operators to VM operators
                         "-" : "SUB",
                         "&" : "AND",
                         "|" : "OR",
                         "<" : "LT",
                         ">" : "GT",
                         "=" : "EQ", }

unaryOp_counvert_table = { "~" : "NOT",                                         # converts Jack unary operators to VM operators
                           "-" : "NEG"}

segment_convert_table = { "ARG"    : "argument",                                # converts identifier kinds to segments they are mapped onto
                          "VAR"    : "local",
                          "FIELD"  : "this",
                          "STATIC" : "static"}

                                                                                # globals
label_counter = 0                                                               # used to track generated labels
current_class = None                                                            # used to track class name for function declarations


def constructor(input_file, output_file):                                       # initalises everything with the input and output files
    global label_counter
    tokenizer.constructor(input_file)
    tokenizer.advance()
    SymbolTable.constructor()
    VMWriter.constructor(output_file)


def advance_with_check():                                                       # safely advance the tokenizer
    if tokenizer.hasMoreTokens():
        tokenizer.advance()
    else:
        print(f"program randomly ends on {tokenizer.current_token_place}: "
              f"({tokenizer.identifier()})")
        VMWriter.close()
        exit()


def eat(string):                                                                # ensures current token is what is expected and then advances
    if tokenizer.tokenType() == "IDENTIFIER":                                   #   current token is a identifier
        current_tokenType = "identifier"
        current_token_value = tokenizer.identifier()

    elif tokenizer.tokenType() == "KEYWORD":                                    #   current token is a keyword
        current_tokenType = "keyword"
        current_token_value = tokenizer.keyWord().lower()

    elif tokenizer.tokenType() == "SYMBOL":                                     #   current token is a symbol
        current_tokenType = "symbol"
        current_token_value = tokenizer.symbol()

    elif tokenizer.tokenType() == "INT_CONST":                                  #   current token is a integer constant
        current_tokenType = "integerConstant"
        current_token_value = tokenizer.intVal()

    elif tokenizer.tokenType() == "STRING_CONST":                               #   current token is a string constant
        current_tokenType = "stringConstant"
        current_token_value = tokenizer.stringVal()

    else:                                                                       #   current token is unrecognised
        print(f"impossible token type on {tokenizer.current_token_place}: "
              f"{tokenizer.tokenType()}")
        VMWriter.close()
        exit()

    if current_token_value == string:                                           #   advance tokenizer if current token has correct value
        advance_with_check()

    else:                                                                       #   recognised token has wrong value
        print(f"unexpected token on {tokenizer.current_token_place}: "
              f"{current_token_value} instead of: {string}")
        VMWriter.close()
        exit()


def eat_type(error_message):                                                    # eats a type token
    current_token_value = False

    if tokenizer.tokenType() == "KEYWORD":                                      #   it is a built in type
        if tokenizer.keyWord() in ["INT", "CHAR", "BOOLEAN"]:
            current_token_value = tokenizer.keyWord().lower()
    elif tokenizer.tokenType() == "IDENTIFIER":                                 #   it is a custom object type
        current_token_value = tokenizer.identifier()

    if current_token_value:                                                     #   eat the token if the current token is a type
        eat(current_token_value)
        return current_token_value
    else:                                                                       #   output error if the current token isn't a type
        print(error_message.format(tokenizer.identifier(),
                                   tokenizer.current_token_place))
        VMWriter.close()
        exit()


def eat_identifier(error_message):                                              # eats an identifier token and returns (string) it's value
    if tokenizer.tokenType() == "IDENTIFIER":
        current_token_value = tokenizer.identifier()
        advance_with_check()
        return current_token_value
    else:                                                                       #   output error if current token isn't an identifier
        print(error_message.format(tokenizer.identifier()))
        VMWriter.close()
        exit()


def check_if_term():                                                            # check if the current token is a term in an expression
    if tokenizer.tokenType() in ["IDENTIFIER", "INT_CONST", "STRING_CONST"]:    #   identifier, integer and string tokens are terms
        return True

    elif tokenizer.tokenType() == "KEYWORD" and \
         tokenizer.keyWord().lower() in \
         ["true", "false", "null", "this", "-", "~"]:                           #   the keywords in the list are also terms
        return True

    elif tokenizer.tokenType() == "SYMBOL" and \
         tokenizer.symbol() in ["-", "~", "("]:                                 #   the symbols in the list are also terms
        return True

    else:                                                                       #   everything else isn't a term
        return False


def CompileClass():                                                             # compiles a class
    global label_counter, current_class
    # open
    SymbolTable.constructor()                                                   #   clear symbol table
    eat("class")

    current_class = eat_identifier("class name on {1}: "                        #   class Name
                                    "({0}) not an identifier")
    eat("{")

    while tokenizer.keyWord() in ["STATIC", "FIELD"]:                           #   variable (field or static) declarations
        CompileClassVarDec()

    while tokenizer.keyWord() in ["CONSTRUCTOR", "FUNCTION", "METHOD"]:         #   subroutine declarations
        CompileSubroutineDec()

    if not(tokenizer.tokenType() == "SYMBOL" and tokenizer.symbol() == "}"):    #   end of program: error if current token isn't a }
        print(f"class has no closing bracket on "
              f"{tokenizer.current_token_place}: ({tokenizer.identifier()})")
        VMWriter.close()
        exit()

    if tokenizer.hasMoreTokens():                                               #   error if there are extra tokens after the closing bracket
        print("more code after end of class definition")
        VMWriter.close()
        exit()


def CompileClassVarDec():                                                       # compiles a static or field declaration
    global label_counter, current_class

    kind = tokenizer.keyWord()                                                  #   detect if the variables are statics or fields
    if kind == "STATIC":
        eat("static")
    elif kind == "FIELD":
        eat("field")

    type = eat_type("static/ field on {1}: ({0}) not a type")                   #   detect type of the variables

    while True:
        name = eat_identifier("variable name on {1}: ({0}) not an identifier")  #   detect name of variable
        SymbolTable.define(name, type, kind)                                    #   add variable to symbol table
        if tokenizer.symbol() != ",":                                           #   end loop if there are no more commas and thus no more variables
            break
        eat(",")

    eat(";")


def CompileSubroutineDec():                                                     # compiles a method, function or constructor
    global label_counter, current_class

    SymbolTable.startSubroutine()                                               #   clear local variable symbol table

    subroutine_type = tokenizer.keyWord()                                       #   detect and eat subroutine's type
    if subroutine_type in ["CONSTRUCTOR", "FUNCTION", "METHOD"]:
        eat(subroutine_type.lower())
    else:
        print(f"subroutine type on {tokenizer.current_token_place}: "           #   error if not a subroutine type
              f"({tokenizer.current_token_value}) isn't constructor,"
              " function or method")
        VMWriter.close()
        exit()

    return_type = tokenizer.keyWord()                                           #   detect and eat subroutine's return type
    if return_type in ["INT", "CHAR", "BOOLEAN", "VOID"]:
        eat(tokenizer.keyWord().lower())

    elif tokenizer.tokenType() == "IDENTIFIER":
        eat(tokenizer.identifier())

    else:
        print(f"subroutine return type on {tokenizer.current_token_place}:"     #   error if return type isn't a type
              f" ({tokenizer.current_token_value}) not a valid type")
        VMWriter.close()
        exit()

    if subroutine_type == "METHOD":                                             #   add "this" to the symbol table as first argument (type = {current class})
        SymbolTable.define("this", current_class, "ARG")                        #   this has to be before compiling arguments so that "this" gets index 0

    name = eat_identifier("function name on {1}: ({0}) not an identifier")      #   detect subroutine's name
    eat("(")
    CompileParameterList()                                                      #   compile the subroutine's parameters
    eat(")")
    eat("{")
    CompileSubroutineVarDec()                                                   #   compile the subroutine's locals

    parameter_count = SymbolTable.VarCount("ARG")                               #   get the number of arguments and locals for this function
    local_count = SymbolTable.VarCount("VAR")

    VMWriter.WriteFunction(f"{current_class}.{name}", local_count)              #       add subroutine defining VM code

    if subroutine_type == "CONSTRUCTOR":                                        #   constructor specific VM code
        field_count = SymbolTable.VarCount("FIELD")                             #       call memory alloc for to find memory block base
        VMWriter.WritePush("constant", field_count)
        VMWriter.WriteCall("Memory.alloc", 1)
        VMWriter.WritePop("pointer", 0)                                         #       set "this" (pointer 0) to block base

    elif subroutine_type == "METHOD":                                           #   method specific code
        VMWriter.WritePush("argument", 0)                                       #       set "this"(pointer 0) to first(VM level) argument, so memory segment \n
        VMWriter.WritePop("pointer", 0)                                         #       "this" references current object

    CompileSubroutineBody()


def CompileParameterList():                                                     # compiles a possibly empty list of parameters for a subroutine
    global label_counter, current_class

    parameter_count = 0                                                         #   keeps track of how many parameters this subroutine has
    while tokenizer.keyWord() in ["INT", "CHAR", "BOOLEAN"] or \
          tokenizer.tokenType() == "IDENTIFIER":                                #   loop through parameters if there is a first parameter
        parameter_count += 1

        type = eat_type("parameter type on {1}: ({0}) not a type")              #       detect parameter type
        name = eat_identifier("parameter name on {1}: ({0}) not an identifier") #       detect parameter name
        SymbolTable.define(name, type, "ARG")                                   #       add parameter to subroutine symbol table

        if tokenizer.symbol() != ",":                                           #       break if there are no more commas and thus no more parameters
            break
        eat(",")


def CompileSubroutineVarDec():                                                  # compiles local variable declaration
    while tokenizer.tokenType() == "KEYWORD" and tokenizer.keyWord() == "VAR":
        CompileVarDec()


def CompileSubroutineBody():                                                    #   compiles the body of a subroutine
    global label_counter, current_class

    CompileStatements()                                                         #   statements
    eat("}")


def CompileVarDec():                                                            # compiles a variable declaration
    global label_counter, current_class

    eat("var")

    type = eat_type("variable type on {1}: ({0}) not a type")                   #   detect type of variables
    while True:
        name = eat_identifier("variable name on {1}: ({0}) not an identifier")  #       detect name of variable
        SymbolTable.define(name, type, "VAR")                                   #       add variable to subroutine symbol table

        if tokenizer.symbol() != ",":                                           #       break if there are no more commas and thus no more variables
            break
        eat(",")

    eat(";")


def CompileStatements():                                                        # compiles a list of statements, not handling enclosing {}
    global label_counter, current_class
    place = tokenizer.current_token_place

    while True:                                                                 #   iterate through statements
        if tokenizer.keyWord() == "LET":
            CompileLet()
        elif tokenizer.keyWord() == "IF":
            CompileIf()
        elif tokenizer.keyWord() == "WHILE":
            CompileWhile()
        elif tokenizer.keyWord() == "DO":
            CompileDo()
        elif tokenizer.keyWord() == "RETURN":
            CompileReturn()
        elif tokenizer.symbol() == "}":                                         #       end of statements
            break
        else:
            print(f"unknown keyword on {place}: "                               #       error there is an unrecognised statement
                  f"({tokenizer.current_token_value}) ")
            VMWriter.close()
            exit()


def CompileLet():                                                               # compiles a let statement
    global label_counter, current_class

    eat("let")
    destination_name = eat_identifier("variable name {1}: "                     #   variable name
                                       "({0}) not an identifier")

    if tokenizer.symbol() == "[":                                               #   store to an array
        eat("[")
        PushIdentifier(destination_name)                                        #       array base is now atop stack
        CompileExpression()                                                     #       array index is now atop stack
        VMWriter.WriteArithmetic("ADD")                                         #       full destination memory address atop stack
        eat("]")

        eat("=")
        CompileExpression()                                                     #       value to be stored is now atop stack
        VMWriter.WritePop("temp", 0)                                            #       get value to be stored out of the way so we can:
        VMWriter.WritePop("pointer", 1)                                         #       set this to destination memory address, which is on the stack
        VMWriter.WritePush("temp", 0)                                           #       get value to be stored back and:
        VMWriter.WritePop("that", 0)                                            #       store to "that 0", which we set to destination address
        eat(";")

    else:                                                                       #   store to a variable
        eat("=")
        CompileExpression()                                                     #       value to be stored is now atop stack
        segment = SymbolTable.KindOf(destination_name)
        if segment == None:                                                     #       error if destination is unknown
            print(f"let statement in {tokenizer.current_token_place} "
                  f"trys to assign a value to an unknown identifer: "
                  f"({destination_name})")
            exit()
        elif segment in ["FUNCTION", "CONSTRUCTOR", "METHOD"]:                  #       error if destination is a subroutine
            print(f"let statement in {tokenizer.current_token_place} "
                  f"trys to assign a value to a subroutine: "
                  f"({destination_name})")
            exit()

        index = SymbolTable.IndexOf(destination_name)
        VMWriter.WritePop(segment_convert_table[segment], index)                #       pop the correct value to the top of the stack
        eat(";")


def CompileIf():                                                                # compiles an if statement
    global label_counter, current_class

    this_index = label_counter                                                  #   holds the index of this if statement
    label_counter += 1

    eat("if")
    eat("(")
    CompileExpression()                                                         #   condition is on top of stack
    eat(")")
    eat("{")
    VMWriter.WriteArithmetic("NOT")
    VMWriter.WriteIf(f"if_{this_index}_else")                                   #   jump to "else" label if false
    CompileStatements()
    VMWriter.WriteGoto(f"if_{this_index}_exit")                                 #   jump to "exit" label
    eat("}")

    VMWriter.WriteLabel(f"if_{this_index}_else")                                #   VM "else" label
    if tokenizer.keyWord() == "ELSE":                                           #   compile the else statement if there is one
        eat("else")
        eat("{")
        CompileStatements()
        eat("}")
    VMWriter.WriteLabel(f"if_{this_index}_exit")                                #   VM "exit" label


def CompileWhile():                                                             # compiles a while statement
    global label_counter, current_class

    this_index = label_counter                                                  #   holds the index of this if statement
    label_counter += 1

    eat("while")
    eat("(")
    VMWriter.WriteLabel(f"while_{this_index}_loop")                             #   generate "loop start" label
    CompileExpression()                                                         #   while condition on top of stack
    VMWriter.WriteArithmetic("NOT")
    VMWriter.WriteIf(f"while_{this_index}_exit")                                #   jump to "exit" label if condition is false
    eat(")")
    eat("{")
    CompileStatements()
    VMWriter.WriteGoto(f"while_{this_index}_loop")                              #   jump back to "loop" label
    VMWriter.WriteLabel(f"while_{this_index}_exit")                             #   generate "exit" label
    eat("}")


def CompileDo():                                                                # compiles a do statement
    global label_counter, current_class

    eat("do")
    CompileTerm()                                                               # all subroutine calls are a subset of terms, so term compiler code is used
    VMWriter.WritePop("temp", 0)                                                # void returned value, which is atop stack

    eat(";")


def CompileReturn():                                                            # compiles a return statement
    global label_counter, current_class

    eat("return")
    if check_if_term():                                                         #   if there is a return value, compile its value
        CompileExpression()                                                     #       and put it's value atop the stack
    else:
        VMWriter.WritePush("constant", 0)                                       #   else, put rubbish there for the VM function to return

    VMWriter.WriteReturn()
    eat(";")


def CompileExpression():                                                        # compiles an expression, generating code that puts it atop the stack
    global label_counter, current_class

    CompileTerm()                                                               #   first term
    while tokenizer.symbol() in ["+", "-", "*", "/", "&",
                                 "|", "<", ">", "=", "("]:
        current_operator = tokenizer.symbol()
        eat(current_operator)                                                   #       eat symbol
        CompileTerm()                                                           #       eat extra term
        if current_operator == "*":                                             #       multiply and divide are OS functions to be called
            VMWriter.WriteCall("Math.multiply", 2)
        elif current_operator == "/":
            VMWriter.WriteCall("Math.divide", 2)
        else:                                                                   #       all other operators are VM level
            VMWriter.WriteArithmetic(symbol_convert_table[current_operator])


def CompileTerm():                                                              # compiles a term, generating code that puts it atop the stack
    global label_counter, current_class

    if tokenizer.tokenType() == "IDENTIFIER":                                   #   identifier term
        previous_token = tokenizer.identifier()

        advance_with_check()

        if tokenizer.symbol() == "[":                                           #       indexed variable term: (var[index])
            eat("[")
            PushIdentifier(previous_token)
            CompileExpression()
            VMWriter.WriteArithmetic("ADD")                                     #           source address on stack
            VMWriter.WritePop("pointer", 1)                                      #           set base address of "that" segment to source address
            VMWriter.WritePush("that", 0)                                       #           push data from source address (aka "that 0") onto stack
            eat("]")

        elif tokenizer.symbol() == ".":                                         #       object method call: className.subroutineName(expressionList)
            eat(".")
            object_name = previous_token
            method_name = eat_identifier("function name on {1}: "
            "({0}) has to be an identifier")
            eat("(")

            if SymbolTable.KindOf(object_name) != None:                         #           calling a method as object_name is an entry in symbol table
                object_class = SymbolTable.TypeOf(object_name)
                PushIdentifier(object_name)                                     #               push object so it's the method's first argument
                expr_len = 1
            else:                                                               #           calling a function
                object_class = object_name
                expr_len = 0

            expr_len += CompileExpressionList()
            VMWriter.WriteCall(f"{object_class}.{method_name}", expr_len)       #           call the function or method
            eat(")")

        elif tokenizer.symbol() == "(":                                         #       method call term: methodName(expressionList)
            VMWriter.WritePush("pointer", 0)
            eat("(")
            expr_len = CompileExpressionList() + 1
            eat(")")
            VMWriter.WriteCall(f"{current_class}.{previous_token}", expr_len)

        else:
            PushIdentifier(previous_token)

    elif tokenizer.tokenType() == "KEYWORD":                                    #   keyword terms
        previous_token = tokenizer.keyWord().lower()
        place = tokenizer.current_token_place
        advance_with_check()

        if previous_token in ["null", "false"]:                                 #       a null or false constant is a 0
            VMWriter.WritePush("constant", 0)
        elif previous_token == "true":                                          #       a true constant is a -1
            VMWriter.WritePush("constant", 1)
            VMWriter.WriteArithmetic("NEG")
        elif previous_token == "this":
            VMWriter.WritePush("pointer", 0)
        else:                                                                   #       error if other keywords appear in a term
            print(f"term contains an invalid keyword in "
                  f"{place} : ({previous_token})")
            exit()


    elif tokenizer.tokenType() == "SYMBOL":                                     #   symbols
        place = tokenizer.current_token_place

        if tokenizer.symbol() == "(":                                           #       bracketted expressions
            eat("(")
            CompileExpression()
            eat(")")

        elif tokenizer.symbol() in ["~", "-"]:                                  #       unaryOp terms
            symbol = tokenizer.symbol()
            advance_with_check()
            CompileTerm()
            VMWriter.WriteArithmetic(unaryOp_counvert_table[symbol])            #           convert unary op to vm language

        else:                                                                   #       error if a symbol other than ( - ~ appears in a term
            print(f"unexpected symbol in "
                  f"{place}: ({tokenizer.current_token_value})")
            VMWriter.close()
            exit()


    elif tokenizer.tokenType() == "INT_CONST":                                  #   integer constant term
        VMWriter.WritePush("constant", tokenizer.intVal())                      #       push the integer onto the stack
        advance_with_check()

    elif tokenizer.tokenType() == "STRING_CONST":                               #   string litteral term
        string_litteral = tokenizer.stringVal()
        place = tokenizer.current_token_place
        advance_with_check()

        VMWriter.WritePush("constant", len(string_litteral))# ! possible memory leak as these strings are never destroyed, but tracking them and destroying them is tricky
        VMWriter.WriteCall("String.new", 1)                                     #       create a new empty string of ample length
        VMWriter.WritePop("temp", 1)                                            #       store string pointer so it can be used many times

        for char in string_litteral:                                            #       add each character one by one to the string
            char_code = ord(char)
            if 32 <= char_code <= 126 or char_code == 128:
                VMWriter.WritePush("temp", 1)                                   #           push string base address as first argument
                VMWriter.WritePush("constant", char_code)                       #           push character as second argument
                VMWriter.WriteCall("String.appendChar", 2)                      #           call method to append character to string
                VMWriter.WritePop("temp", 0)                                    #           dispose of void return
            else:
                print(f"invalid character ({char}) in string"
                      f" ({string_litteral}) on"
                      f"{place}")
                exit()

        VMWriter.WritePush("temp", 1)                                           #       push string base address as end result of term


def PushIdentifier(identifier):                                                 # pushes an identifier's value onto the stack
    kind = SymbolTable.KindOf(identifier)
    if kind == None:                                                            #   no kind means an unknown identifier
        print(f"unknown identifier in {tokenizer.current_token_place}: "
              f"({identifier})")
        exit()

    index = SymbolTable.IndexOf(identifier)
    VMWriter.WritePush(segment_convert_table[kind], index)                      #   push from correct segment


def CompileExpressionList():                                                    # compiles a (possibly empty) comma separated list of expressions, leaving their values atop the stack
    global label_counter, current_class
    expression_count = 0

    if check_if_term():
        CompileExpression()
        expression_count += 1
    while tokenizer.symbol() == ",":
        eat(",")
        CompileExpression()
        expression_count += 1

    return expression_count
