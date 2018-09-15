class Goal(object): pass
class Expr(Goal): pass
class Term(Expr): pass
class Factor(Term): pass
class Empty(Goal): pass
class Add(Expr):
  oper = '+'
  def __init__(self, term: Term = None, expr: Expr = None):
    self.term = term
    self.expr = expr
  def __repr__(self):
    return "Add({}, {})".format(self.term, self.expr)
class Sub(Expr):
  oper = '-'
  def __init__(self, term: Term = None, expr: Expr = None):
    self.term = term
    self.expr = expr
  def __repr__(self):
    return "Sub({}, {})".format(self.term, self.expr)
class Mul(Term):
  oper = '*'
  def __init__(self, factor: Factor = None, term: Term = None):
    self.factor = factor
    self.term = term
  def __repr__(self):
    return "Mul({}, {})".format(self.factor, self.term)
class Div(Term):
  oper = '/'
  def __init__(self, factor: Factor = None, term: Term = None):
    self.factor = factor
    self.term = term
  def __repr__(self):
    return "Div({}, {})".format(self.factor, self.term)
class Number(Factor):
  def __init__(self, value: int = None):
    self.value = value
  def __repr__(self):
    return "Number({})".format(self.value)
class Identifier(Factor):
  def __init__(self, name: str = None):
    self.name = name
  def __repr__(self):
    return "Identifier({})".format(self.name)
class Except(Goal):
  def __init__(self, msg: str = None):
    self.msg = msg
  def __str__(self):
    return self.msg
  def __repr__(self):
    return self.msg
  