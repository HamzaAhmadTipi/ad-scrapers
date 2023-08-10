import requests
import json
import csv
from datetime import datetime

def get_tiktok_ads(query):
    cookies = {
        '_ttp': '2BAsnYUy5nAV76l5j0hLE2EJ7jd',
        '_abck': 'CFC28E3AFE39323F446594F977D95A3A~-1~YAAQJXP8Pvd02IOEAQAA+9KNnQh5TNiEF5hnvxp2xy6x807buyBNUX9rI1fR5kB0vgUgiODZ3Gf4hZ/N+l06Y6GPCwPFuaLiwGBL9uU6xYcmuqM6AAYCkWDV2XWVdQEUe7qTJPexUfGJyZHY9VT5y/LFVYPUkanJOBlCLo4OL+v8cxZqo951DKHj0Ulx9z199gOfTuuKBgUU/NQzMgrv9dIE1Sa0kZ+Hj3JqHoNULw5BP0J6fNUxXpaEyLXQAN7zKVtJgEECz5j4IHsazgw+Y3GzbY+mzvanuVB5HNZPpmqA22QaKfegMjlpPCCx9b2veIwtEzqON4/Gjs+HsR3/vvhHkinMGgCnJ4ajXPQ5dS6wU9VUOz3JyQXz0a6RVMR0hzd3FdKPPNgROQ==~-1~-1~-1',
        'passport_csrf_token': '99da5b0d4ae5a9b3ea2e3d4f3024ace6',
        'passport_csrf_token_default': '99da5b0d4ae5a9b3ea2e3d4f3024ace6',
        'tt_chain_token': 'JDK40pE6f2oMl1mVL+lKRg==',
        'cookie-consent': '{%22ga%22:false%2C%22af%22:false%2C%22fbp%22:false%2C%22lip%22:false%2C%22bing%22:false%2C%22ttads%22:false%2C%22reddit%22:false%2C%22criteo%22:false%2C%22version%22:%22v9%22}',
        'cmpl_token': 'AgQQAPOYF-RO0rNY4imM9p0__qAOYudMv5kTYM2R2g',
        'passport_auth_status': '1818e34c919b04bd9840270839961957%2C',
        'passport_auth_status_ss': '1818e34c919b04bd9840270839961957%2C',
        'sid_guard': '8fec7348cc43d87c6351df2fddfeb778%7C1690969841%7C15551999%7CMon%2C+29-Jan-2024+09%3A50%3A40+GMT',
        'uid_tt': 'b7e3baa1e686a11a717f920a665d11178837f1fed75284e008b7129072e9a87d',
        'uid_tt_ss': 'b7e3baa1e686a11a717f920a665d11178837f1fed75284e008b7129072e9a87d',
        'sid_tt': '8fec7348cc43d87c6351df2fddfeb778',
        'sessionid': '8fec7348cc43d87c6351df2fddfeb778',
        'sessionid_ss': '8fec7348cc43d87c6351df2fddfeb778',
        'sid_ucp_v1': '1.0.0-KDNiNDQxZjY2ZmY4NzFhMzU2MjgwOGY4NjQ4NzNhMmNjZjVmMWY5MzYKHwiGiJGm4JGDs2MQ8c2opgYYswsgDDC7mZibBjgIQBIQAxoIdXNlYXN0MmEiIDhmZWM3MzQ4Y2M0M2Q4N2M2MzUxZGYyZmRkZmViNzc4',
        'ssid_ucp_v1': '1.0.0-KDNiNDQxZjY2ZmY4NzFhMzU2MjgwOGY4NjQ4NzNhMmNjZjVmMWY5MzYKHwiGiJGm4JGDs2MQ8c2opgYYswsgDDC7mZibBjgIQBIQAxoIdXNlYXN0MmEiIDhmZWM3MzQ4Y2M0M2Q4N2M2MzUxZGYyZmRkZmViNzc4',
        'store-idc': 'useast2a',
        'store-country-code': 'gb',
        'store-country-code-src': 'uid',
        'tt-target-idc': 'useast2a',
        'tt-target-idc-sign': 'kVL31zcRRbRsdx_QuLylsRDpuKrMT8eBGQXyS3iOrOgcGJIhhDXzigiCo5V-K7vKfPUay5iMBgxDsIH1yCJBdV_SgU5xWfq3JFfRoKDGp5P0tmA3IBFu7FcGD_THPJQQW-7ZmYMTB7h1omn0-4TTIr2ENXi_Yu2mh46Ink0Jym_szh9zQo1npGOXjb7zAaDNGTSUhkVn6Q29nGDgoZ3rH2H5aFPcFmo4XIauQpgb3YVjuezRVCvc6sJ1PtOXq_jEctPnHUWNZWZ0oIsFDuOlxW2h4uSgCsUFclaKcnis4Biyx-tEXwd6_CzlydB0Ukja8a1QTTgmbMrSnuqofokUCmqWb5nLPITRSPu9VF7EyVqKRFVReDeF4p1_GL_20l8ieuq8nYquI-zyfl-S3coHshhQLDEzQLtr8Eg6DzL8LhWYwBruVhZPrS_1-QTvTSaOiWl9-ihDlv87BLvd-7ej5_srMCVDP8o6Pq5dRzIvih0fyMjGvgbK7XApefME4YNN',
        'odin_tt': '114ff32b83c7eb39ec9943493d1ebe8433c1262636ac04c1971debf8724601a627ef56959db63ed9e3a07af4d4d142cd0dcacf75b232bc04522557ac426b0a10',
        'from_way': 'paid',
        'tta_attr_id': '0.1691111753.7263269673884450817',
        'tta_attr_id_mirror': '0.1691111753.7263269673884450817',
        'ttwid': '1%7CjpOxUqbgu_jNlgKM62GnRDCPSKwFwdvosdy4k9lss-w%7C1691111771%7C5032731932628736b27e80d410c95927a1592ea7fe00a8af2a98dbb7965f18b5',
        'msToken': 'wqix3DybgxJzXNjiNCaW6UWZSZV3PTjODHbbRl5GuTbmfmV_tOJWQJR6vQdZgG-b8COwnjTtw38jSPTvnWg-bKULNXD8e0iiTXoWAYQB6Y1BmMYQ8puX',
    }

    headers = {
        'authority': 'library.tiktok.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/json',
        # 'cookie': '_ttp=2BAsnYUy5nAV76l5j0hLE2EJ7jd; _abck=CFC28E3AFE39323F446594F977D95A3A~-1~YAAQJXP8Pvd02IOEAQAA+9KNnQh5TNiEF5hnvxp2xy6x807buyBNUX9rI1fR5kB0vgUgiODZ3Gf4hZ/N+l06Y6GPCwPFuaLiwGBL9uU6xYcmuqM6AAYCkWDV2XWVdQEUe7qTJPexUfGJyZHY9VT5y/LFVYPUkanJOBlCLo4OL+v8cxZqo951DKHj0Ulx9z199gOfTuuKBgUU/NQzMgrv9dIE1Sa0kZ+Hj3JqHoNULw5BP0J6fNUxXpaEyLXQAN7zKVtJgEECz5j4IHsazgw+Y3GzbY+mzvanuVB5HNZPpmqA22QaKfegMjlpPCCx9b2veIwtEzqON4/Gjs+HsR3/vvhHkinMGgCnJ4ajXPQ5dS6wU9VUOz3JyQXz0a6RVMR0hzd3FdKPPNgROQ==~-1~-1~-1; passport_csrf_token=99da5b0d4ae5a9b3ea2e3d4f3024ace6; passport_csrf_token_default=99da5b0d4ae5a9b3ea2e3d4f3024ace6; tt_chain_token=JDK40pE6f2oMl1mVL+lKRg==; cookie-consent={%22ga%22:false%2C%22af%22:false%2C%22fbp%22:false%2C%22lip%22:false%2C%22bing%22:false%2C%22ttads%22:false%2C%22reddit%22:false%2C%22criteo%22:false%2C%22version%22:%22v9%22}; cmpl_token=AgQQAPOYF-RO0rNY4imM9p0__qAOYudMv5kTYM2R2g; passport_auth_status=1818e34c919b04bd9840270839961957%2C; passport_auth_status_ss=1818e34c919b04bd9840270839961957%2C; sid_guard=8fec7348cc43d87c6351df2fddfeb778%7C1690969841%7C15551999%7CMon%2C+29-Jan-2024+09%3A50%3A40+GMT; uid_tt=b7e3baa1e686a11a717f920a665d11178837f1fed75284e008b7129072e9a87d; uid_tt_ss=b7e3baa1e686a11a717f920a665d11178837f1fed75284e008b7129072e9a87d; sid_tt=8fec7348cc43d87c6351df2fddfeb778; sessionid=8fec7348cc43d87c6351df2fddfeb778; sessionid_ss=8fec7348cc43d87c6351df2fddfeb778; sid_ucp_v1=1.0.0-KDNiNDQxZjY2ZmY4NzFhMzU2MjgwOGY4NjQ4NzNhMmNjZjVmMWY5MzYKHwiGiJGm4JGDs2MQ8c2opgYYswsgDDC7mZibBjgIQBIQAxoIdXNlYXN0MmEiIDhmZWM3MzQ4Y2M0M2Q4N2M2MzUxZGYyZmRkZmViNzc4; ssid_ucp_v1=1.0.0-KDNiNDQxZjY2ZmY4NzFhMzU2MjgwOGY4NjQ4NzNhMmNjZjVmMWY5MzYKHwiGiJGm4JGDs2MQ8c2opgYYswsgDDC7mZibBjgIQBIQAxoIdXNlYXN0MmEiIDhmZWM3MzQ4Y2M0M2Q4N2M2MzUxZGYyZmRkZmViNzc4; store-idc=useast2a; store-country-code=gb; store-country-code-src=uid; tt-target-idc=useast2a; tt-target-idc-sign=kVL31zcRRbRsdx_QuLylsRDpuKrMT8eBGQXyS3iOrOgcGJIhhDXzigiCo5V-K7vKfPUay5iMBgxDsIH1yCJBdV_SgU5xWfq3JFfRoKDGp5P0tmA3IBFu7FcGD_THPJQQW-7ZmYMTB7h1omn0-4TTIr2ENXi_Yu2mh46Ink0Jym_szh9zQo1npGOXjb7zAaDNGTSUhkVn6Q29nGDgoZ3rH2H5aFPcFmo4XIauQpgb3YVjuezRVCvc6sJ1PtOXq_jEctPnHUWNZWZ0oIsFDuOlxW2h4uSgCsUFclaKcnis4Biyx-tEXwd6_CzlydB0Ukja8a1QTTgmbMrSnuqofokUCmqWb5nLPITRSPu9VF7EyVqKRFVReDeF4p1_GL_20l8ieuq8nYquI-zyfl-S3coHshhQLDEzQLtr8Eg6DzL8LhWYwBruVhZPrS_1-QTvTSaOiWl9-ihDlv87BLvd-7ej5_srMCVDP8o6Pq5dRzIvih0fyMjGvgbK7XApefME4YNN; odin_tt=114ff32b83c7eb39ec9943493d1ebe8433c1262636ac04c1971debf8724601a627ef56959db63ed9e3a07af4d4d142cd0dcacf75b232bc04522557ac426b0a10; from_way=paid; tta_attr_id=0.1691111753.7263269673884450817; tta_attr_id_mirror=0.1691111753.7263269673884450817; ttwid=1%7CjpOxUqbgu_jNlgKM62GnRDCPSKwFwdvosdy4k9lss-w%7C1691111771%7C5032731932628736b27e80d410c95927a1592ea7fe00a8af2a98dbb7965f18b5; msToken=wqix3DybgxJzXNjiNCaW6UWZSZV3PTjODHbbRl5GuTbmfmV_tOJWQJR6vQdZgG-b8COwnjTtw38jSPTvnWg-bKULNXD8e0iiTXoWAYQB6Y1BmMYQ8puX',
        'origin': 'https://library.tiktok.com',
        'referer': 'https://library.tiktok.com/ads?region=GB&start_time=1664578800000&end_time=1691112354452&adv_name=coca cola&adv_biz_ids=&query_type=1&sort_type=impression,desc',
        'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    }

    params = {
        'region': 'GB',
        'type': '1',
        'start_time': '1664578800',
        'end_time': '1691112354',
    }

    json_data = {
        'query': query,
        'query_type': '1',
        'adv_biz_ids': '',
        'order': 'impression,desc',
        'offset': 0,
        'search_id': '',
        'limit': 36,
    }

    response = requests.post('https://library.tiktok.com/api/v1/search', params=params, cookies=cookies, headers=headers, json=json_data)
    json_response = response.json()


    # Extracting the adverts from the 'data' array
    adverts = json_response["data"]

    # Function to convert Unix timestamp to normal date string
    def unix_timestamp_to_date(timestamp):
        return datetime.utcfromtimestamp(timestamp / 1000).strftime('%Y-%m-%d %H:%M:%S')

    # CSV file name
    csv_file = "tiktok_ads.csv"

    # Function to write a single advert to the CSV file
    def write_advert_to_csv(csv_writer, advert):
        csv_writer.writerow([
            advert['id'],
            advert['name'],
            unix_timestamp_to_date(advert['first_shown_date']),
            unix_timestamp_to_date(advert['last_shown_date']),
            advert['estimated_audience'],
            ",".join(advert['image_urls']),  # Convert list to comma-separated string
            ",".join([video['video_url'] for video in advert['videos']]),  # Convert list of video URLs to comma-separated string
            ",".join([video['cover_img'] for video in advert['videos']]),  # Convert list of cover images to comma-separated string
        ])

    # Writing data to CSV file
    with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        
        # Writing header row
        csv_writer.writerow([
            "ID", "Name","First Shown Date", "Last Shown Date",
            "Estimated Audience", "Image URLs", "Video URLs", "Cover Images"
        ])
        
        # Writing data rows
        for advert in adverts:
            write_advert_to_csv(csv_writer, advert)

    print("Data has been written to", csv_file)



if __name__ == "__main__":
    query = input("search brand for tiktok ads: ")
    get_tiktok_ads(query)
    
    
