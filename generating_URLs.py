environment_list = ["production", "staging", "development", "sandbox"]
endpoint_list = ["orders", "transactions", "balance", "store"]
BASE_URL ='https://{environment}.happyapi.com/{endpoint}?access_token={access_token}'

access_token = input("Please type in the access token: ")
for environment  in environment_list:
    for endpoint in endpoint_list:
        current_url = f"https://{environment}.happyapi.com/{endpoint}?access_token={access_token}"
        print(current_url)