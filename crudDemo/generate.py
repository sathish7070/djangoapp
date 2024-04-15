import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','crudDemo.settings')

import django
django.setup()

from crudapp.models import *
from faker import Faker 
from random import *

faker=Faker()


def generate (n):
    for i in range(n):
        fsno=randint(1,1000)
        fsname=faker.name()
        fsclass=randint(1,12)
        fsaddress=faker.city()
        Stud_record=Student.objects.get_or_create(sno=fsno,sname=fsname,sclass=fsclass,saddress=fsaddress)

generate(20)        

