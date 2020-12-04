# -*- coding: utf-8 -*-
"""
----------Phenix Labs----------
Created on Fri Dec  4 21:22:47 2020
@author: Gyan Krishna

Topic: sending emails using smtp server

how to create smtp server:-
https://medium.com/@coffmans/setup-your-own-simple-smtp-server-how-to-c9159cfc7934
"""

from string import Template
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def getContacts(filename):
    names=[]
    emails=[]
    
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for contact in contacts_file:
            names.append(contact.split[0])
            emails.append(contact.split[1])
    return names,emails,

def getTemplate(filename):
    with open(filename, mode='r', encoding='utf-8') as template_file:
        content = template_file.read()
    return content

s = smtplib.SMTP(host="127.0.0.1", port=587)
s.starttls()
s.login("GyanKrishna@mail.mydomain", "backtrack")

names,emails = getContacts("contacts.txt")
template = getTemplate("message.txt")


for name,email in zip(names, emails):
    msg = MIMEMultipart()  # creating a message
    message = template.substitute(RECEPIENT=name.title())
    
    
    msg['From']="GyanKrishna@mail.mydomain"
    msg['To'] = email
    msg['Subject'] = "hello world"
    
    msg.attach(MIMEText(message,'plain'))
    s.send_message(msg)
    
    del msg