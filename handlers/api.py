import requests

url = "https://api.api-ninjas.com/v1/celebrity"
headers = {
    'X-Api-Key': 'CrDpVnmBQRYLCs6Qb5B4O0jT8LE89lgFhYF0ikwv'
}
ism = input("futbolchi: ")
params = {
    'name': ism
}
response = requests.get(url=url, headers=headers, params=params)
if response.status_code == 200:
    print(response.json())
    n = response.json()
else:
    print("Xatolik:", response.status_code, response.text)

full_name = n[0]["name"]
# pazitsiya = n[0]["position"]
# if pazitsiya == "F":
#     pazitsiya = "hujumchi"
boy = n[0]["height"]
print(full_name)
# print(pazitsiya)
sana=n[0]["birthday"]
print(sana)

print(boy)