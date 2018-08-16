def __eq(lhs, rhs):

    operator = " = "
    return "`"+str(lhs)+"`"+operator+"'"+str(rhs)+"'"


def __gt(lhs, rhs):

    operator = " > "
    return "`"+str(lhs)+"`"+operator+"'"+str(rhs)+"'"


def __lt(lhs, rhs):

    operator = " < "
    return "`"+str(lhs)+"`"+operator+"'"+str(rhs)+"'"


def __ge(lhs, rhs):

    operator = " >= "
    return "`"+str(lhs)+"`"+operator+"'"+str(rhs)+"'"


def __le(lhs, rhs):

    operator = " <= "
    return "`"+str(lhs)+"`"+operator+"'"+str(rhs)+"'"


def __ne(lhs, rhs):

    operator = " <> "
    return "`"+str(lhs)+"`"+operator+"'"+str(rhs)+"'"
