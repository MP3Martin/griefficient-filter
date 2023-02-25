COLOREND = "\x1b[0m"
UPLINE = "\033[A"

def replaceOnLine(orig, char, replace, line):
  orig = orig.split('\n')
  orig[line] = orig[line].replace(char, replace)
  return "\n".join(orig)

def substring_after(s, delim):
  if delim in s:
    return s.partition(delim)[2]
  else:
    return s


if __name__ == '__main__':
  print("This is not a standalone program!")
  