channel_access_token = '1N/b770dxp0RGhcUgQVg/dGH3PLuq74n/BMSgJEm8dpqu16dKCPOxLLp856/E3UbQGBfoiLp+m41MqZjIpTc4fsWJ7Jb7Fo1UUWB52Q8C5aoMirMQLnLIgxLIFSUIB8PhoDF22fGKTS2IxYYN15k5wdB04t89/1O/w1cDnyilFU='
import json
import requests

richdata = {
  "size": {
    "width": 2500,
    "height": 843
  },
  "selected": True,
  "name": "Rich Menu 1",
  "chatBarText": "กดเพื่อดูเมนู",
  "areas": [
    {
      "bounds": {
        "x": 1153,
        "y": 508,
        "width": 1347,
        "height": 335
      },
      "action": {
        "type": "message",
        "text": "ออกจากการสนทนา"
      }
    }
  ]
}

def RegisRich(Rich_json, channel_access_token):
    url = 'https://api.line.me/v2/bot/richmenu'
    Rich_json = json.dumps(Rich_json)
    Authorization = 'Bearer {}'.format(channel_access_token)
    headers = {'Content-Type': 'application/json; charset=UTF-8',
               'Authorization': Authorization}
    response = requests.post(url, headers=headers, data=Rich_json)
    print(str(response.json()['richMenuId']))
    return str(response.json()['richMenuId'])


def CreateRichMenu(ImageFilePath, Rich_json, channel_access_token):
    richId = RegisRich(Rich_json=Rich_json, channel_access_token=channel_access_token)
    url = 'https://api-data.line.me/v2/bot/richmenu/{}/content'.format(richId)
    Authorization = 'Bearer {}'.format(channel_access_token)
    headers = {'Content-Type': 'image/jpeg',
               'Authorization': Authorization}
    img = open(ImageFilePath, 'rb').read()
    response = requests.post(url, headers=headers, data=img)
    print(response.json())


CreateRichMenu(ImageFilePath='img_rich_menu/richmenu.jpg', Rich_json=richdata,
               channel_access_token=channel_access_token)

# Return is richmenu-75b7b1b107d1c3617593fce43b3e3000
