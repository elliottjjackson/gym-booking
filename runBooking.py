def runBooking(website, username, password,dayClass,classTime,classNum):
    ### selenium.webbrowser - web browser functionality
    ### sys - allows terminal control
    ### bs4 - parses website's html table
    ### requests - downloads webpage content
    ### time & datetime - to log when the script runs
    ### os - retrieve system environmental variables
    ### selenium - required for website interfacing
    ### random - to generate lag between inputs to mimic a real user
    ### selenium.common.exceptions - error catches when the gym timetable changes
    import webbrowser, sys, bs4, requests, time, datetime, os,sys
    from selenium import webdriver
    from random import random
    from selenium.common.exceptions import ElementNotInteractableException
    from selenium.common.exceptions import NoSuchElementException
    #from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.firefox.options import Options
    ### website html parse script
    from htmlTableSearch import htmlTableSearch

    #Legend: Monday = 0, Sunday = 6
    #Website table has the current day as index 0.
    day = datetime.datetime.today().weekday()

    #Below determines the table index of the day of the desired class.
    if dayClass >= day:
        tableColumn = str(dayClass+1-day)
    else:
        tableColumn = str(8-(day-dayClass))

    #browser = webdriver.Chrome(executable_path=r'C:/Users/Ejay0/AppData/Local/Programs/Python/Python38/chromedriver.exe', options=chromeOptions)
    options = Options()
    browser = webdriver.Firefox(options=options)
    browser.maximize_window()
    browser.get(website)

    #time delay required for humanisation
    time.sleep(random()*3)

    #Logs into website using user credentials
    loginElem = browser.find_element_by_id('loginLink')
    loginElem.click()
    emailElem = browser.find_element_by_id('Email')
    emailElem.send_keys(username)
    time.sleep(1+random())
    pwElem = browser.find_element_by_id('Password')
    pwElem.send_keys(password)
    pwElem.submit()
    time.sleep(1+random())

    #return the index of the class time in website html table
    try:
        tableRow = str(1+htmlTableSearch(classTime,'//*[@id="timeTableTable"]/tbody/tr',browser))
    except:
        print('Class time not available on this day')
        tableRow = str(-1)

    #html Xpath for the desired class
    Xpath = '//*[@id="timeTableTable"]/tbody/tr['+tableRow+']/td['+tableColumn+']/div/a'
    
    #edits Xpath if two classes are expected at the same time slot 
    if classNum > 1:
        Xpath = Xpath[:-2]
        Xpath += '['+str(classNum)+']/a'

    #click on desired class + exception captures
    try:
        browser.find_element_by_xpath(Xpath).click()
    except ElementNotInteractableException: #exception for if class is full 
        Xpath += '[1]/img'
        try:
            browser.find_element_by_xpath(Xpath).click()      
        except NoSuchElementException: #exception if nothing works
            browser.close()
            sys.exit('Class not bookable')
    except NoSuchElementException: #exception if nothing works
        browser.close()
        sys.exit('Class not bookable')

    #time delay required for humanisation
    time.sleep(1+random())

    #click the book button
    try:
        bookButton = browser.find_element_by_name('submitButton')
        bookButton.click()
    except NoSuchElementException:
        print('Class is full or unavailable')
        pass

    #time delay required for humanisation
    time.sleep(1+random())

    browser.close()