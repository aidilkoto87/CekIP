import socket
import json
import requests

hostname = input("Domain website: ")
ip_address = socket.gethostbyname(hostname)

url = f'https://geolocation-db.com/json/{ip_address}&position=true'
response = requests.get(url)

if response.status_code == 200:
    geolocation = response.json()
    for key, value in geolocation.items():
        print(f"{key}: {value}")
else:
    print("Gagal mengambil data geolokasi.")