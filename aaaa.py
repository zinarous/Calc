def parse_expr():
  term = parse_term()
  while 1:
    if match('+'):
      term = term + parse_term()
    elif match('-'):
      term = term - parse_term()
    else: return term

def parse_term():
  factor = parse_factor()
  while 1:
    if match('*'):
      factor = factor * parse_factor()
    elif match('/'):
      factor = factor / parse_factor()
    else: return factor

def parse_factor():
  if match('-'):
    negate = -1
  else: negate = 1
  if peek_digit():
    return negate * parse_number()
  if match('('):
    expr = parse_expr()
    if not match(')'): error
    return negate * expr
  error

def parse_number():
  num = 0
  while peek_digit():
    num = num * 10 + read_digit()
  return num