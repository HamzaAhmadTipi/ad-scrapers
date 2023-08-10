#----imports:
import requests
import json
import csv
import re



#---function:
def get_google_ads(url):
    cookies = {
        'CONSENT': 'YES+srp.gws-20220110-0-RC3.en+FX+561',
        '_ga': 'GA1.1.1263383831.1681893408',
        'SID': 'ZQj6l0gn6JvEaldKezGlD9mNrHgTAtIMAeFgvY6C3nAprMBs1aEKCfHomvqpN5hNo3cvbg.',
        '__Secure-1PSID': 'ZQj6l0gn6JvEaldKezGlD9mNrHgTAtIMAeFgvY6C3nAprMBspwZ46Ak6lqcxZW3cgiC_BA.',
        '__Secure-3PSID': 'ZQj6l0gn6JvEaldKezGlD9mNrHgTAtIMAeFgvY6C3nAprMBsRWUWB82CPd1NGdVISGRE3w.',
        'HSID': 'Av8Qr9pqU5FIERw66',
        'SSID': 'AE6e-5D1u5g4Y7RKO',
        'APISID': 'jE9p4IwxCSA80n8T/AXT66fVaxlGhdTIhG',
        'SAPISID': 'rZ3mbIxP0VCgMmEa/AcphkhQR8NXJiyWUx',
        '__Secure-1PAPISID': 'rZ3mbIxP0VCgMmEa/AcphkhQR8NXJiyWUx',
        '__Secure-3PAPISID': 'rZ3mbIxP0VCgMmEa/AcphkhQR8NXJiyWUx',
        'SIDCC': 'APoG2W9YohHD5c5ikXJEBmPKbZ84QG2Yk-9uEz_kl1TImNn_Tmr-UIO1PIaLnUXAq4HgnjVTf0A',
        '__Secure-1PSIDCC': 'APoG2W8fzvH4ER82BnADpjrj6vfhVa7ILmQSY2MWVSMzdB8gWnGf4syhO9LO4PFRtHBz4kobQJ4',
        '__Secure-3PSIDCC': 'APoG2W_Gg9sOt9CEtAlBM4P5Dm6CTi1zzcaPPmr6tjEfyW99HEZdHNXLXfcgb27QHv6lZivxaC8',
        'AEC': 'Ad49MVF1wFc1Ui_8wThmEEKoWxw299_ySK5OfQ1p8cSRejh1JJJZtGfeIP8',
        'NID': '511=ssDwc20jtRwdzQZ-h-ap7ETvHex3nXW9rmWHa_eXNq_4WbKWhkebkalHcykXyuQGIf0F3R7ALnsGO13hCAk_Y-40LVzShIvuNJG62fywghgOXbooTf-RFON6QLhHqvCnn10IFFO0Nxfvt6ELW8nscG-aWhSZW1iwM1LDRKOZFMVVinOmXXBsQVqlOqDDFvVwYnjHsbzqeP-dDXYXcLfNz2jP0_e58p4uU2nkMJ4wsN8dyszQZmn1pV1Gomzv-892he_hfG66ypMTRT_GKNTOaKpcNnAXMzdCRxQZEnQTlqlARfKgwJ2dh7VSWyA60tZHdOApzVzjRkdqAISGBZgj2Tw6uWX9',
        '1P_JAR': '2023-08-04-00',
        '_ga_YMYR0M0J94': 'GS1.1.1691109075.4.1.1691109101.0.0.0',
    }

    headers = {
        'authority': 'adstransparency.google.com',
        'accept': '*/*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'CONSENT=YES+srp.gws-20220110-0-RC3.en+FX+561; _ga=GA1.1.1263383831.1681893408; SID=ZQj6l0gn6JvEaldKezGlD9mNrHgTAtIMAeFgvY6C3nAprMBs1aEKCfHomvqpN5hNo3cvbg.; __Secure-1PSID=ZQj6l0gn6JvEaldKezGlD9mNrHgTAtIMAeFgvY6C3nAprMBspwZ46Ak6lqcxZW3cgiC_BA.; __Secure-3PSID=ZQj6l0gn6JvEaldKezGlD9mNrHgTAtIMAeFgvY6C3nAprMBsRWUWB82CPd1NGdVISGRE3w.; HSID=Av8Qr9pqU5FIERw66; SSID=AE6e-5D1u5g4Y7RKO; APISID=jE9p4IwxCSA80n8T/AXT66fVaxlGhdTIhG; SAPISID=rZ3mbIxP0VCgMmEa/AcphkhQR8NXJiyWUx; __Secure-1PAPISID=rZ3mbIxP0VCgMmEa/AcphkhQR8NXJiyWUx; __Secure-3PAPISID=rZ3mbIxP0VCgMmEa/AcphkhQR8NXJiyWUx; SIDCC=APoG2W9YohHD5c5ikXJEBmPKbZ84QG2Yk-9uEz_kl1TImNn_Tmr-UIO1PIaLnUXAq4HgnjVTf0A; __Secure-1PSIDCC=APoG2W8fzvH4ER82BnADpjrj6vfhVa7ILmQSY2MWVSMzdB8gWnGf4syhO9LO4PFRtHBz4kobQJ4; __Secure-3PSIDCC=APoG2W_Gg9sOt9CEtAlBM4P5Dm6CTi1zzcaPPmr6tjEfyW99HEZdHNXLXfcgb27QHv6lZivxaC8; AEC=Ad49MVF1wFc1Ui_8wThmEEKoWxw299_ySK5OfQ1p8cSRejh1JJJZtGfeIP8; NID=511=ssDwc20jtRwdzQZ-h-ap7ETvHex3nXW9rmWHa_eXNq_4WbKWhkebkalHcykXyuQGIf0F3R7ALnsGO13hCAk_Y-40LVzShIvuNJG62fywghgOXbooTf-RFON6QLhHqvCnn10IFFO0Nxfvt6ELW8nscG-aWhSZW1iwM1LDRKOZFMVVinOmXXBsQVqlOqDDFvVwYnjHsbzqeP-dDXYXcLfNz2jP0_e58p4uU2nkMJ4wsN8dyszQZmn1pV1Gomzv-892he_hfG66ypMTRT_GKNTOaKpcNnAXMzdCRxQZEnQTlqlARfKgwJ2dh7VSWyA60tZHdOApzVzjRkdqAISGBZgj2Tw6uWX9; 1P_JAR=2023-08-04-00; _ga_YMYR0M0J94=GS1.1.1691109075.4.1.1691109101.0.0.0',
        'origin': 'https://adstransparency.google.com',
        'referer': url,
        'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
        'x-client-data': 'CIu2yQEIpbbJAQipncoBCJ7bygEIlKHLAQic/swBCIWTzQEIhaDNAQjCsc0BCNq0zQEI3L3NAQi7vs0BCN/EzQEI7sTNAQimxc0BCPTFzQEIlcjNAQ==',
        'x-framework-xsrf-token': '',
        'x-same-domain': '1',
    }

    params = {
        'authuser': '',
    }

    data = {
        'f.req': '{"2":40,"3":{"12":{"1":"","2":true},"13":{"1":["AR13163360354559852545"]}},"7":{"1":1,"2":0,"3":2826}}',
    }

    response = requests.post(
        'https://adstransparency.google.com/anji/_/rpc/SearchService/SearchCreatives',
        params=params,
        cookies=cookies,
        headers=headers,
        data=data,
    )

    json_data = response.json()
    ad_metadata_list = json_data.get('1', [])
    advertisements = []

    for ad_metadata in ad_metadata_list:
        advertisement = {}
        advertisement['ID'] = len(advertisements)  # Counting up from 0
        advertisement['Brand Name'] = ad_metadata.get('12', '')
        ad_image_html = ad_metadata['3']['3']['2'] if '3' in ad_metadata else ''
        advertisement['Ad Image'] = re.findall(r'<img src="([^"]+)"', ad_image_html)[0] if ad_image_html else ''
        advertisement['Brand ID'] = ad_metadata.get('1', '')
        advertisement['Ad ID'] = ad_metadata.get('2', '')
        advertisement['Ad Width'] = ad_metadata['3']['3']['2'].split('width="')[1].split('"')[0] if '3' in ad_metadata else ''
        advertisement['Ad Height'] = ad_metadata['3']['3']['2'].split('height="')[1].split('"')[0] if '3' in ad_metadata else ''
        advertisements.append(advertisement)

    # Save the data to a CSV file
    csv_file = 'google-ads.csv'

    with open(csv_file, mode='w', newline='') as file:
        fieldnames = ['ID', 'Brand Name', 'Ad Image', 'Brand ID', 'Ad ID', 'Ad Width', 'Ad Height']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for ad in advertisements:
            writer.writerow(ad)
    print(f"ads saved to {csv_file}.")



# run 
if __name__ == "__main__":
    url = input('google ad transparency URL: ')
    get_google_ads(url)
