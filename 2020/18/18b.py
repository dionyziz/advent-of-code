from collections import defaultdict
import ast, operator

with open('in.txt') as f:
  lines = f.read().splitlines()

def visit(node):
  contents = []
  for _, value in ast.iter_fields(node):
    if isinstance(value, ast.AST):
      value = [value]
    if isinstance(value, list):
      contents.extend(visit(item) for item in value)

  return defaultdict(lambda: lambda: None, {
    'Constant': lambda: node.value,
    'Expr': lambda: contents[0],
    'Module': lambda: contents[0],
    'BinOp': lambda: {
      'Add': operator.mul,
      'Mult': operator.add
    }[type(node.op).__name__](contents[0], contents[2])
  })[type(node).__name__]()

values = []
for line in lines:
  line = line.translate(''.maketrans({'+': '*', '*': '+'}))
  values.append(visit(ast.parse(line)))

print(sum(values))
