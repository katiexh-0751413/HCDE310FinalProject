# HCDE310 Final Project

# Goals:
# Get hex number from color API using rgb values
# Use hex number found from color API to get closest shades of makeup

import urllib.parse, urllib.request, urllib.error, json, webbrowser

def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)

# Colors API
# baseurl: https://www.thecolorapi.com
#color = {'hex':'cb997e', 'format':'json'}

# Extracting data from the Colors API
# We are using the RGB numbers to convert to the hex value
color = {'rgb': 'rgb(203, 153, 126)', 'format': 'json'}
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

# A method to get data from the color API
# Defaults to using rgb values and formatting the data in json
def get_color_data(rgb='rgb(203, 153, 126', format='json'):
    params = {'rgb': rgb, 'format': format}
    paramstr = urllib.parse.urlencode(params)
    requeststr = urllib.request.urlopen(baseurl + "/id?" + paramstr).read()
    data = json.loads(requeststr)
    return data

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

# A method to get data from the makeup API
# Defaults to getting foundations that are rated greater than 4 stars
def get_makeup_data(product_type='foundation', rating_greater_than=4):
    params = {'product_type': product_type, 'rating_greater_than': rating_greater_than}
    paramstr = urllib.parse.urlencode(params)
    requeststr = urllib.request.urlopen(baseurl + "?" + paramstr).read()
    data = json.loads(requeststr)
    return data

makeup_data = get_makeup_data()

light_dict = []
medium_dict = []
dark_dict = []

for product in makeup_data:
    name = product['name']
    id = product['id']
    shade = product['product_colors'] # list of dictionaries of color name and hex value
    if (len(shade) >= 3):
        light_dict.append({'color_name': shade[0]['colour_name'],
                           'hex_value': shade[0]['hex_value'],
                           'image_link': product['image_link'],
                           'product_name': product['name'],
                           'color_link': "https://www.colorhexa.com/" + shade[0]['hex_value'][1:] + ".png"})

        medium_dict.append({'color_name': shade[int((len(shade) - 1) / 2)]['colour_name'],
                            'hex_value': shade[int((len(shade) - 1) / 2)]['hex_value'],
                            'image_link': product['image_link'],
                            'product_name': product['name'],
                            'color_link': "https://www.colorhexa.com/" + shade[int((len(shade) - 1) / 2)]['hex_value'][1:] + ".png"})

        dark_dict.append({'color_name': shade[len(shade) - 1]['colour_name'],
                          'hex_value': shade[len(shade) - 1]['hex_value'],
                          'image_link': product['image_link'],
                          'product_name': product['name'],
                          'color_link': "https://www.colorhexa.com/" + shade[len(shade) - 1]['hex_value'][1:] + ".png"})

if __name__ == '__main__':
    column = {"Light": {}, "Medium": {}, "Dark": {}}
    for product in light_dict:
        column["Light"][product["product_name"]] = product

    for product in medium_dict:
        column["Medium"][product["product_name"]] = product

    for product in dark_dict:
        column["Dark"][product["product_name"]] = product

    print("COLUMN:")
    #print(pretty(column))

    template_values = {"column": column}
    print(pretty(template_values))

    import jinja2, os

    JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
                                           extensions=['jinja2.ext.autoescape'],
                                           autoescape=True)

    template = JINJA_ENVIRONMENT.get_template('finalprojecttemplate.html')
    with open('makeupphotos.html', "w", encoding="utf-8") as file:
        file.write(template.render(template_values))