import subprocess
from modules.util import COLOREND, replaceOnLine, substring_after

def main(parsedArgs: dict, command: list = ['griefficient']):
  mode = parsedArgs["mode"]
  ignored = parsedArgs["ignored"]

  # - get the output of griefficient -
  try:
    griefficient = subprocess.check_output(command, shell=True)
  except:
    print("[ERROR] Griefficinet is not installed, find a tutorial at https://github.com/Odyssey346/Griefficient")
    exit()

  # - initial formating -
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

  if resultCount == 0:
    print("No results found!")
    exit()
    
  return (final, serverLines, resultCount, firstLines)

if __name__ == '__main__':
  print("This is not a standalone program!")