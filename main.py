# made by MP3Martin, licensed under MIT license
# this is the worst code i have ever made
# idk why i didn't parse the output and then reconstruct it again
import argparse
import subprocess
import sys
import os
from multiprocessing import Process
import modules.proxy as proxy

def runProxy(ip, port, current):
  proxy.main('', port, current)
proxyProcess = None

# ARGUMENTS PARSING WRAPPER
parser = argparse.ArgumentParser(description="Run griefficient and filter it's output.")
parser.add_argument("-m", "--mode", dest="mode", choices=["b", "w"], default="b", help="the filtering mode (b for blacklist / w for whitelist) (default: b)")
parser.add_argument("-f", "--filter", dest="filter", default="🕅🕅🕅🕅🕅🕅🕅🕅🕅🕅🕅🕅🕅🕅🕅🕅🕅", help="the filter string(s) that filter the version info (separate with commas)", type=str)
parser.add_argument("-g", "--grad", dest="grad", action="store_const", const=True, default=False, help="if the servers should be shown gradually (on ENTER key press)")
parser.add_argument("-pr", "--proxy", dest="proxy", action="store_const", const=True, default=False, help="enable local proxy that connects to the remote server (works only if --grad is enabled)")
parser.add_argument("-p", "--port", dest="port", default=25565, help="the local proxy port (works only if --proxy is enabled) (default: 25565)", type=int)

# CONSTS
COLOREND = "\x1b[0m"
# ARGS = sys.argv
ARGS = parser.parse_args()
UPLINE = "\033[A"

# FUNCTIONS
def replaceOnLine(orig, char, replace, line):
  orig = orig.split('\n')
  orig[line] = orig[line].replace(char, replace)
  return "\n".join(orig)

def substring_after(s, delim):
  if delim in s:
    return s.partition(delim)[2]
  else:
    return s

def cls():
  print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

# MAIN
def main():
  global proxyProcess
  # - initial formating -
  try:
    griefficient = subprocess.check_output(['griefficient'], shell=True)
  except:
    raise Exception("Griefficinet is not installed, find tutorial at https://github.com/Odyssey346/Griefficient")

  out = griefficient
  out = f"{out}"
  out = out[2:]
  out = out[:-3]
  out = out.replace("\\n", "\n")

  if out.count("\n") < 3:
    final = out
  else:
    out = f"\x1b[0;34;40m{out}"
    out = replaceOnLine(out, "by Odyssey346", "\x1b[0;32;40mby Odyssey346", 0)
    out = out.replace("\n", "\x1b[0m\n", 1)
    out = out.replace("\\xe2\\x9c\\x85", "\U00002705")
    out = out.replace("\\xf0\\x9f\\x94\\x8e", "\U0001F50E")
    out = out.replace("\\xf0\\x9f\\x91\\x89", "\x1b[0;36;40m" + "\U0001F449")
    out = out.replace("Environment variables are set properly.", "\x1b[0;32;40m" + "Environment variables are set properly." + COLOREND)
    out = out.replace("Getting data from Shodan's API, please wait...", "\x1b[0;32;40m" + "Getting data from Shodan's API, please wait..." + COLOREND)
    out = out.replace("results shown out", COLOREND + "results shown out")
    out = out.replace("shown out of", "shown out of" + "\x1b[0;36;40m")
    out = out.replace("possible results", COLOREND + "possible results")

    # - seperate outputs -
    firstLines = '\n'.join(out.split('\n')[:3])
    serverLines = '\n'.join(out.split('\n')[3:-1])
    lastLines = '\n'.join(out.split('\n')[-1:])

    # - format serverLines -
    serverLines = serverLines.replace("\n", "\n" + "\x1b[0;34;40m")
    serverLines = f"\x1b[0;34;40m{serverLines}{COLOREND}"
    serverLines = serverLines.replace("(", "\x1b[0;36;40m" + "(")

    # - parse ARGS -
    mode = ARGS.mode

    ignored = ARGS.filter
    ignored = ignored.split(",")
    # we don't want bedrock servers
    ignored.append("Bedrock")

    grad = ARGS.grad

    proxy = ARGS.proxy

    port = int(ARGS.port)

    # - filter serverLines -
    serverLines = serverLines.split("\n")
    tmpServerLines = []
    if mode == "w":
      # whitelist mode
      for line in serverLines:
        if any(bad in substring_after(line, "(") for bad in ignored):
          tmpServerLines.append(line)
    else:
      # blacklist mode
      for line in serverLines:
        if not any(bad in substring_after(line, "(") for bad in ignored):
          tmpServerLines.append(line)
    serverLines = "\n".join(tmpServerLines)

    # - additional formating -
    if str.encode(serverLines) == b'':
      resultCount = 0
    else:
      resultCount = serverLines.count('\n') + 1
    
    lastLines = lastLines.replace("100", str(resultCount))

    # - combine all *Lines -
    final = f"{firstLines}\n{serverLines}\n{lastLines}"

  grad_i = 0

  if resultCount == 0:
    print("No results found!")
    exit()

  if not grad:
    print(final)
  else:
    print("\n\n\n\n\n\n\n\n")
    for line in serverLines.split("\n"):
      grad_i = grad_i + 1
      currentAdress = line.split("\x1b")[1].replace(" ", "").replace("[0;34;40m", "").split(":")
      currentIp = currentAdress[0]
      currentPort = currentAdress[1]
      if proxy:
        # start the proxy
        proxyProcess = Process(target=runProxy, args=('', port, (currentIp, currentPort)))
        proxyProcess.start()
      addSpaces = ""
      for _ in range(int(str(len(line) - os.get_terminal_size().columns).replace("-", "")) + 20):
        addSpaces = addSpaces + " "
      a = firstLines
      b = "\n\n" + line + addSpaces + "\n\n"
      c = f"\x1b[0;36;40m👉 \x1b[0;33;40m#{grad_i} \x1b[0mof \x1b[0;36;40m{str(resultCount)} \x1b[0mresults shown out of\x1b[0;36;40m 215187 \x1b[0mpossible results (blame Shodan)"
      print(UPLINE+UPLINE+UPLINE+UPLINE+UPLINE+UPLINE+UPLINE+UPLINE+a+b+c)
      if input(f"Press \x1b[0;33;40mENTER{COLOREND} to show \x1b[0;33;40mnext server{COLOREND}. Type \x1b[0;33;40mEND{COLOREND} and press \x1b[0;33;40mENTER{COLOREND} to \x1b[0;33;40mend the program{COLOREND}.").lower() == "end":
        if proxy:
          proxyProcess.kill()
        exit()
      if proxy:
        proxyProcess.kill()
        proxyProcess = None

if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt:
    try:
      proxyProcess.kill()
    except:
      pass
    exit()
