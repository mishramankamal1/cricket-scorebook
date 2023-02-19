import pandas as pd
import random
import string

# Function to generate random string
def random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

# Create data for the DataFrame
def create_dataFrame():
    data = {
        'Name': [random_string(5) for i in range(100)],
        'Age': [random.randint(18, 65) for i in range(100)],
        'Gender': [random.choice(['Male', 'Female']) for i in range(100)],
        'Country': [random.choice(['USA', 'Canada', 'Mexico', 'UK']) for i in range(100)],
        'Salary': [random.randint(50000, 200000) for i in range(100)],
    }

# Create the DataFrame
    df = pd.DataFrame(data)
    return df

# Print the first 5 rows of the DataFrame

