import requests

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