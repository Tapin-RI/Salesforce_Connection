from simple_salesforce import Salesforce
from auth import Creds

sf = Salesforce(username=Creds.username,
                password=Creds.password,
                security_token=Creds.token)

new_account_data = {'Name': input("Enter the Account Name: ")}

try:
    sf.Account.Create(new_account_data)
    print("New Account record created successfully.")
except Exception as e:
    print(f"Failed to create the new Account record. Error: {str(e)}")
