import requests

def filedownloader(url,fname):
# retrieving HTML payload from the website
  response = requests.get(url,allow_redirects=True)
  #open the file to write in binary mode
  open(fname, 'wb').write(response.content)

url=input("Enter the URL of the image you want to download: ")  
print()
fname=input("Enter the name in which you want the file saved with the extension. \nFor example, if you want to save a file as a .jpg then,\ntype the filename with the extension .jpg ex: flower.jpg:")
filedownloader(url,fname)

