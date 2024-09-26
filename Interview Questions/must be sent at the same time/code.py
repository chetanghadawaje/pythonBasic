"""
must be sent at the same time.
List of Times for a Given Day (24hr Hour:Minutes:Seconds): 09:15:25,11:58:23,13:45:09,13:45:09,13:45:09,17:22:00,17:22:00
API Call to Send GET request to "ifconfig.co" Please send a Zip file that contains the python code and a readme on how
to execute. You can import any native python packages (ex: datetime, urllib, etc...) you need but no 3rd party packages.
Things we're looking for:
proper readme
doc strings +
logging +
ability to generate test times within a few seconds to test
unit/integration tests
breaking up the main function into smaller sub function +
moving the URL to a global config +
ability to accept timestamps via the CLI +
"""

import requests
import threading
import logging
from datetime import datetime
from collections import Counter

from config import ifconfig_url, testing_flag

class TimeForDay():
    def __init__(self):
        self.time_list = ["09:15:25","11:58:23","13:45:09","13:45:09","13:45:09","17:22:00","17:22:00"]
        self.input_flag = True
        self.time_dict = dict()

    def api_call(self):
        """ This function use to call get api"""
        response = requests.get(ifconfig_url)
        logging.info(f"API Call URL={ifconfig_url} | Response = {response} | {datetime.now().time()}")
        return True if response.status_code == 200 else False

    def input_from_user(self):
        """ This method use to accept time to user"""
        while self.input_flag:
            """Here to add input time to time_list"""
            user_input = input("enter timestamps you want to add (HH:MM:SS). or press 'N'.")
            if user_input.upper() == "N":
                self.input_flag = False
            else:
                try:
                    _ = datetime.strptime(user_input, "%H:%M:%S").time()
                    self.time_list.append(user_input)
                except ValueError as err:
                    logging.exception(f"Value error exception occurred. user input: {user_input} | Message: {err}")
        logging.info(f"User update time list: {self.time_list}")
        self.time_dict = Counter(self.time_list)

    def cron_job(self):
        """This function use run continues using while loop to check time and executing call"""
        print("Cron job running...")
        while True:
            current_time = "13:45:09" if testing_flag else datetime.now().strftime('%H:%M:%S')
            time_value = self.time_dict.get(current_time, False)
            if time_value:
                self.time_dict.pop(current_time)
                for i in range(time_value):
                    print(f"API Call {i+1} in process for {current_time}.")
                    threading.Thread(target=self.api_call())
            if testing_flag:
                break

    def start_method(self):
        """ This method use to manage other method call"""
        logging.info("Main Function exacted start")
        self.input_from_user()
        self.cron_job()


if __name__ == "__main__":
    obj = TimeForDay()
    obj.start_method()
