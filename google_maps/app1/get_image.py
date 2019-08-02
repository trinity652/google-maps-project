import requests 
api_key = "_your_api_key_"
url = "https://maps.googleapis.com/maps/api/staticmap?"
zoom = 10
r = requests.get(url + "center =" + center +str() +","+str()+"&zoom =" +
                   str(zoom) + "&size = 400x400&key =" +
                             api_key + "sensor = false") 
f = open('address of the file location ', 'wb') 
f.write(r.content) 
f.close() 