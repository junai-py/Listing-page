import csv
import re
import math
import xlsxwriter
import requests
from lxml import html
import configparser
# path for the configure file
config = configparser.ConfigParser()
config.read('config.ini')

cookies = {
    'userSegment': '50-percent',
    'vtc': 'cdoeNj9L0__y0EjR9Y2LZc',
    'walmart.nearestPostalCode': 'P7B3Z7',
    'walmart.nearestLatLng': '48.4120872,-89.2413988',
    '_gcl_au': '1.1.614532968.1573210445',
    'cto_lwid': 'dfcc6b50-0304-4889-8aa9-8a9b84315047',
    '_fbp': 'fb.1.1573210446216.1721535546',
    'walmart.shippingPostalCode': 'P7B3Z7',
    'defaultNearestStoreId': '3124',
    'wmt.c': '0',
    'walmart.id': 'dd674c50-aaee-4279-a6a5-6a06f0853530',
    '_ga': 'GA1.2.402624589.1573210447',
    '__gads': 'ID=0ab638475a73c629:T=1573210447:S=ALNI_MYYZNRevsdPXqNulbPPSXnfTwJqoQ',
    's_ecid': 'MCMID%7C51738210376231396870554991472031887395',
    'DYN_USER_ID': '90777814-ee28-4ccc-884c-a3021b7e28bd',
    'WM_SEC.AUTH_TOKEN': 'MTAyOTYyMDE4HYlTdyCPJJwoQdFM/X0V++9mvtutMA0Iz/Sl2vywoJc7Um9gU9BBFygLeTFR7YifDXAzi3z/Hq92rWb1UIl89Va+dcOPvXUlnuWE4XfsxQUQLPcqBTY9clppxKQp4AGEj8OFN4dileb20bpDLeCIlSFd/Hsc7bnSe4+TLU2zbj0IFK+y/Gap1sHmahcf+haAK6gW32Es8Nhx2Ld6uRcKZ+SQRjag9i3lcQdP4rqyG0Db/SoGFgAYL9DGZ8K45WCX9t4mIdf/51xP5AC/IE1umnTJFncH3NLumc8CCE5K9XkKsNqUwKygo1rZvlGJv9Pou3jNtzMSFUQbBtexUYLngB3mKRAU738BwImVB03J7/4PCv9qkuAuSK1PebmbRR68dQSEL00zgCEtAMuOkVZMYA==',
    'LT': '1573210448009',
    'wmt.breakpoint': 'd',
    'DYN_USER_ID.ro': '90777814-ee28-4ccc-884c-a3021b7e28bd',
    'TBV': '7',
    'previousBreakpoint': 'desktop',
    'walmart.locale': 'en',
    'og_session_id': 'af0a84f8847311e3b233bc764e1107f2.697188.1573210456',
    'DYN_USER_CONFIRM': '81a016ef496b9ff8cf33a2ea6a5dc7cc',
    'BVBRANDID': '2243528e-6faf-4e19-ac27-2aeab6269799',
    '_gid': 'GA1.2.890490997.1573447272',
    'zone': '9',
    'deliveryCatchment': '3124',
    'walmart.csrf': 'e2251384693f0ca7478436ef',
    'rxVisitor': '1573630703057AB2D5Q2HD5M9I0GVI44JB9MDSBEU89HL',
    'headerType': 'whiteGM',
    'usrState': '1',
    'og_session_id_conf': 'af0a84f8847311e3b233bc764e1107f2.697188.1573210456',
    'AMCVS_C4C6370453309C960A490D44%40AdobeOrg': '1',
    's_cc': 'true',
    'og_autoship': '0',
    'dtCookie': '34$5GU1KLTS8CT7BRF31JM3LIR1G1SJM9KS',
    'authDuration': '{"lat":"1573631861074000","lt":"1573631861074000"}',
    'ENV': 'ak-cdc-prod',
    'bstc': 'SCu8eFmY1ctKPehNTfkXV4',
    'xpa': '2lwWQ|4cnYb|AGGCM|CCpW9|LVSOt|MZ9tt|N3K-b|NOECn|NOaJP|P7oLY|SXgTw|YuWN8|fIfOs|jeBOs|kEwnS|sGGbM|yI7_k',
    'exp-ck': '2lwWQ34cnYb4AGGCM1CCpW92LVSOt1MZ9tt1N3K-b9NOECn2NOaJPqP7oLYcSXgTw6YuWN81fIfOsyjeBOs3kEwnS1sGGbM4yI7_k1',
    'TS01f4281b': '01c5a4e2f95723c6bb3801ed626dbdfab7aadfc16f60a873a0cb8dc092c86606f3961bbdcfcb6906693ccf4299b760f0959d2b9dc5',
    'TS011fb5f6': '01c5a4e2f95723c6bb3801ed626dbdfab7aadfc16f60a873a0cb8dc092c86606f3961bbdcfcb6906693ccf4299b760f0959d2b9dc5',
    'TS0175e29f': '01c5a4e2f95723c6bb3801ed626dbdfab7aadfc16f60a873a0cb8dc092c86606f3961bbdcfcb6906693ccf4299b760f0959d2b9dc5',
    'akaau_P1': '1573646637~id=a2aa466ef65b5ead99a074f87f5f7158',
    'rxvt': '1573646636938|1573644836938',
    'dtPC': '34$444836915_992h1vEKUCVQSDLNFEPVLECURHMSWIMEUXSKVZ',
    'xpm': '1%2B1573644836%2BcdoeNj9L0__y0EjR9Y2LZc~%2B0',
    'JSESSIONID': 'DE9DBA548FC69A51E8B490D96404E227.restapp-375463611-8-402001703',
    'JSESSIONID.ro': 'DE9DBA548FC69A51E8B490D96404E227.restapp-375463611-8-402001703',
    's_visit': '1',
    'AMCV_C4C6370453309C960A490D44%40AdobeOrg': '1585540135%7CMCIDTS%7C18214%7CMCMID%7C51738210376231396870554991472031887395%7CMCAAMLH-1574249641%7C9%7CMCAAMB-1574249641%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1573652042s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.4.0',
    'seqnum': '8',
    's_gnr': '1573644895625-Repeat',
    '_4c_': 'jVTbbqMwEP2VCmn7VALGNxypqtJstRc1vey22kdkbDdYIYCMU5qt8u87TnNpV1ppeQDP8ZmDZ5jDazRUponGiHLMCBGECZadRQuz7qPxa%2BSsDo%2FnaByVSmvDFY4N4iIGpo5FTkmsUpIhhjChREZn0UvQylORM0IZpXhzFulmr6HNk1zV%2FiONcUZSoNk9S%2F69nyME%2B27YEfYbPEsR%2B0DdIkBV3Y76Gq1cDZKV910%2FTpJhGEaDrJfS%2BZGSiWmSUpbr7S0upa%2FifmGbWElnjlhyE%2BeY0qSTcxMjOJtqtQFNJEb5iELsf0OEcQrLzrV6pXzh112gDKY86fUCNrR5tsoUg9W%2BCrksTY9oZey88gCLN7RzgQKrwTa6HY5ZFOMjesgiOHBL1w69CZnTyrVLc8JzQFv4jNG1bVYvEDjzZJzbcv7dEFMb5V3bWNVD5SjFF1ZZfV6B5KcsDU0ovt4VD203ld7MW7curo4Zxa8ZvKe3flv9QXeHwVQBDMHt7OFHcXk1md7evDtLu2ysXzkT9339%2FlBl0vfJsLRKNlLL0OIEJd9%2FxtkI0VEaX4vHu6TnPEUYZ5ixXFB%2BMbm%2FPEenSzg4RRznGdTBWYYRFiznKaVECBTGBaM851jQ08n91XloYxcmMHS5bpWsQxlgj7Poy6R4%2FPY5NDvNWEZoLkbBMqBLCN9XNJtuKf%2F3Rkh6cHY%2BN25mfNWCzyCW2nrbNrKO3mzzzjE6fGpVy763Spt%2B4dsu2uymn2OOUUayPAc%2FeA8TD2ZIwwWM54OxyrTEWmEWY8NJTBhBsRSliDMhqdLKgMjBe%2BF3wBjJKKE7SZS%2FKW42fwA%3D',
}
headers = {
    'authority': 'www.walmart.ca',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
    'sec-fetch-user': '?1',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'if-modified-since': 'Wed, 13 Nov 2019 09:31:09 GMT',
}

Image = []
Title = []
Prdurl = []
Page = []
Total_prd=0

# to find out the no of pages & product
def path(url):

    resp = requests.get(url=url, headers=headers, cookies=cookies)
    tree = html.fromstring(resp.content)
    total = tree.xpath('//*[@id="shelf-sort-count"]/span[3]/text()')
    prd = total[0]
    Total_prd = int(prd)
    print ("Total products:{}".format(prd))
    page = int(math.ceil(Total_prd / 60) + 1)
    print ("Total Pages:{}".format(page))
    fetching_loop(page)
    return Total_prd
# loop to extract all the data for all pages
def fetching_loop(page):
    for x in range(1, (page + 1)):
        no = str(x)
        url = "https://www.walmart.ca/en/baby/baby-bath-skin-care/baby-bath/N-8355/page-" + no
        response = requests.get(url=url, headers=headers, cookies=cookies)

        # for product url
        prd = re.compile(config['xpath']['prd_url'])
        id1 = response.content
        pid = prd.findall(id1)
        for x in range(0, len(pid)):
            pid[x] = "https://www.walmart.ca/" + pid[x][13:-1]
            Prdurl.append(pid[x])
            Page.append(no)
        # print(len(Prdurl))

        # for title
        tree = html.fromstring(response.content)
        title = tree.xpath(config['xpath']['title'])
        for x in range(0, len(title)):
            Title.append(title[x])
        # print (len(Title))

        # for image url
        img = tree.xpath(config['xpath']['img_url'])
        for x in range(0, len(img)):
            img[x] = "https:" + img[x]
            Image.append(img[x])
        # print (len(Image))
# to print all the data
def print_data(Title,Prdurl,Image):
    print ("PRODUCT TITLE:{}".format(Title))
    print ("PRODUCT URL:{}".format(Prdurl))
    print ("PRODUCT IMAGE:{}".format(Image))
# to save all the data in xlsx file
def csvfile(Total_prd):
    workbook = xlsxwriter.Workbook('walmart_listing.xlsx')
    worksheet = workbook.add_worksheet()
    row = 1
    column = 0
    head = 0
    worksheet.write(head, column, "PRODUCT URL")
    worksheet.write(head, column + 1, "PRODUCT PAGE")
    worksheet.write(head, column + 2, "PRODUCT TITLE")
    worksheet.write(head, column + 3, "PRODUCT IMAGE URL")
    # to write in xlsx
    for x in range(0, Total_prd):
        worksheet.write(row, column, Prdurl[x])
        worksheet.write(row, column + 1, Page[x])
        worksheet.write(row, column + 2, Title[x])
        worksheet.write(row, column + 3, Image[x])
        row += 1
    # close it then only file will save
    workbook.close()
    
    
url = "https://www.walmart.ca/en/baby/baby-bath-skin-care/baby-bath/N-8355"
Total_prd=path(url)
print_data(Title,Prdurl,Image)
csvfile(Total_prd)
