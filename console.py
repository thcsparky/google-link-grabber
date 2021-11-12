import requests
intro = "Google Link Finder: I decided to make this program again with a console app because of the way PyQt5 handles loops, it causes the program to hang before ever updating the list"


print(intro)

def main():
    a = input('Enter search term \n').rstrip()
    data = "url?q="
    url = "https://google.com/search?q=REPLACE&client=firefox-b-1-e"

    curpos = 0
    ended = ''
    strout = ''
    while data.find('url?q=') > -1 and ended == '':
        if curpos == 0:
            url = url.replace('REPLACE', a)
        
            req = requests.get(url)
            if req.status_code != 200:
                data = 'url?q='
                break
            elif req.status_code == 200:
                data = req.text 

                links = data.split('url?q=')
                for x in links:
                    link = x.split('&amp')[0]
                    if link.startswith('https') and not link.startswith('https://support') and not link.startswith('https://accounts'):
                        print(link)
                        strout += link + '\n'

        elif curpos > 0:
            url = url.replace('REPLACE', a)

            url2 = url + '&start=' + str(curpos)
            req = requests.get(url2)
            if req.status_code != 200:
                data = 'url?q='
                break
            elif req.status_code == 200:
                data = req.text 
                
                links = data.split('url?q=')
                for x in links:
                    link = x.split('&amp')[0]
                    if link.startswith('https') and not link.startswith('https://support') and not link.startswith('https://accounts'):
                        print(link)
                        strout += link + '\n'
        curpos += 10

    print("Program ended.\n")
    print(strout)
if __name__ == "__main__":
    main()