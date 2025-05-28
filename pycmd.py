import subprocess
import datetime
import os

# Define log directory in the user's home folder
log_dir = os.path.join(os.path.expanduser("~"), ".pycmdlogs")

# Try to create the log directory
try:
    os.mkdir(log_dir)
except Exception as e:
    print(f"Exception occurred : {e}")

# Function to get current date and time in specific formats
def getDateTime():
    return {
        "date": str(datetime.date.today()).replace("-", ""),
        "time": datetime.datetime.now().strftime("%H:%M:%S")
    }

# Function to write command output to the log file
def writer(res):
    log_file_path = os.path.join(log_dir, f'{getDateTime()["date"]}.txt')
    with open(log_file_path, "a+") as file:
        file.write("------------\n")
        file.write("| " + getDateTime()["time"] + "| \n") 
        file.write("------------\n")
        file.write(res + "\n") 

# Main shell loop function
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