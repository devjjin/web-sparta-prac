import requests

r = requests.get('http://spartacodingclub.shop/sparta_api/seoulair')
rjson = r.json()

rows = rjson['RealtimeCityAir']['row']
print(rows)

for air in rows:
    msrste_nm = air['MSRSTE_NM']
    idex_mvl = air['IDEX_MVL']
    print(msrste_nm, idex_mvl)