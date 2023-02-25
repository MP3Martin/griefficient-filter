# made by MP3Martin, licensed under MIT license
# this is the worst code i have ever made
# idk why i didn't parse the output and then reconstruct it again
import argparse
import subprocess
import sys
import os
from multiprocessing import Process
import modules.proxy as proxy
import modules.parse_griefficient as parse_griefficient

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
ARGS = parser.parse_args()
from modules.util import COLOREND, UPLINE

# MAIN
def main():
  global proxyProcess
  
  # - parse ARGS -
  mode = ARGS.mode
  ignored = ARGS.filter
  ignored = ignored.split(",")
  ignored.append("Bedrock") # we don't want bedrock servers
  grad = ARGS.grad
  proxy = ARGS.proxy
  port = int(ARGS.port)

  parsedArgs = {}
  parsedArgs.update({"mode": mode, "ignored": ignored, "grad": grad, "proxy": proxy, "port": port})

  final, serverLines, resultCount, firstLines = parse_griefficient.main(parsedArgs = parsedArgs)

  # - start displaying the output -
  grad_i = 0

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
        proxyProcess = Process(target=runProxy, daemon=True, args=('', port, (currentIp, currentPort)))
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
