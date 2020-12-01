# makes use of tokenizer to output and compile jack grammar
#modules

import JackTokenizer, SymbolTable, VMWriter

# statics
type_convert_table = {  "IDENTIFIER"    : "identifier",
                        "STRING_CONST"  : "stringConstant",
                        "INT_CONST"     : "integerConstant",
                        "KEYWORD"       : "keywordConstant"}


#globals
label_counter = 0 # used to track generated labels
current_class = None # used to track class name for function declarations


def constructor(input_file, output_file): # opens files
    global label_counter
    tokenizer.constructor(input_file)
    tokenizer.advance()
    SymbolTable.constructor()
    VMWriter.constructor(output_file)


def advance_with_check():
    if tokenizer.hasMoreTokens():
        tokenizer.advance()
    else:
        print(f"program randomly ends on {tokenizer.current_token_place}: ({tokenizer.identifier()})")
        exit()


def _eat(string): # ensures current token is what is expected and then advances
    if tokenizer.tokenType() == "IDENTIFIER":
        current_token_type = "identifier"
        current_token_value = tokenizer.identifier()

    elif tokenizer.tokenType() == "KEYWORD":
        current_token_type = "keyword"
        current_token_value = tokenizer.keyWord().lower()

    elif tokenizer.tokenType() == "SYMBOL":
        current_token_type = "symbol"
        current_token_value = tokenizer.symbol()

    elif tokenizer.tokenType() == "INT_CONST":
        current_token_type = "integerConstant"
        current_token_value = tokenizer.intVal()

    elif tokenizer.tokenType() == "STRING_CONST":
        current_token_type = "stringConstant"
        current_token_value = tokenizer.stringVal()

    else:
        print(f"impossible token type on {tokenizer.current_token_place}: {tokenizer.tokenType()}")
        exit()

    if current_token_value == string: # it is on the expected token
        # increment tokenizer forward
        advance_with_check()

    else: # unexpected token
        print(f"unexpected token on {tokenizer.current_token_place}: {current_token_value} instead of: {string}")
        exit()


def _eat_type(error_message): # eats a type token
    current_token_value = False

    if tokenizer.tokenType() == "KEYWORD":
        if tokenizer.keyWord() in ["INT", "CHAR", "BOOLEAN"]:
            current_token_value = tokenizer.keyWord().lower()

    elif tokenizer.tokenType() == "IDENTIFIER":
        current_token_value = tokenizer.identifier()

    if current_token_value:
        _eat(current_token_value)
        return current_token_value

    else:
        print(error_message.format(tokenizer.identifier(), tokenizer.current_token_place))
        exit()


def _eat_identifier(error_message): # eats an identifier token and returns it
    if tokenizer.tokenType() == "IDENTIFIER":
        current_token_value = tokenizer.identifier()
        advance_with_check()
        return current_token_value
    else:
        print(error_message.format(tokenizer.identifier()))
        exit()


def check_term(): # check if the current token is a term in an expression
    if tokenizer.tokenType() in ["IDENTIFIER", "INT_CONST", "STRING_CONST"]:
        return True
    elif tokenizer.tokenType() == "KEYWORD" and tokenizer.keyWord().lower() in ["true", "false", "null", "this", "-", "~"]:
        return True
    elif tokenizer.tokenType() == "SYMBOL" and tokenizer.symbol() in ["-", "~", "("]:
        return True
    else:
        return False


def CompileClass(): # compiles a class
    global label_counter, current_class
    # open
    # reset symbols
    SymbolTable.constructor()
    _eat("class")

    # className
    current_class = _eat_identifier("class name on {1}: ({0}) not an identifier")
    _eat("{")

    # var declaration
    while tokenizer.keyWord() in ["STATIC", "FIELD"]:
        CompileClassVarDec()

    # subroutine declaration
    while tokenizer.keyWord() in ["CONSTRUCTOR", "FUNCTION", "METHOD"]:
        CompileSubroutineDec()

    # end } - tokenizer should have run out of tokens by this point
    if not(tokenizer.tokenType() == "SYMBOL" and tokenizer.symbol() == "}"):
        print(f"class has no closing bracket on {tokenizer.current_token_place}: ({tokenizer.identifier()})")
        exit()

    if tokenizer.hasMoreTokens():
        print("more tokens after end of class definition")
        exit()

    # close


def CompileClassVarDec(): # compiles a static or field declaration
    global label_counter, current_class
    # open

    # static or field
    kind = tokenizer.keyWord()
    if kind == "STATIC":
        _eat("static")
    elif kind == "FIELD":
        _eat("field")

    # type
    type = _eat_type("static/ field on {1}: ({0}) not a type")

    #var name
    name = _eat_identifier("variable name on {1}: ({0}) not an identifier")
    #append to table
    SymbolTable.define(name, type, kind)

    # more variables
    while tokenizer.symbol() == ",":
        _eat(",")
        #var name
        name = _eat_identifier("variable name on {1}: ({0}) not an identifier")
        # append to table
        SymbolTable.define(name, type, kind)

    _eat(";")

    # close


def CompileSubroutineDec(): # compiles a method, function or constructor
    global label_counter, current_class
    #open
    # new subroutine symbol scope
    SymbolTable.startSubroutine()

    # subroutine type
    subroutine_type = tokenizer.keyWord()
    if subroutine_type in ["CONSTRUCTOR", "FUNCTION", "METHOD"]:
        _eat(subroutine_type.lower())
    else:
        print(f"function type on {tokenizer.current_token_place}: ({tokenizer.current_token_value}) isn't constructor, function or method")
        exit()

    # return type
    if tokenizer.keyWord() in ["INT", "CHAR", "BOOLEAN", "VOID"]:
        _eat(tokenizer.keyWord().lower())

    elif tokenizer.tokenType() == "IDENTIFIER":
        _eat(tokenizer.identifier())

    else:
        print(f"subroutine return on {tokenizer.current_token_place}: ({tokenizer.current_token_value}) not a type")
        exit()

    # function name
    name = _eat_identifier("function name on {1}: ({0}) not an identifier")


    _eat("(")
    parameter_count = CompileParameterList()
    _eat(")")

    # save current line of output file
    subr_declaration_line =

    #constructor code:
    if subroutine_type == "CONSTRUCTOR":
        #VM function declaration
        VMWriter.WriteFunction(f"{current_class}.{name}",) #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        # call memory alloc for to find memory block base
        field_count = SymbolTable.VarCount("field")
        VMWriter.WritePush("constant", field_count)
        VMWriter.WriteCall("Memory.alloc", 1)
        # set this (pointer 0) to block base
        VMWriter.WritePop("pointer", 0)

    # method code:
    if subroutine_type == "METHOD":
        # set this(pointer 0) to first argument
        VMWriter.WritePush("argument", 0)
        VMWriter.WritePop("pointer", 0)

    CompileSubroutineBody()

    # close


def CompileParameterList(): # compiles a (possibly empty)list of parameters
    global label_counter, current_class
    # open
    parameter_count = 0 # keeps track of how many arguments this subroutine has

    # first parameter declaration
    if tokenizer.keyWord() in ["INT", "CHAR", "BOOLEAN"] or tokenizer.tokenType() == "IDENTIFIER":
        parameter_count += 1
        # first parameter type
        type = _eat_type("{0}{1}") # should never error as it is checked beforehand

        # first parameter name
        name = _eat_identifier("parameter name on {1}: ({0}) not an identifier")

        # add parameter to table
        SymbolTable.define(name, "argument", type)

    # more parameters
    while tokenizer.symbol() == ",":
        parameter_count += 1
        # ,
        _eat(",")

        # type
        type = _eat_type("parameter type on {1}: ({0}) not a type")

        # name
        name = _eat_identifier("parameter name on {1}: ({0}) not an identifier")

        # add parameter to table
        SymbolTable.define(name, "argument", type)

    # close
    return parameter_count


def CompileSubroutineBody(): # compiles the body of a subroutine
    global label_counter, current_class
    # open
    _eat("{")

    # variable declarations
    while tokenizer.keyWord() == "VAR":
        CompileVarDec();

    # statements
    CompileStatements()

    _eat("}")

    # close


def CompileVarDec(): # compiles a var declaration
    global label_counter, current_class
    # open
    # var
    _eat("var")

    # type
    type = _eat_type("variable type on {1}: ({0}) not a type")

    # name
    name = _eat_identifier("variable name on {1}: ({0}) not an identifier")

    # add local to table
    SymbolTable.define(name, "local", type)

    # more names
    while tokenizer.symbol() == ",":
        _eat(",")
        # name
        name = _eat_identifier("variable name on {1}: ({0}) not an identifier")

        # add parameter to table
        SymbolTable.define(name, "argument", type)

    # ;
    _eat(";")

    #close


def CompileStatements(): # compiles a list of statements, not handling enclosing {}
    global label_counter, current_class
    # open

    #iterate through statements
    while True:
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
        # end of statements case
        elif tokenizer.symbol() == "}":
            break
        else:
            print(f"unknown keyword on {tokenizer.current_token_place}: ({tokenizer.current_token_value}) ")
            exit()

    # close


def CompileLet(): # compiles a let statement
    global label_counter, current_class
    # open

    _eat("let")
    # varName
    _eat_identifier("variable name {1}: ({0}) not an identifier")

    # [ expression ]
    if tokenizer.symbol() == "[":
        _eat("[")
        CompileExpression()
        _eat("]")

    _eat("=")
    CompileExpression()
    _eat(";")

    # close


def CompileIf(): # compiles an if statement
    global label_counter, current_class
    # open

    _eat("if")
    _eat("(")
    CompileExpression()
    _eat(")")
    _eat("{")
    CompileStatements()
    _eat("}")

    # else statement?
    if tokenizer.keyWord() == "ELSE":
        _eat("else")
        _eat("{")
        CompileStatements()
        _eat("}")

    #close


def CompileWhile(): # compiles a while statement
    global label_counter, current_class
    # open

    _eat("while")
    _eat("(")
    CompileExpression()
    _eat(")")
    _eat("{")
    CompileStatements()
    _eat("}")

    # close


def CompileDo(): # compiles a do statement
    global label_counter, current_class
    # open

    _eat("do")

    _eat_identifier("subroutine call name on {1}: ({0}) not an identifier")
    # normal function call
    if tokenizer.symbol() == "(":
        _eat("(")
        CompileExpressionList()
        _eat(")")

    # object function call
    elif tokenizer.symbol() == ".":
        _eat(".")
        _eat_identifier("subroutine call name on {1}: ({0}) not an identifier")
        _eat("(")
        CompileExpressionList()
        _eat(")")

    else:
        print(f"function call on {tokenizer.current_token_place}: ({tokenizer.current_token_value}) isn't called")
        exit()

    _eat(";")

    # close


def CompileReturn(): # compiles a return statement
    global label_counter, current_class
    # open

    _eat("return")
    if check_term():
        CompileExpression()
    _eat(";")

    # close

def CompileExpression(): # compiles an expression
    global label_counter, current_class
    # open

    CompileTerm()
    while tokenizer.symbol() in ["+", "-", "*", "/", "&amp;", "|", "&lt;", "&gt;", "="]:
        # symbol
        _eat(tokenizer.symbol())
        CompileTerm()

    # close


def CompileTerm(): # compiles a term - also determines which type of identifier it is
    global label_counter, current_class
    # open

    # grammar becomes ll(2) so previous token is saved and it is advanced by one
    if tokenizer.tokenType() == "IDENTIFIER":
        previous_token_type = "identifier"
        previous_token = tokenizer.identifier()

    elif tokenizer.tokenType() == "KEYWORD":
        previous_token_type = "keyword"
        previous_token = tokenizer.keyWord().lower()

    elif tokenizer.tokenType() == "SYMBOL":
        previous_token_type = "symbol"
        previous_token = tokenizer.symbol()

    elif tokenizer.tokenType() == "INT_CONST":
        previous_token_type = "integerConstant"
        previous_token = tokenizer.intVal()

    elif tokenizer.tokenType() == "STRING_CONST":
        previous_token_type = "stringConstant"
        previous_token = tokenizer.stringVal()

    advance_with_check()

    # varName[expression]
    if tokenizer.symbol() == "[":
        _eat("[")
        CompileExpression()
        _eat("]")

    # className.subroutineName(expressionList)
    elif tokenizer.symbol() == ".":
        _eat(".")
        _eat_identifier("function name on {1}: ({0}) has to be an identifier")
        _eat("(")
        CompileExpressionList()
        _eat(")")

    # unaryOp term
    elif previous_token in ["~", "-"]:
        CompileTerm()

    # (expression)
    elif previous_token == "(":
        CompileExpression()
        _eat(")")

    # subroutineName(expressionList)
    elif tokenizer.symbol() == "(":
        _eat("(")
        CompileExpressionList()
        _eat(")")


    elif not(previous_token_type in ["identifier", "stringConstant", "integerConstant"] or previous_token in ["true", "false", "null", "this"]):
        print(f"term starts wth keyword or symbol on {tokenizer.current_token_place}: ({previous_token})")
        exit()


def CompileExpressionList(): # compiles a (possibly empty) comma separated list of expressions
    global label_counter, current_class
    # open

    if check_term():
        CompileExpression()
    while tokenizer.symbol() == ",":
        _eat(",")
        CompileExpression()

    # close
