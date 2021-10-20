#!/usr/bin/env python3

import shutil
import psutil
import os
import socket
from emails import generate_error_report
from emails import send_email

def check_CPU_usage():
    CPU_usage = psutil.cpu_percent(1)
    return CPU_usage > 80


def check_disk_space(disk):
    du = shutil.disk_space(disk)
    Free_space = du.free / du.total * 100
    return Free_space > 20


def check_available_memory():
    available_memory = psutil.virtual_memory().available/(1024*1024)
    return available_memory > 500


def check_localhost_connectivity():
    localhost = socket.gethostbyname('localhost')
    return localhost == '127.0.0.1'


if check_CPU_usage():
    Error_message = "Error - Available memory is less than 500MB"
elif not check_disk_space("/"):
    Error_message = "Error - Available disk space is less than 20%"
elif not check_available_memory():
    Error_message = "Error - Available memory is less than 500MB"
elif not check_localhost_connectivity():
    Error_message = "Error - localhost cannot be resolved to 127.0.0.1"
else:
    pass


if __name__ == '__main__':
    try:
        email_subject = "{}".format(Error_message)
        email_body = "Please check your system and resolve the issue as soon as possible"
        message = generate_error_report("automation@example.com", "student-04-8004cef6e6d2@example.com", email_subject, email_body)
        send_email(message)
    except NameError:
        pass
