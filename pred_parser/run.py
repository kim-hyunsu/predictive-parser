import sys
from function.scanner import Scanner
from function.parser import Parser
from function.translator import Translator

if __name__ == '__main__':
  scanner = Scanner()
  if len(sys.argv) < 2:
    print("No file input.")
    exit()
  input = sys.argv[1]
  output = sys.argv[2]
  with open(input, 'r') as rf, open(output, 'w') as wf:
    codes = rf.read().split('\n')
    inter_codes = []
    for code in codes:
      token_list = scanner.scan(code)
      parser = Parser(token_list)
      ast = parser.parse()
      translator = Translator(ast)
      inter_code = translator.translate()
      inter_codes.append(inter_code)
    wf.write('\n'.join(inter_codes))