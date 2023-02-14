import requests
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import json

api_endpoint = ''
api_endpoint_for_ChannelInfor =''


useremail = ""
password = ""

data = {
    "Email": useremail,
    "Password": password
}
# Send the HTTP request
response = requests.post(api_endpoint, json=data, headers={'Content-Type': 'application/json'})

if response.status_code == 200:
    data = response.json()
    rez = data['result']
    # print(rez)
    accessToken = rez['accessToken']

    # print(accessToken)
    access_token = accessToken
   
    headers = {'Authorization': 'Bearer ' + access_token}

    # Send the HTTP request with the headers
    response = requests.get(api_endpoint_for_ChannelInfor, headers=headers)

    print(response)
    # keystream = response['streamKey']
    # print(keystream)


    global streamKEY

    # streamKEY = keystream
    

    # Check the status code
    if response.status_code == 200:
        data = response.json()
        print(data)
        res = data['result']
        playbackUrl = res['playbackUrl']
        print(playbackUrl)

        # save xml
        json_data = res
        xml_root = ET.Element('root')
        def json_to_xml(json_data, parent):
            if isinstance(json_data, dict):
                for key, value in json_data.items():
                    elem = ET.SubElement(parent, key)
                    json_to_xml(value, elem)
            elif isinstance(json_data, list):
                for item in json_data:
                    json_to_xml(item, parent)
            else:
                parent.text = str(json_data)
        json_to_xml(json_data, xml_root)
        xml_tree = ET.ElementTree(xml_root)

        # Save the XML to a file
        xml_tree.write('output1.xml', encoding='utf-8', xml_declaration=True)

        



    else:
        print('Error: status code', response.status_code)





else:
    # Handle the error (e.g. print the status code)
    print('Error: status code', response.status_code)
