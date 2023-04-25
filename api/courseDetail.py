import requests

def get_course_detail(token, system_order):
    url = "https://xue.eoffcn.com/api/new/course/list?system_order={}".format(system_order)

    payload = {}
    headers = {
      'authority': 'xue.eoffcn.com',
      'accept': '*/*',
      'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
      'cookie': 'Hm_lvt_a6adf98bf5f7dd3d72872cf8b3535543=1682404898; Hm_lvt_a50bb98b162401cba9c89f1aa21a0b95=1682404898; Hm_lvt_3b55befee519827f19523fc1585b132c=1682404898; _ga=GA1.2.1220400741.1682404899; _gid=GA1.2.1127532502.1682404899; x-sso-gateway-web-token={}; Hm_lpvt_a6adf98bf5f7dd3d72872cf8b3535543=1682413749; Hm_lpvt_a50bb98b162401cba9c89f1aa21a0b95=1682413749; Hm_lpvt_3b55befee519827f19523fc1585b132c=1682413749'.format(token),
      'referer': 'https://xue.eoffcn.com/web/index.html',
      'sec-ch-ua': '"Chromium";v="112", "Microsoft Edge";v="112", "Not:A-Brand";v="99"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Windows"',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'same-origin',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58',
      'x-requested-with': 'XMLHttpRequest'
    }

    response = requests.request("GET", url, headers=headers, data=payload).json()

    return response