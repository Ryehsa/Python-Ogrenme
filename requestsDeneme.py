import requests
response =requests.get('https://sachane.com/',stream=True)
print(response.status_code)
#print(response.content)


# gelen sonucu dosyaya yazdırma
with open ('Result.txt','wb') as result_file:
    result_file.write(response.content)

