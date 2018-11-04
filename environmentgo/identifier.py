import base64

import requests


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
    return r.json()['responses'][0]['labelAnnotations'][0]['description']
