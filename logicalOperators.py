def __and(lhs, rhs=None):

    operator = " AND "

    if type(lhs) is str and type(rhs) is str:
        return "(("+lhs+")"+operator+"("+rhs+"))"

    elif type(lhs) is list and rhs is None:
        if len(lhs) > 1:
            operator_string = "("
            lhs_iterator = 1
            lhs_size = len(lhs)
            for l in lhs:
                if lhs_iterator < lhs_size:
                    operator_string += "("+l+")"+operator
                elif lhs_iterator == lhs_size:
                    operator_string += "("+l+")"
                lhs_iterator = lhs_iterator+1
            operator_string += ")"
            return operator_string
        else:
            raise ValueError("Length of list must be greater than 1")

    else:
        raise TypeError(
            "Type of LHS and RHS must be string (or) "
            "LHS must a list without any RHS"
            )


def __or(lhs, rhs=None):

    operator = " OR "

    if type(lhs) is str and type(rhs) is str:
        return "(("+lhs+")"+operator+"("+rhs+"))"

    elif type(lhs) is list and rhs is None:
        if len(lhs) > 1:
            operator_string = "("
            lhs_iterator = 1
            lhs_size = len(lhs)
            for l in lhs:
                if lhs_iterator < lhs_size:
                    operator_string += "("+l+")"+operator
                elif lhs_iterator == lhs_size:
                    operator_string += "("+l+")"
                lhs_iterator = lhs_iterator+1
            operator_string += ")"
            return operator_string
        else:
            raise ValueError("Length of list must be greater than 1")

    else:
        raise TypeError(
            "Type of LHS and RHS must be string (or) "
            "LHS must a list without any RHS"
            )
