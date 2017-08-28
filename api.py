import requests

'''To register for an API key with Lusha do the following....
1. Go to https://www.lusha.co/api_register
2. Fill in your information like I have shown
3. Confirm your email
4. Click the Get API Key button in the middle of the screen
5. Scroll down until you find the box that says "API Secret Keys"
6. This API key is your prized possesion. Do not share it with anyone. Its like your social security number. 
7. Copy that API key and paste it into the line that says "insert api key here" below.
8. Change the domain to whatever company you would like to look up, I listed google as an example.
9. Go to your terminal, navigate to the directory this code is stored in and run the following commands.

pip install -r requirements.txt
python api.py

This will return the search results from lusha! Great job!
'''

def lookup(domain):
	url = "https://api.lusha.co/company?domain={}".format(domain)
	## After registering you will get an api key similar to this 
	## ab31h3oaosye. Copy and paste the key into the line below 
	## and confirm the key is wrapped in quotes like the example. 
	## example:
	## headers = {"api_key": "ab31h3oaosye"}
	headers = {"api_key": "insert api key here"}
	r = requests.get(url, headers=headers)
	answer = r.json()
	print answer

## you can change this domain to whatever you would like. leave the quotes around 
## the domain like the example.
## example:
## domain = 'google.com'

domain = 'google.com'
lookup(domain)