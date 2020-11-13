import os
import subprocess

if __name__ == "__main__":
    output = subprocess.run(['git', 'status'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    print(output)