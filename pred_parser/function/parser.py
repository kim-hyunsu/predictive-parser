from definition.token import Id, Num, Oper, Plus, Minus, Times, Over, Error
from definition.grammar import Goal, Expr, Add, Sub, Term, Mul, Div, Factor, Number, Identifier, Except, Empty

class Parser(object):
  def __init__(self, token_list):
    self.token_list = token_list
    self.length = len(token_list)
    self.index = 0
    self.token = None
    self.stack = []
    self.empty = False

  def _next_token(self):
    if (self.index < self.length):
      self.token = self.token_list[self.index]
    self.index += 1

  # goal
  def parse(self) -> Goal:
    if self.length == 0:
      return Empty()
    self._next_token()
    if isinstance(self.expr(), Error):
      return Except("Syntax Error")
    return self.stack.pop()

  def expr(self):
    if isinstance(self.term(), Error):
      return Error("Syntax Error")
    error = self.expr_prime()
    if self.empty:
      self.empty = False
      return error
    e = self.stack.pop()
    op = self.stack.pop()
    t = self.stack.pop()
    op.expr = e
    op.term = t
    self.stack.append(op)
    return error

  def expr_prime(self):
    if isinstance(self.token, Plus):
      self.stack.append(Add())
      self._next_token()
      return self.expr()
    if isinstance(self.token, Minus):
      self.stack.append(Sub())
      self._next_token()
      return self.expr()
    self.empty = True
    return None

  def term(self):
    if isinstance(self.factor(), Error):
      return Error("Syntax Error")
    error = self.term_prime()
    if self.empty:
      self.empty = False
      return None
    t = self.stack.pop()
    op = self.stack.pop()
    f = self.stack.pop()
    op.factor = f
    op.term = t
    self.stack.append(op)
    return error

  def term_prime(self):
    if isinstance(self.token, Times):
      self.stack.append(Mul())
      self._next_token()
      return self.term()
    if isinstance(self.token, Over):
      self.stack.append(Div())
      self._next_token()
      return self.term()
    self.empty = True
    return None

  def factor(self):
    if isinstance(self.token, Num):
      self.stack.append(Number(self.token.value))
      self._next_token()
      return None
    if isinstance(self.token, Id):
      self.stack.append(Identifier(self.token.name))
      self._next_token()
      return None
    return Error("Syntax Error")
