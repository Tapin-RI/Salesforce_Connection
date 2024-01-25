from simple_salesforce import Salesforce
from auth import Creds

sf = Salesforce(username=Creds.username,
                password=Creds.password,
                security_token=Creds.token)

query = "SELECT ID, Name FROM Account"
accounts = sf.query_all(query)['records']

for account in accounts:
    account_data = {
        'Id': account['Id'],
        'Name': account['Name']
    }
    print("Account Data:")
    for field, value in account_data.items():
        print(f"{field}: {value}")
    print("\n")
