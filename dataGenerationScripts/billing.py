from faker import Faker

fake = Faker()

# Open a file for writing
with open('billing_data.txt', 'w') as f:
    # Generate 900 rows of INSERT statements
    for i in range(1, 901):
        id = i  # Generate a random ID between 1 and 100
        amount = fake.random_int(min=100, max=1000)  # Generate a random amount between 100 and 1000
        patients_id = i  # Generate a random patients ID between 1 and 100
        appointments_id = i  # Generate a random appointments ID between 1 and 100
        insurances_id = i  # Generate a random insurances ID between 1 and 100
        
        # Write the INSERT statement to the file
        f.write(f"INSERT INTO public.billing(id, \"Amount\", \"appointmentsId\", \"insurancesId\") "
                f"VALUES ({id}, {amount}, {appointments_id}, {insurances_id});\n")
