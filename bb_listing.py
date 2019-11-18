import json
import re
import requests

# to get token from main page
resp = requests.session()
resp1=resp.get('https://www.bigbasket.com/')
cokie = resp1.headers.get('set-cookie')
prd = re.compile('csrftoken=\w+;')
token = prd.search(cokie).group()[10:-1]
print token



# choose city curl
data = {
  'city_id': '1000023',
  'next': '/',
  'csrfmiddlewaretoken': token,
  'area': '560012 , Bangalore',
  'places': '{"pincode":"560012","street":"","location":[77.567052140475,13.020773384655],"id":12,"display_name":"560012","landmark":"","type":"pincode","area_id":0,"label":"560012 , Bangalore"}',
  'continue': ''
}
response = requests.post('https://www.bigbasket.com/choose-city/', data=data)
resp2=resp.get('https://www.bigbasket.com/pc/fruits-vegetables/fresh-fruits/kiwi-melon-citrus-fruit/?nc=nb',data=data)
sid1 = re.compile('''sid = '.*;''')
scontent = resp2.content
sid = sid1.search(scontent).group()[7:-2]
print sid
slu1 = re.compile('''slug = '.*;''')
slu = slu1.search(scontent).group()[8:-2]
print slu




headers = {
    'authority': 'www.bigbasket.com',
    'accept': 'application/json, text/plain, */*',
    'x-csrftoken': 'dkwW9Vjn3lZvWUFMflsuetKLeSpYXEEaz39StY4YQbgWfpQ4ur7orUBW6RomZYfC',
    'x-requested-with': 'XMLHttpRequest',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'referer': 'https://www.bigbasket.com/pc/fruits-vegetables/fresh-fruits/kiwi-melon-citrus-fruit/?nc=nb',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cookie': '_bb_vid="NDIyNjY4MDU4Mg=="; _bb_tc=0; _client_version=2204; _bb_rdt="MzE1MzkyNzM3NA==.0"; _bb_rd=6; sessionid=ykkd9jy4h2sxo2d6y0eo72kbx087mcnq; _gcl_au=1.1.1503876782.1573801878; _ga=GA1.2.348443591.1573801879; _fbp=fb.1.1573801879802.1496149597; adb=0; _bb_source=pwa; _bb_cid=1; _gid=GA1.2.1879046409.1574051897; _sp_van_encom_hid=1718; _bb_hid=1719; _sp_bike_hid=1716; _bb_visaddr="fDU2MDAxMnw3Ny41NjcwNTIxNDA0NzV8MTMuMDIwNzczMzg0NjU1fDU2MDAxMnw="; _bb_aid="MzAwNDMzOTk4NA=="; csrftoken=dkwW9Vjn3lZvWUFMflsuetKLeSpYXEEaz39StY4YQbgWfpQ4ur7orUBW6RomZYfC; ts="2019-11-18 14:46:45.067"; bigbasket.com=80f7a905-27e6-4739-9b50-694f6bf360a9',
}

params = (
    ('type', 'pc'),
    ('slug', slu),
    ('sid', sid),
)

response = requests.get('https://www.bigbasket.com/custompage/sysgenpd/', headers=headers, params=params)
prdlist = json.loads(response.content)

count = prdlist['tab_info'][0]['product_info']['p_count']
print count
for x in range(0,(count+1)):
    # title path
    print (prdlist['tab_info'][0]['product_info']['products'][x]['p_desc'])
    # image-url path
    print(prdlist['tab_info'][0]['product_info']['products'][x]['p_img_url'])
    # product-url path
    url= (prdlist['tab_info'][0]['product_info']['products'][x]['absolute_url'])
    prd_url="https://www.bigbasket.com"+url
    print prd_url