# -*- coding: utf-8 -*-
"""billing.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12Akijq2w2Q58BD8mVxKqJenLkuenaDkK
"""

!pip install Faker

from faker import Faker

fake = Faker()

# Generate 900 rows of INSERT statements
for i in range(1,901):
    id = i  # Generate a random ID between 1 and 100
    amount = fake.random_int(min=100, max=1000)  # Generate a random amount between 100 and 1000
    patients_id = i  # Generate a random patients ID between 1 and 100
    appointments_id = i  # Generate a random appointments ID between 1 and 100
    insurances_id = i  # Generate a random insurances ID between 1 and 100
    
    # Print the INSERT statement
    print(f"INSERT INTO public.billing(id, \"Amount\", \"patientsId\", \"appointmentsId\", \"insurancesId\") "
          f"VALUES ({id}, {amount}, {patients_id}, {appointments_id}, {insurances_id});")

