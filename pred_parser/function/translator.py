from definition.grammar import Goal, Expr, Add, Sub, Term, Mul, Div, Factor, Number, Identifier, Except, Empty

class Translator(object):
  def __init__(self, ast: Goal):
    self.ast = ast

  def _translate(self, tree: Goal) -> str:
    if isinstance(tree, Number):
      return str(tree.value)
    if isinstance(tree, Identifier):
      return str(tree.name)
    if isinstance(tree, Term):
      return tree.oper + self._translate(tree.factor) + self._translate(tree.term)
    if isinstance(tree, Expr):
      return tree.oper + self._translate(tree.term) + self._translate(tree.expr)
    if isinstance(tree, Except):
      return 'incorrect syntax'
    if isinstance(tree, Empty):
      return ''

  def translate(self) -> str:
    return self._translate(self.ast)
