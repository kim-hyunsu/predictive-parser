import sys

reference = sys.argv[1]
difference = sys.argv[2]
with open(reference) as f1, open(difference) as f2:
  content1 = f1.read()
  content2 = f2.read()
  if content1 == content2:
    print('COMPILE SUCCESS')
  else:
    print('COMPILE FAILURE')