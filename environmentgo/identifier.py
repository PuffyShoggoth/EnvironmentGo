import base64

import requests

def invasive(s, s1):
    specl1 = ["Emerald Ash Borer", "Zebra Mussels", "Asian Carp", "Asian Long Horned Beetle", "Didymo","Purple Loosetrife","Round Goby", "Giant Hogweed", "Eastern Grey Squirrel", "Invasive Phragmites", "Dog-Strangling Vine", "Garlic Mustard", "Japanese Barberry", "Japanese Knotweed", "Miscanthus", "Wild Parsnip", "Wild Chervil","European Water Chestnut","Fanwort","Water Soldier","Yellow Iris"]
    specl = [x.lower for x in specl1]
    if s.lower() in specl:
        return True
    elif s1.lower() in specl:
        return True
    else:
        return False

def identify_image(image_bytes):
    json_dict = {
        "requests": [
            {
                "image": {
                    "content": base64.b64encode(image_bytes).decode('ascii')
                },
                "features": [
                    {
                        "type": "LABEL_DETECTION",
                        "maxResults": 1
                    }
                ]
            }
        ]

    }
    r = requests.post("https://vision.googleapis.com/v1/images:annotate?key=AIzaSyCITmpyz5bINsR8qAtJhzLlSbVBhWtn8dM",
                      json=json_dict)
    try:
        return (r.json()['responses'][0]['labelAnnotations'][1]['description']+", "+r.json()['responses'][0]['labelAnnotations'][0]['description'], invasive(r.json()['responses'][0]['labelAnnotations'][1]['description'], r.json()['responses'][0]['labelAnnotations'][0]['description']))
    except:
        return (r.json()['responses'][0]['labelAnnotations'][0]['description'], invasive(r.json()['responses'][0]['labelAnnotations'][0]['description'], ""))