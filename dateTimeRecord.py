def dateTimeRecord():
    from datetime import datetime
    import os
    
    #get directory of current script
    directory = str(os.path.dirname(os.path.realpath(__file__)))

    #retrieve and report date and time
    now = datetime.now()
    now_str = now.strftime("%d/%m/%y %H:%M:%S")
    print("date and time : ",now_str)

    #set up text file and append with date and time.
    directory = directory.replace('\\','/') + '/text-store.txt'
    with open(directory,"a+") as file_object:
        file_object.seek(0)
        data = file_object.read(100)
        if len(data) > 0 :
            file_object.write("\n")
        file_object.write(now_str)