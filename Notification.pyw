import requests
import json
from plyer import notification
import time
import playsound
from playsound import playsound


running = True
while running:
    try:
        category = 'life'
        api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
        response = requests.get(api_url, headers={'X-Api-Key': 'XD0z4rOG0ydOhkRIgk6n6g==HiHvBhj0AkTOPjo5'})
        if response.status_code == requests.codes.ok:
            print(response.text)
           
        else:
            print('Error')
    except:
        print('Error getting quote')


    quote = response.text.replace("[", "").replace("]", "").replace("{","").replace("}","")
    print(quote)

    
    notification.notify(
        title = "YOUR DAILY QUOTE",
        message = f"{quote}",
        app_icon = None,
        toast = True,
        timeout = 25
    )
    playsound("arcade.wav")
    print("playing sound")
    time.sleep(3 * 60 * 60)
    
# SUCCESS!