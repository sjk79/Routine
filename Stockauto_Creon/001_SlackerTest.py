import requests
 
def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )
    print(response)
 
myToken = "xoxb-2483926020578-2469328976551-Qcu5xUqVzxqSsPeQ0Mv5RxHz"
 
post_message(myToken,"#stock_test","test")
