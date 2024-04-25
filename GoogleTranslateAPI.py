import requests

API_URL = "https://translate.googleapis.com/translate_a/single"


class Translator(object):
    def __init__(self, translate_from, translate_to):
        self.payload = {
            "client": "gtx",
            "dt": "t",

            "sl": translate_from,
            "tl": translate_to,
            "q": ""
        }

    def translate(self, word):
        self.payload['q'] = word

        with requests.Session() as sess:
            request = sess.post(API_URL, self.payload)
            post_json = request.json()

            if request.status_code == 200:
                return post_json[0][0][0], post_json[0][0][1]


translator = Translator("fa", "en")