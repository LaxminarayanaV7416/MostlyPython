# lets talk about requests library in python
# this library is used to hit API's and get the relevant information
# if we want parse websites probably we can use BeautifulSoup (bs4) or requests-html

# installation of reuqests library in python
###### $ pip install requests

#lets understand http status codes
# 1. 200's -> sucess codes
# 2. 300's -> redirects
# 3. 400's -> client errors
# 4. 500's -> Server errors

# extra note for testing use website ==> http://httpbin.org/

import requests

url = 'https://xkcd.com/353/'
req = requests.get(url)

print(req) #prints the response code here as <Response [200]>

# to see the methods use dir(req) to get to know them, leys see most common
req.text # outputs text if we get any text response from url, in our case we will get html code
req.content # used to get bytes , usually used for images lets see and example
req.status_code # outputs the status code 200
req.ok # outputs True if http code is less than 400 else outputs false
req.headers # outputs the headers as dict , for eg., {'Content-Type':'image/png',etc.,}
req.json() # if we get any json response,it will convert it to python dictionary.
req.url # prints the url we are trying to hit, chanegs when we use params as keyword argument since it adds the data to url
req.raw # used to get raw information and make sure stream=True in requests keyword arguments
req.cookies # to get cookies as dictionary 

image_url = 'https://images.pexels.com/photos/1047051/pexels-photo-1047051.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940'
req = requests.get(image_url)

# this is how we save images to local storage

with open('image.jpg',mode='wb') as img:
    img.write(req.content)


#########################
# lets start using real apis so we are going to use website called http://httpbin.org/ for our testign purpose
import requests

payload = {'Name':'Laxminarayana vadnala','position':'Machine Learning Engineer'}
request = requests.get('https://httpbin.org/get', params=payload)

#requests.get keyword arguments 
# 1. params => {} basically when we hit the get requests we send data in url itself so params 
# do the addition of payload to url we can check this by printing req.url
# 2. auth => usually used for authentication used as auth=('username','password')
# 3. headers => {} if we want to send any custom headers to the api get request
# 4. stream => bool input True / False rarely used for raw response 
# 5. cookies  => {} to send cookies to the api

print(request.json())

#lets see the POST requests
payload = {'key1': 'value1', 'key2': 'value2'}
files = {'file': ('report.xls', open('report.xls', 'rb'), 'application/vnd.ms-excel', {'Expires': '0'})}
request = requests.post('https://httpbin.org/post', json = payload,files = files) # we are tryig to send the form data using 'data' as keyword argument

#requests.post keyword arguments
# 1. data => to send the form data to api
# 2. json => to send form data in form json to API
# 3. files => {} to send multipart encoded files to api

print(request.json())

# Now lets see some basic authentication using requests library

auth_data = ('lucky','vadnala')
request = requests.get('https://httpbin.org/basic-auth/lucky/vadnala', auth = auth_data)

print(request.json())