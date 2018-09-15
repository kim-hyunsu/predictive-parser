class Id(object):
  def __init__(self, name):
    self.name = name
  def __repr__(self):
    return "Id({})".format(self.name)

class Num(object):
  def __init__(self, value):
    self.value = value
  def __repr__(self):
    return "Num({})".format(self.value)

class Oper(object): pass

class Plus(Oper):
  def __init__(self):
    pass
  def __repr__(self):
    return "Plus(+)"

class Minus(Oper):
  def __init__(self):
    pass
  def __repr__(self):
    return "Minus(-)"

class Times(Oper):
  def __init__(self):
    pass
  def __repr__(self):
    return "Times(*)"

class Over(Oper):
  def __init__(self):
    pass
  def __repr__(self):
    return "Over(/)"

class Error(object):
  def __init__(self, type):
    self.type = type
  def __repr__(self):
    return "Error({})".format(self.type)