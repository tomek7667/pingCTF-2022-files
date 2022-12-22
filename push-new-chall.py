import os

os.system("git add .")
message = input("Enter commit message: ")
os.system("git commit -m '" + message + "'")
os.system("git push")