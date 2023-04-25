import requests

def login(username, password):
    url = "https://youzhi.eoffcn.com/ssogateway/v1/user/login"

    payload = "type=1&username={}&password={}&ref=https%3A%2F%2Fyouzhi.eoffcn.com%2F%3Fsf%3Dwxsyhyzx2%26memberPoster%3D1&ssoAppId=10040".format(username, password)
    headers = {
      'authority': 'youzhi.eoffcn.com',
      'accept': 'application/json, text/javascript, */*; q=0.01',
      'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
      'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
      'cookie': 'Hm_lvt_a6adf98bf5f7dd3d72872cf8b3535543=1682404898; Hm_lvt_a50bb98b162401cba9c89f1aa21a0b95=1682404898; Hm_lvt_3b55befee519827f19523fc1585b132c=1682404898; _ga=GA1.2.1220400741.1682404899; _gid=GA1.2.1127532502.1682404899; _gat=1; x-sso-gateway-web-token=RLvf3zlfKKg2e0Oh5eNBRcN3mjCDwvlFb-zaRYDaZ2dWydkGySxyINSe_Cithz263mJ1PUoopWi1yEaTOItB0JLtJ2YPFDiXLAP4eTM5VtY0-9u-77PQw9LQPP5ehRJsyjJZcU46O1ilovGzL0tuT-PPCkJm79peYJsp99d09NoyZfsvGUFuxlbhZ_74Sm9_; x-s-encode=c2lnbj0yMDU4Y2JmY2I0MWMzOGM0YjBhYmUxNGQ5MTNkZWE4YSZ0PTE2ODI0MTM3NDQ%253D; Hm_lpvt_a50bb98b162401cba9c89f1aa21a0b95=1682413744; Hm_lpvt_3b55befee519827f19523fc1585b132c=1682413744; Hm_lpvt_a6adf98bf5f7dd3d72872cf8b3535543=1682413744',
      'origin': 'https://youzhi.eoffcn.com',
      'referer': 'https://youzhi.eoffcn.com/?sf=wxsyhyzx2&memberPoster=1',
      'sec-ch-ua': '"Chromium";v="112", "Microsoft Edge";v="112", "Not:A-Brand";v="99"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Windows"',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'same-origin',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58',
      'x-requested-with': 'XMLHttpRequest',
      'x-s-encode': 'c2lnbj0yMDU4Y2JmY2I0MWMzOGM0YjBhYmUxNGQ5MTNkZWE4YSZ0PTE2ODI0MTM3NDQ%3D'
    }

    response = requests.request("POST", url, headers=headers, data=payload).json()
    if response:
        return response['data']['user']['token']
    else:
        print("账号或者密码错误")
