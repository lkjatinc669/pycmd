import subprocess
import datetime
import os

try:
    os.mkdir(".pycmdlogs")
except Exception as e:
    print(f"Exception occured : {e}")

def getDateTime():
    return {
        "date" : str(datetime.date.today()).replace("-", ""),
        "time" : datetime.datetime.now().strftime("%H:%M:%S")
    }

def writer(res):
    with open(f'./.pycmdlogs/{getDateTime()["date"]}.txt', "a+") as file:
        file.write("------------\n")
        file.write("| " + getDateTime()["time"] + "| \n") 
        file.write("------------\n")
        file.write(res + "\n") 

def shell():

    localShell = "cmd "

    while True:
        command = input(f"{localShell}> ")  
        if command.lower() in ["exit", "quit"]:
            break

        if command.lower().startswith("set name"):
            if len(command.split("=")) != 2:
                print("Error in command please use set name=cmd name default name cmd")
            localShell = command.split("=")[1].strip()
        
        process = subprocess.run(command, shell=True, capture_output=True, text=True)
        
        if process.stdout:
            print(process.stdout)
            writer(process.stdout + "\n")
        if process.stderr:
            print(process.stderr)
            writer(process.stderr + "\n")

if __name__ == "__main__":
    try:
        shell()
    except KeyboardInterrupt:
        print("PyCmd Terminated")