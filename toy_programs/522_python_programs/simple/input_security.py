import subprocess

command = input("Enter a command to execute: ")

if ";" in command or "|" in command:
    print("Invalid command.")
else:
    subprocess.run(command, shell=True)