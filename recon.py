import requests
from bs4 import BeautifulSoup
import sys

# recebendo valor para a variavel atravez de argumentos. ex: python recon.py http://luci-lua.tk/ 
url = sys.argv[1]
tag = input("tag: ")

req = requests.get(str(url))
print("Status: ", req.status_code)


html  = BeautifulSoup(req.content, 'html.parser')

def result():
    print("Headers: ", req.headers)
    
    # print (html.prettify())
    # pretiffy para deixar HTML dentro do escopo
    
    # Procurar tudo o que for TAG <a></a>
    forTag = html.find_all(tag)
    
    print(tag, ":", forTag)
    
    
    

if (req.status_code == 200):
    result()
else:
    print("Nada pode ser encontrado")
