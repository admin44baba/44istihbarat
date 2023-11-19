import requests
import urllib

def ip_bilgileri(ip):
    r = requests.get("https://api.ipinfo.io/{}/json".format(ip))
    data = r.json()
    print("**IP Bilgileri**")
    print("IP Adresi: {}".format(data["ip"]))
    print("Ülke: {}".format(data["country"]))
    print("Şehir: {}".format(data["city"]))
    print("İnternet Sağlayıcısı: {}".format(data["org"]))

def url_bilgileri(url):
    r = requests.get(url)
    ip = r.headers['X-Forwarded-For']
    try:
        location = requests.get("https://ipinfo.io/{}/json".format(ip)).json()["city"]
        print("**URL Bilgileri**")
        print("URL: {}".format(url))
        print("IP Adresi: {}".format(ip))
        print("Konum: {}".format(location))
    except Exception as e:
        print("Bir hata oluştu:", e)

def kisi_bilgileri(isim, soyisim):
    query = "{} {} site:linkedin.com".format(isim, soyisim)
    r = requests.get("https://www.google.com/search?q={}".format(query))
    urls = [urllib.parse.unquote(link.split("\"")[0]) for link in r.text.split("<a href=\"")[1:] if "linkedin.com" in link]
    print("**Kişi Bilgileri**")
    for url in urls:
        print(url)

print("**1=IP Bilgisi Bulma**")
print("**2=URL Bilgisi Bulma**")
print("**3=Kişi Bilgisi Bulma**")
secim = input("Seçiminiz: ")

if secim == "1":
    ip = input("IP Adresi Girin: ")
    ip_bilgileri(ip)
elif secim == "2":
    url = input("URL Girin: ")
    url_bilgileri(url)
elif secim == "3":
    isim = input("İsim Girin: ")
    soyisim = input("Soyisim Girin: ")
    kisi_bilgileri(isim, soyisim)
else:
    print("Geçersiz Seçim!")
