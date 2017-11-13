import urllib.request
try:
    urllib.request.urlopen("https://www.google.com", timeout=2)
    print ("working connection")
 
except urllib.request.URLError:
    print ("No internet connection")