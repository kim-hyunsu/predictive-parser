import re

from definition.token import Id, Num, Plus, Minus, Times, Over, Error

class Scanner(object):
  def __init__(self):
    pass

  def _scan_without_whitespace(self, word: str) -> list:
    if word.isdigit():
      return [Num(word)]
    if word in '+':
      return [Plus()]
    if word in '-':
      return [Minus()]
    if word in '*':
      return [Times()]
    if word in '/':
      return [Over()]
    if len(word) == 1:
      return [Id(word)]

    m = re.search(r'(.+)(\+|-|\*|/)(.+)', word)
    if m:
      left = m.group(1)
      op = m.group(2)
      right = m.group(3)
      return self._scan_without_whitespace(left) + self._scan_without_whitespace(op) + self._scan_without_whitespace(right)
    
    return [Error("Syntax Error")]
  
  def scan(self, code: str) -> list:
    token_list = []
    rough_list = code.strip().split()
    for word in rough_list:
      token_list.extend(self._scan_without_whitespace(word))

    return token_list