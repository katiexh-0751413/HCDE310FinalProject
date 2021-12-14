# HCDE310 Final Project

import urllib.parse, urllib.request, urllib.error, json, webbrowser

def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)

# Colors API
# baseurl: https://www.thecolorapi.com
color = {'hex':'cb997e', 'format':'json'}
paramstr = urllib.parse.urlencode(color)
baseurl = 'https://www.thecolorapi.com'
colorrequest = baseurl + '/id?' + paramstr
print("Color URL link: " + colorrequest)

def safe_get_color_url(url='https://www.thecolorapi.com/docs?ref=public-apis'):
    try:
        link = urllib.request.urlopen(url)
    except Exception as exception:
        print("The server couldn't fulfill the request.")
        print("Error code:  %s" % exception.code)

safe_get_color_url()

def get_color_data(hex='cb997e', format='json'):
    params = {'hex': hex, 'format': format}
    paramstr = urllib.parse.urlencode(params)
    requeststr = urllib.request.urlopen(baseurl + "/id?" + paramstr).read()
    data = json.loads(requeststr)
    return data

print()
print("COLOR DATA:")
print(pretty(get_color_data()))

# Makeup API
# baseurl: http://makeup-api.herokuapp.com/api/v1/products.json
makeup = {'product_type':'foundation', 'rating_greater_than':4}
paramstr = urllib.parse.urlencode(makeup)
baseurl = 'http://makeup-api.herokuapp.com/api/v1/products.json'
makeuprequest = baseurl + "?" + paramstr
print("Makeup URL link: " + makeuprequest)

def safe_get_makeup_url(url='http://makeup-api.herokuapp.com/?ref=public-apis'):
    try:
        link = urllib.request.urlopen(url)
    except Exception as exception:
        print("The server couldn't fulfill the request.")
        print("Error code:  %s" % exception.code)

safe_get_makeup_url()

def get_makeup_data(product_type='foundation', rating_greater_than=4):
    params = {'product_type': product_type, 'rating_greater_than': rating_greater_than}
    paramstr = urllib.parse.urlencode(params)
    requeststr = urllib.request.urlopen(baseurl + "?" + paramstr).read()
    data = json.loads(requeststr)
    return data

print()
print("MAKEUP DATA:")
print(pretty(get_makeup_data()))