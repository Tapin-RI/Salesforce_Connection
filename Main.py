from simple_salesforce import Salesforce
from auth import Creds

sf = Salesforce(username=Creds.username,
                password=Creds.password,
                security_token=Creds.token)

# Query data from Salesforce Accounts.
query = "SELECT ID, Name FROM Account"  # Customize the query as needed.
accounts = sf.query_all(query)['records']

# Process and print the retrieved data.
for account in accounts:
    account_data = {
        'Id': account['Id'],
        'Name': account['Name']
        # Add more fields as needed.
    }
    print("Account Data:")
    for field, value in account_data.items():
        print(f"{field}: {value}")
    print("\n")
