import os
import subprocess

if __name__ == "__main__":
    output = subprocess.check_output('./detect.sh', shell=True)