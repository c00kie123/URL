import requests 

def shorten_link(full_link, link_name):
    API-KEY = '2ca31aa2d18c88000c51d1cb56ab23473c91b'
    BASE-URL = ' https://cutt.ly/api/api.php'

    payload = {'key': API-KEY, 'short': full_link, 'name'=link_name}
    request = requests.get(BASE-URL, params=payload)
    data =request.json()

    print('')
    try:
      title = data['url']['title']
      shortlink = data['url']['shortLink']
      
      print("Title: ", title)
      print("Link", shortlink)
     except:
      status = data['url]['status']
      print("Error Status: ", status)

                    
link = input("Link to shorten: ")
name = input("Enter your link name: ")
shorten_link(link,name)      
