from bs4 import BeautifulSoup
import requests
import sys
import json
import time
from user_agent import generate_user_agent
from playsound import playsound

# Sends a request to the server that appears to be sent from an actual user
headers = {'User-Agent': generate_user_agent(device_type="desktop", os=('mac', 'linux'))}
url = "https://courses.illinois.edu/schedule/2018/fall/"
className = sys.argv[1]
classNumber = sys.argv[2]
CRN = sys.argv[3]
url = url + str(className) + "/" + str(classNumber)
classOpen = 0

while classOpen == 0:

		flag = 0

		r = requests.get(url, timeout=5, headers=headers)
		soup = BeautifulSoup(r.content,'html.parser')

		datastring = soup.find_all('script')[3]
		datastring = datastring.text
		datastring = datastring.encode("utf-8")
		datastring= datastring[26:-93]
		courses = json.loads(datastring)

		for course in courses:
			if CRN == course['crn']:
				while course['availability'] != 'Open' and course['availability'] != 'Open (Restricted)':
					print "Hang Tight...will let you know when the course opens"
					flag = 1
					time.sleep(300) #Refreshes the webpage every 5 minutes
					break
				if flag ==1:
					break
				print "Course is now open"
				classOpen =1
				playsound('03  Hips Dont Lie [ Featuring Wycelf Jean ] - Shakira.mp3')
				break
