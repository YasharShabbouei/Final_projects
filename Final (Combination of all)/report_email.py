#!/usr/bin/env python3

import os
import sys
from reports import generate_report
import datetime
from emails import generate_email, send_email

def prepare_pdf_body(Desc_Directory):
    additional_info_name = []
    additional_info_weight = []

    for each_Desc_file in os.listdir(Desc_Directory):
#        print(each_Desc_file)
        with open(Desc_Directory+each_Desc_file) as RawData:
            All_lines = RawData.readlines()
            name = All_lines[0].strip("\n")
            weight = All_lines[1].strip("\n")
            additional_info_name.append("name: " +name)
            additional_info_weight.append("weight: " +weight)
#            print(additional_info_name)
    additional_info = ""
    for i in range(len(additional_info_name)):
        additional_info += additional_info_name[i] + "<br />" + additional_info_weight[i] + "<br />" + "<br />"

    return additional_info


if __name__ == "__main__":
    Desc_Directory = "/home/student-04-8004cef6e6d2/supplier-data/descriptions/"
    Current_datetime = datetime.date.today().strftime("%B %d, %Y")
    # generate the report as PDF file
    PDF_title = "Processed Update on " + str(Current_datetime)
    additional_info = prepare_pdf_body(Desc_Directory)
    generate_report("/tmp/processed.pdf", PDF_title, additional_info)

    # generate email and send it
    email_subject = "Upload Completed - Online Fruit Store"
    email_body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    message = generate_email("automation@example.com", "student-04-8004cef6e6d2@example.com",
                             email_subject, email_body, "/tmp/processed.pdf")
    send_email(message)
