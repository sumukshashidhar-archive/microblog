import os
import subprocess

if __name__ == "__main__":
    output = subprocess.check_output('git status', shell=True)
    print(str(output))