# -*- coding: utf-8 -*-
"""
----------Phenix Labs----------
Created on Tue Jun 29 23:50:35 2021
@author: Gyan Krishna

Topic: Fake data generator test!
Library to install: pip install Faker
"""


from faker import Faker
fake = Faker()
print("fake email    :",fake.email())
print("fake country  :",fake.country())
print("fake name     :",fake.name())
print("fake text     :",fake.text())
print("fake location :",fake.latitude(), fake.longitude())
print("fake url      :",fake.url())