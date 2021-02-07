def htmlTableSearch(textFind,xpath,browser):
    #create text array for all html text in xpath location
    texts = [ i.text for i in browser.find_elements_by_xpath(xpath) ]

    #loop finds the indeces that contain the text and stores in indexMatch
    indexMatch = []
    i = 0
    while i < len(texts):
        if textFind in texts[i]:
            indexMatch.append(i)
        i += 1

    #returns the index of the first instance of the searched text
    return(indexMatch[0])