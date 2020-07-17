# -*- coding: utf-8 -*-
"""
  █████▒█    ██  ▄████▄   ██ ▄█▀       ██████╗ ██╗   ██╗ ██████╗
▓██   ▒ ██  ▓██▒▒██▀ ▀█   ██▄█▒        ██╔══██╗██║   ██║██╔════╝
▒████ ░▓██  ▒██░▒▓█    ▄ ▓███▄░        ██████╔╝██║   ██║██║  ███╗
░▓█▒  ░▓▓█  ░██░▒▓▓▄ ▄██▒▓██ █▄        ██╔══██╗██║   ██║██║   ██║
░▒█░   ▒▒█████▓ ▒ ▓███▀ ░▒██▒ █▄       ██████╔╝╚██████╔╝╚██████╔╝
 ▒ ░   ░▒▓▒ ▒ ▒ ░ ░▒ ▒  ░▒ ▒▒ ▓▒       ╚═════╝  ╚═════╝  ╚═════╝
 ░     ░░▒░ ░ ░   ░  ▒   ░ ░▒ ▒░
 ░ ░    ░░░ ░ ░ ░        ░ ░░ ░
          ░     ░ ░      ░  ░
-------------------------------------------------
   File Name：     主播小时榜
   Description :
   Author :       92159
   date：          2020/7/2
-------------------------------------------------
   Change Activity:
                   2020/7/2:
-------------------------------------------------
"""
__author__ = '92159'
import requests
import time
from douyin.fuck_douyin import get_X_gorgon


def get_hour_list():
    _rticket = int(str(time.time() * 1000).split('.')[0])
    ts = str(int(_rticket / 1000))
    # url = "https://webcast3-normal-c-lf.amemv.com/webcast/ranklist/hour/?hour_info=0&room_id=6844771268063922952&rank_type=12&sec_anchor_id=MS4wLjABAAAA9K1pRalDsSsOXTR95ld3XykADjnUBBJ1NI_UOvxJ5dg&sec_user_id=MS4wLjABAAAARMQhSF0D_1Oy5bgTKs9jXj0zIPU2aOj7bqiH4-L0HYs&webcast_sdk_version=1540&webcast_language=zh&webcast_locale=zh_CN&os_api=22&device_type=HD1910&ssmix=a&manifest_version_code=110301&dpi=192&uuid=860274377317243&app_name=aweme&version_name=11.3.0&ts=1593672769&cpu_support64=false&app_type=normal&ac=wifi&host_abi=armeabi&update_version_code=11309900&channel=aweGW&_rticket=1593657636336&device_platform=android&iid=1433413949870696&version_code=110300&mac_address=3e%3A1f%3A51%3A55%3A13%3Ad6&cdid=6f30fdf9-94cd-472f-91ee-3180fa0838b9&openudid=64685146805e7f4c&device_id=1609335808985086&resolution=1280*720&os_version=5.1.1&language=zh&device_brand=OnePlus&aid=1128&mcc_mnc=46003"
    url = f"https://webcast.amemv.com/webcast/ranklist/hour/?" \
          f"hour_info=0&room_id=6844771268063922952&rank_type=12&" \
          f"sec_anchor_id=MS4wLjABAAAA9K1pRalDsSsOXTR95ld3XykADjnUBBJ1NI_UOvxJ5dg" \
          f"&ts={ts}&_rticket={_rticket}&aid=1128"
    cookies = 'd_ticket=c90cba17563014f6da47c5789a2d3b1f84b18; odin_tt=c48db2fdad46bd23316ac172bba5cba20453c185e08b0b851c49349f972649fbd1bc97ff0c070dfa26c31ce8019c063f09692d857b83ff4ac581eb50dc0f8275; sid_guard=38e5a2d2d1b832fde4667e5bea5a1367%7C1590736940%7C5184000%7CTue%2C+28-Jul-2020+07%3A22%3A20+GMT; uid_tt=565d172429fef00f6df5a5cbf82a97dc; sid_tt=38e5a2d2d1b832fde4667e5bea5a1367; sessionid=38e5a2d2d1b832fde4667e5bea5a1367; install_id=1028786593992525; ttreq=1$acb357c7964511c40cf4169918aca5fcbb22a7e8'
    gorgon = get_X_gorgon(url, cookies, ts)
    header = {
        "Accept-Encoding": "gzip",
        "sdk-version": "1",
        "Cookie": cookies,
        # "x-tt-token": "00e06ecb4467b94336433a1c29a37cb3fc041fe397f3b8dbebb03567af5d2da51f72b725934a9b5ae1d8ae92602c1c410610d3e5e5d1907ae4fee4c2d3ef386a6596c170dae6475de311c442d73c20cac916a-1.0.0",
        "X-Gorgon": gorgon,
        "X-Khronos": ts,
        "Host": "webcast.amemv.com",
        "Connection": "Keep-Alive",
        "User-Agent": "okhttp/3.10.0.1"
    }
    try:
        res = requests.get(url, headers=header)
    except Exception as e:
        print(e)
    else:
        top_list = []
        begin_time = res.json().get('data').get('begin_time')
        res = res.json().get('data').get('ranks')
        for i in res:
            # 当前小时收礼数
            gap_description = i.get('gap_description')
            # 当前具体收礼数目
            score = i.get('score')
            # 当前排名
            rank = i.get('rank')
            # 主播昵称
            nickname = i.get('user').get('nickname')
            # 主播加密id
            sec_uid = i.get('user').get('sec_uid')
            # 主播抖音id
            display_id = i.get('user').get('display_id')
            # 主播短名称
            short_id = i.get('user').get('short_id')
            # 主播头像
            user_head = i.get('user').get('avatar_thumb').get('url_list')[0]
            # 主播本场房间号
            room_ids_str = i.get('user').get('own_room')
            result = {
                'gap_description': gap_description,
                'score': score,
                'rank': rank,
                'nickname': nickname,
                'sec_uid': sec_uid,
                'display_id': display_id,
                'short_id': short_id,
                'user_head': user_head,
                'room_ids_str': room_ids_str
            }
            top_list.append(result)
        result = {'begin_time': begin_time, 'top_list': top_list}
        return result


if __name__ == '__main__':
    result = get_hour_list()
    print(result)
