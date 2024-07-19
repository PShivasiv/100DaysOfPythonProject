import requests
import shutil

apikey= "YOUR API CODE"
data = input("Enter the website url:")


parameters = {
    "data":data,
    "fmt":"png",
    "fg_color":"00ff00",
}

api_url = 'https://api.api-ninjas.com/v1/qrcode'
response = requests.get(api_url, headers={'X-Api-Key': apikey,  'Accept': 'image/png'}, stream=True,params=parameters)



if response.status_code == requests.codes.ok:
    with open('E:/Python Udemy/Day-37/QRCODE.png', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
else:
    print("Error:", response.status_code, response.text)

