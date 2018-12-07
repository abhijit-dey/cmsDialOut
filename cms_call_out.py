#### Install the Following Python3 Requests library for this script to work:
# `pip install requests`

import requests

#### Following information must be provided before you can start the script.
# Enter the CMS IP and the webadmin port number.
HOST = "10.106.170.215:445"
# Enter the CME webadmin username and password.
USER = "abhijit"
PASSWD = "tmeblr123"

#### Call id of the conference from which dial out has to be performed.
call_id = "125f53a4-1a64-455c-8b58-b31319fea8e0"
dial_out_uri = "user1@mmcvd.ciscolabs.com"


#### This is how CMS logs show the dial out.
# 2018-11-18	22:58:34.246	Info	10.1.1.17: API user "abhijit" created new call leg f0601ca1-5c01-43a1-a465-f124d3cb1604, call 125f53a4-1a64-455c-8b58-b31319fea8e0
# 2018-11-18	22:58:34.246	Info	call 17: outgoing SIP call to "user1@mmcvd.ciscolabs.com" from space "Test1"


#### Dont modify the below code.
def add_remote_party_to_call(call_id, remote_party):
    # make call to URI
    # POST https://<host>/api/v1/calls/<call_id>/callLegs

    try:
        response = requests.post(
            url="https://{}/api/v1/calls/{}/callLegs".format(HOST, call_id),
            auth=(USER, PASSWD),
            headers={
                "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
            },
            data={
                "remoteParty": remote_party,
            },
            verify=False
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')

add_remote_party_to_call(call_id, dial_out_uri)
