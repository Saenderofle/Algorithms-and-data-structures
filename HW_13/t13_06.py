precedence = {"+": 1, "-": 1, "*": 2, "/": 2}

def parse_prefix(expr, i):
    token = expr[i]
    if token.isalpha():
        # Операнд – присвоюємо йому "високий" пріоритет, щоб уникнути дужок.
        return token, 3, i + 1
    else:
        op = token
        op_prec = precedence[op]
        left_expr, left_prec, i = parse_prefix(expr, i + 1)
        right_expr, right_prec, i = parse_prefix(expr, i)
        if left_prec < op_prec:
            left_expr = "(" + left_expr + ")"
        if right_prec < op_prec or (right_prec == op_prec and op in "-/"):
            right_expr = "(" + right_expr + ")"
        return left_expr + op + right_expr, op_prec, i

if __name__ == '__main__':
    expr = input().strip()
    infix, _, _ = parse_prefix(expr, 0)
    print(infix)
