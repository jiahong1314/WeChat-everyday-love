#!/usr/bin/python3
# coding=utf-8
import love
# {{content.DATA}}
# 综合指数：{{total.DATA}}
# 爱情指数：{{love.DATA}}
# 工作指数：{{work.DATA}}
# 财运指数：{{money.DATA}}
# 健康指数：{{health.DATA}}
# 幸运颜色：{{color.DATA}}
# 幸运数字：{{math.DATA}}
# 今日概述：{{toady.DATA}}
if __name__ == '__main__':
    # 微信配置
    wechat_config = {
        'appid': '',  # (No.1)此处填写公众号的appid
        'appsecret': '',  # (No.2)此处填写公众号的appsecret
        'template_id': ''  # (No.3)此处填写公众号的模板消息ID
    }

    # 用户列表
    '''
        run()方法可以传入openids列表，也可不传参数
        不传参数则对微信公众号的所有用户进行群发
    '''
    openids = [
        '',  # (No.4)此处填写你的微信号（微信公众平台上的微信号）
        # 'xxxxx', #如果有多个用户也可以
        # 'xxxxx',
    ]

    # 执行
    icb = love.love(wechat_config)

    icb.run()



