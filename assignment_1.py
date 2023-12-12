import os
import datetime

# The class ActivityLogger has methods to initialize the logger, log activities, and retrieve logs.
class ActivityLogger:
    def __init__(self, log_file="activity_log.txt"): # constructor of class ActivityLogger with parameter
        #log_file, which have a default value of "activity_log.txt"
        self.log_file = log_file # assigns 'log_file parameter to the attribute of instance
        self.log_file_exists() #function calling

    def log_file_exists(self): #method creates the log file if it doesn't exist
        if not os.path.exists(self.log_file): #checking file is existing or not
            with open(self.log_file, "w"): # open the file in write mode
                pass

    def log_activity(self, activity): #method add provided activity to the log_file with timestamp
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{timestamp}: {activity}\n"

        with open(self.log_file, "a") as log_file: # open the log_file in append mode
            log_file.write(log_entry)

    def get_activity_logs(self): #for retreving activity logs
        with open(self.log_file, "r") as log_file: #open the log_file in read mode
            logs = log_file.readlines() #allows to read all lines in log_file and store them to variable logs
        return logs

# Example Usage:
if __name__ == "__main__": #This block will be executed if the script is run as the main program
    logger = ActivityLogger() # object creation

    # Log activities
    logger.log_activity("Started the application")
    logger.log_activity("Performed some action")
    logger.log_activity("Finished the process")

    # Retrieve and print logs
    logs = logger.get_activity_logs()
    print("Activity Logs:")
    for log in logs:
        print(log.strip())
