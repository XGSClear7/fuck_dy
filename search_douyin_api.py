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
   File Name：     search_douyin_mod
   Description :
   Author :       92159
   date：          2020/7/17
-------------------------------------------------
   Change Activity:
                   2020/7/17:
-------------------------------------------------
"""
__author__ = '92159'
import time
import requests
from fuck_douyin import get_X_gorgon, get_X_SS_STUB


COOKIES = ''


def search(dy_id):
    """
    传入要查询的抖音ID,返回查询的账户信息,COOKIES使用多个可以有效保证搜索接口的可用性,搜索接口失效一般只需要更改cookie即可.
    """
    # 抖音的两个时间戳参数
    _rticket = int(str(time.time() * 1000).split('.')[0])
    ts = str(int(_rticket / 1000))

    # 搜索接口的URL
    URL = f'https://aweme.snssdk.com/aweme/v1/discover/search/?os_api=22&device_type=HD1910&ssmix=a&manifest_version_code=100901&dpi=192&uuid=861617543160856&app_name=aweme&version_name=10.9.0&ts={str(ts)}&app_type=normal&ac=wifi&host_abi=armeabi-v7a&update_version_code=10909900&channel=aweGW&_rticket={str(_rticket)}&device_platform=android&iid=2119504168242088&version_code=100900&cdid=1829f767-6813-4b81-b158-653e8f10ae66&openudid=8ba083cc751ea801&device_id=2436163515723038&resolution=720*1280&os_version=5.1.1&language=zh&device_brand=OnePlus&aid=1128&mcc_mnc=46003'
    # 账号COOKIES
    # 请求参数
    POST_DATA = {
        'cursor': 0,  # 请求页数
        'keyword': dy_id,  # 请求参数
        'count': 10,  # 数量
        'hot_search': 0,  # 热搜数量
        'is_pull_refresh': 0,
        'type': 1,
        'search_source': '',
        'search_id': '',
        'query_correct_type': 1
    }
    # url参数
    URL_PARAMS = f'cursor=0&keyword={dy_id}&count=10&type=1&is_pull_refresh=0&hot_search=0&search_source=&search_id=&query_correct_type=1'
    # 获取STUB
    X_SS_STUB = get_X_SS_STUB(URL_PARAMS)
    # 获取gorgon
    X_gorgon = get_X_gorgon(URL, COOKIES, ts)
    # 构建请求头
    HEADER = {
        'X-SS-STUB': X_SS_STUB,
        'Accept-Encoding': 'gzip',
        'X-SS-REQ-TICKET': str(_rticket),
        'sdk-version': '1',
        'Cookie': COOKIES,
        # 'x-tt-token': '0038e5a2d2d1b832fde4667e5bea5a1367afa4666acd0187c159bcfcfd843ef126165db8251a4a9f83b566192380d6ebab15',
        'X-Gorgon': X_gorgon,
        'X-Khronos': ts,
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Content-Length': '138',
        'Host': 'aweme-hl.snssdk.com',
        'Connection': 'Keep-Alive',
        'User-Agent': 'okhttp/3.10.0.1',
    }
    # 构建请求
    try:
        res = requests.post(url=URL, data=POST_DATA, headers=HEADER).json()
        data = res.get('user_list')
    except Exception as e:
        print(e)
        return {'status': 500, 'data': None}
    else:
        if data:
            user_list = []
            for i in data:
                # print(i)
                i = i['user_info']
                uid = i.get('uid')
                short_id = i.get('short_id')
                nickname = i.get('nickname')
                signature = i.get('signature')
                sec_uid = i.get('sec_uid')
                unique_id = i.get('unique_id')
                birthday = i.get('birthday')  # 生日
                # is_verified = i.get('is_verified')  # 账号验证
                aweme_count = i.get('aweme_count')  # 作品数
                following_count = i.get('following_count')  # 关注人数
                follower_count = i.get('follower_count')  # 粉丝数
                favoriting_count = i.get('favoriting_count')  # 喜欢
                total_favorited = i.get('total_favorited')  # 点赞数
                # constellation = i.get('constellation')  # 星座
                location = i.get('location')  # 位置
                # room_id = i.get('room_id')
                # live_verify = i.get('live_verify')  # 直播验证
                school_name = i.get('school_name')  # 学校名称
                region = i.get('region')  # 注册地
                # account_region = i.get('account_region')    # 注册数量
                unique_id_modify_time = i.get('unique_id_modify_time')  # 抖音号验证时间
                avatar_uri = i.get('avatar_uri')
                share_qrcode_uri = i.get('share_qrcode_uri')  # 二维码uri
                try:
                    nick_img = i.get('avatar_larger').get('url_list')[0]
                except:
                    pass
                    nick_img = ''
                result = {
                    'uid': uid,
                    'short_id': short_id,
                    'unique_id': unique_id,
                    'sec_uid': sec_uid,
                    'nickname': nickname,
                    'signature': signature,
                    'birthday': birthday,
                    # 'is_verified': is_verified,
                    'aweme_count': aweme_count,
                    'following_count': following_count,
                    'follower_count': follower_count,
                    'favoriting_count': favoriting_count,
                    'total_favorited': total_favorited,
                    # 'constellation': constellation,
                    'location': location,
                    # 'room_id': room_id,
                    # 'live_verify': live_verify,
                    'school_name': school_name,
                    'region': region,
                    'unique_id_modify_time': unique_id_modify_time,
                    'avatar_uri': avatar_uri,
                    'share_qrcode_uri': share_qrcode_uri,
                    'nick_img': nick_img
                }
                # 返回准确的用户数据,如果要返回全部只保留user_list.append(result)
                if unique_id != dy_id:
                    # print(uid, short_id, sec_uid, nickname, nick_img, signature, room_id_str)
                    user_list.append(result)
                else:
                    return {'status': 200, 'data': [result]}
            return {'status': 200, 'data': user_list}
        else:
            return {'status': 500, 'data': None}


if __name__ == '__main__':
    if not COOKIES:
        print(
        """
        !!!!!!
        请添加COOKIE.
        !!!!!!
        """
        )
    else:
        dy_id = input("Please enter your search account name:")
        result = search(dy_id)
        print(result)
