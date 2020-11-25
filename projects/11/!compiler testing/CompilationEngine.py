# makes use of tokenizer to output and compile jack grammar
#modules

import JackTokenizer

# statics
type_convert_table = {  "IDENTIFIER"    : "identifier",
                        "STRING_CONST"  : "stringConstant",
                        "INT_CONST"     : "integerConstant",
                        "KEYWORD"       : "keywordConstant"}


#globals
output = None
indent = 0 # keeps track of how to indent xml for readability


def constructor(input_file, output_file): # opens files
    global output
    tokenizer.constructor(input_file)
    tokenizer.advance()
    output = output_file.open("w")


def advance_with_check():
    if tokenizer.hasMoreTokens():
        tokenizer.advance()
    else:
        print(f"program randomly ends in {tokenizer.current_token_place}: ({tokenizer.identifier()})")
        exit()


def _eat(string):
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
        print(f"impossible token type in {tokenizer.current_token_place}: {tokenizer.tokenType()}")
        exit()

    if current_token_value == string: # it is on the expected token
        # write to file
        _output_xml_term(current_token_type, current_token_value)
        # increment tokenizer forward
        advance_with_check()

    else: # unexpected token
        print(f"unexpected token in {tokenizer.current_token_place}: {current_token_value} instead of: {string}")
        exit()


def _eat_type(error_message):
    current_token_value = False

    if tokenizer.tokenType() == "KEYWORD":
        if tokenizer.keyWord() in ["INT", "CHAR", "BOOLEAN"]:
            current_token_value = tokenizer.keyWord().lower()

    elif tokenizer.tokenType() == "IDENTIFIER":
        current_token_value = tokenizer.identifier()

    if current_token_value:
        _eat(current_token_value)

    else:
        print(error_message.format(tokenizer.identifier(), tokenizer.current_token_place))
        exit()


def _eat_identifier(error_message):
    if tokenizer.tokenType() == "IDENTIFIER":
        _output_xml_term("identifier", tokenizer.identifier())
    else:
        print(error_message.format(tokenizer.identifier()))
        exit()
    advance_with_check()


def _output_xml_term(type, value):
    global indent
    output.write(f"{' '*indent*2}<{type}> {value} </{type}>\n")


def check_term():
    if tokenizer.tokenType() in ["IDENTIFIER", "INT_CONST", "STRING_CONST"]:
        return True
    elif tokenizer.tokenType() == "KEYWORD" and tokenizer.keyWord().lower() in ["true", "false", "null", "this", "-", "~"]:
        return True
    elif tokenizer.tokenType() == "SYMBOL" and tokenizer.symbol() in ["-", "~", "("]:
        return True
    else:
        return False


def CompileClass(): # compiles a class
    global indent
    # open
    output.write(f"{' '*indent*2}<class>\n")
    indent += 1
    _eat("class")

    # className
    _eat_identifier("class name in {1}: ({0}) not an identifier")
    _eat("{")

    # var declaration
    while tokenizer.keyWord() in ["STATIC", "FIELD"]:
        CompileClassVarDec()

    # subroutine declaration
    while tokenizer.keyWord() in ["CONSTRUCTOR", "FUNCTION", "METHOD"]:
        CompileSubroutineDec()

    # end } - tokenizer should have run out of tokens by this point
    if tokenizer.tokenType() == "SYMBOL" and tokenizer.symbol() == "}":
        _output_xml_term("symbol", "}")
    else:
        print(f"class has no closing bracket in {tokenizer.current_token_place}: ({tokenizer.identifier()})")
        exit()

    if tokenizer.hasMoreTokens():
        print("more tokens after end of class definition")
        exit()

    # close
    indent -= 1
    output.write(f"{' '*indent*2}</class>\n")


def CompileClassVarDec(): # compiles a static or field declaration
    global indent
    # open
    output.write(f"{' '*indent*2}<classVarDec>\n")
    indent += 1

    # static or field
    if tokenizer.keyWord() == "STATIC":
        _eat("static")
    elif tokenizer.keyWord() == "FIELD":
        _eat("field")

    # type
    _eat_type("static/ field in {1}: ({0}) not a type")

    #var name
    _eat_identifier("variable name in {1}: ({0}) not an identifier")

    # more variables
    while tokenizer.symbol() == ",":
        _eat(",")
        #var name
        _eat_identifier("variable name in {1}: ({0}) not an identifier")

    _eat(";")

    # close
    indent -= 1
    output.write(f"{' '*indent*2}</classVarDec>\n")


def CompileSubroutineDec(): # compiles a method, subroutine or constructor
    global indent
    #open
    output.write(f"{' '*indent*2}<subroutineDec>\n")
    indent += 1

    # subroutine type
    if tokenizer.keyWord() in ["CONSTRUCTOR", "FUNCTION", "METHOD"]:
        _eat(tokenizer.keyWord().lower())
    else:
        print(f"function type in {tokenizer.current_token_place}: ({tokenizer.current_token_value}) not constructor, function or method")
        exit()

    # return type
    if tokenizer.keyWord() in ["INT", "CHAR", "BOOLEAN", "VOID"]:
        _eat(tokenizer.keyWord().lower())

    elif tokenizer.tokenType() == "IDENTIFIER":
        _eat(tokenizer.identifier())

    else:
        print(f"subroutine return in {tokenizer.current_token_place}: ({tokenizer.current_token_value}) not a type")
        exit()

    # function name
    _eat_identifier("function name in {1}: ({0}) not an identifier")
    _eat("(")
    CompileParameterList()
    _eat(")")
    CompileSubroutineBody()

    # close
    indent -= 1
    output.write(f"{' '*indent*2}</subroutineDec>\n")


def CompileParameterList(): # compiles a (possibly empty)list of parameters
    global indent
    # open
    output.write(f"{' '*indent*2}<parameterList>\n")
    indent += 1

    # first paramater declaration
    if tokenizer.keyWord() in ["INT", "CHAR", "BOOLEAN"] or tokenizer.tokenType() == "IDENTIFIER":
        # first parameter type
        _eat_type("{0}{1}") # should never error as it is checked beforehand

        # first parameter name
        _eat_identifier("parameter name in {1}: ({0}) not an identifier")

    # more parameters
    while tokenizer.symbol() == ",":
        # ,
        _eat(",")

        # type
        _eat_type("parameter type in {1}: ({0}) not a type")

        # name
        _eat_identifier("parameter name in {1}: ({0}) not an identifier")

    # close
    indent -= 1
    output.write(f"{' '*indent*2}</parameterList>\n")


def CompileSubroutineBody(): # compiles the body of a subroutine
    global indent
    # open
    output.write(f"{' '*indent*2}<subroutineBody>\n")
    indent += 1
    _eat("{")

    # variable declarations
    while tokenizer.keyWord() == "VAR":
        CompileVarDec();

    # statements
    CompileStatements()

    _eat("}")

    # close
    indent -= 1
    output.write(f"{' '*indent*2}</subroutineBody>\n")


def CompileVarDec(): # compiles a var declaration
    global indent
    # open
    output.write(f"{' '*indent*2}<varDec>\n")
    indent += 1

    # var
    _eat("var")

    # type
    _eat_type("variable type in {1}: ({0}) not a type")

    # name
    _eat_identifier("variable name in {1}: ({0}) not an identifier")

    # more names
    while tokenizer.symbol() == ",":
        _eat(",")
        # name
        _eat_identifier("variable name in {1}: ({0}) not an identifier")

    # ;
    _eat(";")

    #close
    indent -= 1
    output.write(f"{' '*indent*2}</varDec>\n")


def CompileStatements(): # compiles a list of statements, not handling enclosing {}
    global indent
    # open
    output.write(f"{' '*indent*2}<statements>\n")
    indent += 1

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
            print(f"unknown keyword in {tokenizer.current_token_place}: ({tokenizer.current_token_value}) ")
            exit()


    # close
    indent -= 1
    output.write(f"{' '*indent*2}</statements>\n")


def CompileLet(): # compiles a let statement
    global indent
    # open
    output.write(f"{' '*indent*2}<letStatement>\n")
    indent += 1

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
    indent -= 1
    output.write(f"{' '*indent*2}</letStatement>\n")


def CompileIf(): # compiles an if statement
    global indent
    # open
    output.write(f"{' '*indent*2}<ifStatement>\n")
    indent += 1

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
    indent -= 1
    output.write(f"{' '*indent*2}</ifStatement>\n")


def CompileWhile(): # compiles a while statement
    global indent
    # open
    output.write(f"{' '*indent*2}<whileStatement>\n")
    indent += 1

    _eat("while")
    _eat("(")
    CompileExpression()
    _eat(")")
    _eat("{")
    CompileStatements()
    _eat("}")

    # close
    indent -= 1
    output.write(f"{' '*indent*2}</whileStatement>\n")


def CompileDo(): # compiles a do statement
    global indent
    # open
    output.write(f"{' '*indent*2}<doStatement>\n")
    indent += 1

    _eat("do")

    _eat_identifier("subroutine call name in {1}: ({0}) not an identifier")
    # normal function call
    if tokenizer.symbol() == "(":
        _eat("(")
        CompileExpressionList()
        _eat(")")

    # object function call
    elif tokenizer.symbol() == ".":
        _eat(".")
        _eat_identifier("subroutine call name in {1}: ({0}) not an identifier")
        _eat("(")
        CompileExpressionList()
        _eat(")")

    else:
        print(f"function call in {tokenizer.current_token_place}: ({tokenizer.current_token_value}) isn't called")
        exit()

    _eat(";")

    # close
    indent -= 1
    output.write(f"{' '*indent*2}</doStatement>\n")


def CompileReturn(): # compiles a return statement
    global indent
    # open
    output.write(f"{' '*indent*2}<returnStatement>\n")
    indent += 1

    _eat("return")
    if check_term():
        CompileExpression()
    _eat(";")

    # close
    indent -= 1
    output.write(f"{' '*indent*2}</returnStatement>\n")


def CompileExpression(): # compiles an expression
    global indent
    # open
    output.write(f"{' '*indent*2}<expression>\n")
    indent += 1

    CompileTerm()
    while tokenizer.symbol() in ["+", "-", "*", "/", "&amp;", "|", "&lt;", "&gt;", "="]:
        # symbol
        _eat(tokenizer.symbol())
        CompileTerm()

    # close
    indent -= 1
    output.write(f"{' '*indent*2}</expression>\n")


def CompileTerm(): # compiles a term - also determines which type of identifier it is
    global indent
    # open
    output.write(f"{' '*indent*2}<term>\n")
    indent += 1

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

    # output previous term
    _output_xml_term(previous_token_type, previous_token)

    # varName[expression]
    if tokenizer.symbol() == "[":
        _eat("[")
        CompileExpression()
        _eat("]")

    # className.subroutineName(expressionList)
    elif tokenizer.symbol() == ".":
        _eat(".")
        _eat_identifier("function name in {1}: ({0}) has to be an identifier")
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
        print(f"term starts wth keyword or symbol in {tokenizer.current_token_place}: ({previous_token})")
        exit()


    indent -= 1
    output.write(f"{' '*indent*2}</term>\n")


def CompileExpressionList(): # compiles a (possibly empty) comma separated list of expressions
    global indent
    # open
    output.write(f"{' '*indent*2}<expressionList>\n")
    indent += 1

    if check_term():
        CompileExpression()
    while tokenizer.symbol() == ",":
        _eat(",")
        CompileExpression()

    # close
    indent -= 1
    output.write(f"{' '*indent*2}</expressionList>\n")
