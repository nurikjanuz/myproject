# import requests
#
#
# def short_url(url):
#     r=requests.post('https://cleanuri.com/api/v1/shorten',
#                     data={
#                         'url':url,
#                     })
#     return r.json()['result_url']
#
# long_url = input("Enter long url: ")
# url1 = short_url(long_url)
# print("Your short link is: "+ url1)

import requests


def short_url(url):
    r=requests.post('https://cleanuri.com/api/v1/shorten',
                    data={
                        'url':url,
                    })
    return r.json()['result_url']

