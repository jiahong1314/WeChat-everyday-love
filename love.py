#!/usr/bin/python3
#coding=utf-8
import sys
import json
import requests

class love1:
    # 初始化
    def __init__(self, wechat_config):
        self.appid = wechat_config['appid'].strip()
        self.appsecret = wechat_config['appsecret'].strip()
        self.template_id = wechat_config['template_id'].strip()
        self.access_token = ''

    # 错误代码
    def get_error_info(self, errcode):
        return {
            40013: '不合法的 AppID ，请开发者检查 AppID 的正确性，避免异常字符，注意大小写',
            40125: '无效的appsecret',
            41001: '缺少 access_token 参数',
            40003: '不合法的 OpenID ，请开发者确认 OpenID （该用户）是否已关注公众号，或是否是其他公众号的 OpenID',
            40037: '无效的模板ID',
        }.get(errcode,'unknown error')

    # 打印日志
    def print_log(self, data, openid=''):
        errcode = data['errcode']
        errmsg = data['errmsg']
        if errcode == 0:
            print(' [INFO] send to %s is success' % openid)
        else:
            print(' [ERROR] (%s) %s - %s' % (errcode, errmsg, self.get_error_info(errcode)))
            if openid is not '':
                print(' [ERROR] send to %s is error' % openid)
            sys.exit(1)

    # 获取access_token
    def get_access_token(self, appid, appsecret):
        url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s' % (appid, appsecret)
        r = requests.get(url)
        data = json.loads(r.text)
        if 'errcode' in data:
            self.print_log(data)
        else:
            self.access_token = data['access_token']

    # 获取用户列表
    def get_user_list(self):
        if self.access_token == '':
            self.get_access_token(self.appid, self.appsecret)
        url = 'https://api.weixin.qq.com/cgi-bin/user/get?access_token=%s&next_openid=' % self.access_token
        r = requests.get(url)
        data = json.loads(r.text)
        if 'errcode' in data:
            self.print_log(data)
        else:
            openids = data['data']['openid']
            return openids

    # 发送消息
    def send_msg(self, openid, template_id, iciba_everyday,astro_words):
        msg = {
            'touser': openid,
            'template_id': template_id,
            'url': '81.70.161.239',  # 设置跳转页面
            'data': {
                'content': {
                    'value': iciba_everyday['newslist'][0]['content'],
                    'color': '#0000CD'
                    },
                'total': {
                    'value': astro_words['newslist'][0]['content'],
                },
                'love': {
                    'value': astro_words['newslist'][1]['content'],
                },
                'work': {
                    'value': astro_words['newslist'][2]['content'],
                },
                'money': {
                    'value': astro_words['newslist'][3]['content'],
                },
                'health': {
                    'value': astro_words['newslist'][4]['content'],
                },
                'color': {
                    'value': astro_words['newslist'][5]['content'],
                },
                'math': {
                    'value': astro_words['newslist'][6]['content'],
                },
                'today': {
                    'value': astro_words['newslist'][8]['content'],
                },
                'note': {
                    'value': '离上岸又近一步，加油！！！',
                }

            }
        }
        json_data = json.dumps(msg)
        if self.access_token == '':
            self.get_access_token(self.appid, self.appsecret)
        url = 'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=%s' % self.access_token
        r = requests.post(url, json_data)
        return json.loads(r.text)

    # 获取渣男语录每天一句
    def get_iciba_everyday(self):
        url = ''   # 请求API  按照请求格式
        r = requests.get(url)
        return json.loads(r.text)
    def get_astro(self):
        url = ''  # 请求API  按照请求格式
        r = requests.get(url)
        return json.loads(r.text)
    # 为设置的用户列表发送消息
    def send_everyday_words(self, openids):
        everyday_words = self.get_iciba_everyday()
        astro_words = self.get_astro()
        print(astro_words['newslist'][8]['content'])
        for openid in openids:
            openid = openid.strip()
            result = self.send_msg(openid, self.template_id, everyday_words,astro_words)
            self.print_log(result, openid)

    # 执行
    def run(self, openids=[]):
        if openids == []:
            # 如果openids为空，则遍历用户列表
            openids = self.get_user_list()
        # 根据openids对用户进行群发
        self.send_everyday_words(openids)

