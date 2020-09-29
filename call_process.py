import os

print("Start Call process ...")
print("pid=" + str(os.getpid()))

os.execvp("python3" , ("python3", "process.py"))

# os.execvp("ls" , " -all"))

print("End Call Process ...")
