import os, datetime
#from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
### Time loggin script for when this script is run
from dateTimeRecord import dateTimeRecord
### Script that automates the gym website booking process using Selenium
from runBooking import runBooking

options = Options()
options.headless = True

class User:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

#Map os environment variables to py script variables
EJName = str(os.getenv('EJName'))
EJGLUser = str(os.getenv('EJEmail'))
EJGLPW = str(os.getenv('EJGLPW'))
JasName = str(os.getenv('JasName'))
JasGLUser = str(os.getenv('JasEmail'))
JasGLPW = str(os.getenv('JasGLPW'))

#Set up a class with the website username and website password.
EJ = User(EJName,EJGLUser,EJGLPW)
Jas = User(JasName,JasGLUser,JasGLPW)
goodLifeWebsite = 'https://member.clubware.com.au/GoodlifeMountlawley/timetable'

print('Start')
dateTimeRecord()

day = datetime.datetime.today().weekday()

Monday = 0
if day == Monday + 1:
    runBooking(goodLifeWebsite,Jas.username,Jas.password,Monday,'5:30 PM',1)

Tuesday = 1
if day == Tuesday + 1:
    runBooking(goodLifeWebsite,Jas.username,Jas.password,Tuesday,'4:45 PM',1)

Wednesday = 2
if day == Wednesday + 1:
    pass

Thursday = 3
if day == Thursday + 1:
    runBooking(goodLifeWebsite,Jas.username,Jas.password,Thursday,'5:30 PM',1)

Friday = 4
if day == Friday + 1:
    runBooking(goodLifeWebsite,Jas.username,Jas.password,Friday,'4:45 PM',1)

Saturday = 5
if day == Saturday + 1:
    runBooking(goodLifeWebsite,EJ.username,EJ.password,Monday,'4:45 PM',1)    

Sunday = 6
if day == Monday:
    runBooking(goodLifeWebsite,Jas.username,Jas.password,Sunday,'10:30 AM',1)
    runBooking(goodLifeWebsite,Jas.username,Jas.password,Sunday,'11:30 AM',1)
    runBooking(goodLifeWebsite,EJ.username,EJ.password,Sunday,'10:30 AM',1)    


print('Finish')
dateTimeRecord()