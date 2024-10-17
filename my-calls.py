# import sys
# sys.path.append('/Users/rislynraja/.local/pipx/venvs') 
# include above lines and modify to httpx installation location if it isnt recognized

import httpx

url = "https://supreme-space-palm-tree-5g46pvpjgxpj27wx7-5000.app.github.dev/"

# curl -d "text=Hello Rislyn&param2=value2" -X POST https://supreme-space-palm-tree-5g46pvpjgxpj27wx7-5000.app.github.dev/echo

response = httpx.get(url)
print(response.status_code)
print(response)

response = httpx.get(url)
print(response.status_code)
print(response.text)


myData = {
    "text": "Hello Rislyn",
    "param2": "Making a POST request",
    "body": "my own value"
}

# A POST RESPONSE TO THE API

response = httpx.post(url + "echo", data=myData) # correct data

print(response.status_code)
print(response)

authData = {
    "id": "rislyn_ferona.raja@uconn.edu",
    "token": "f99aa8b8573062e9802f4fc0807ae1cb"
}

response = httpx.post(url + "auth", data=authData) # correct id but incorrect token

print(response.status_code)
print(response.text)

wrongAuthData = {
    "id": "rislyn_ferona.raja@uconn.edu",
    "token": "hello"
}

response = httpx.post(url + "auth", data=wrongAuthData) # incorrect id and incorrect token

print(response.status_code)
print(response.text)

noIDAuthData = {
    "id": "me@uconn.edu",
    "token": "good bye"
}

response = httpx.post(url + "auth", data=noIDAuthData)

print(response.status_code)
print(response.text)