import subprocess

command = input("Enter a command to execute: ")
args = command.split()

try:
    subprocess.run(args, check=True, shell=False)
except subprocess.CalledProcessError as e:
    print(f"Command execution failed with return code {e.returncode}")