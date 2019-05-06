#-*-coding:utf-8-*-
#@Time      :2019/5/7 0003 20:52
#@Author    :蓝天下的风
#@Email     :394845369@qq.com
#@File      :send_email.py
#@Software  :PyCharm Community Edition

"""
    发送邮件
    手工发邮件
    1、选择邮件发送服务商：网易，QQ
    2、登录
    3、编写邮件
    4、发送
    协议 pop3 smtp
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

class SendEmail:

    def __init__(self):
        self.mailhost='smtp.qq.com'
        self.emailname = '394845369@qq.com'
        self.emailpwd = 'atmgmtnrtucobied'
        self.sendto = '394845369@qq.com'
        self.subject= 'python邮件测试'
        self.msg_from = 'GaoXu'
        self.port=465
        self.msg_raw="""<p>Python 邮件发送测试...</p>
            <p><a href="https://www.ketangpai.com/Home/User/login.html">点击</a></p>
            """#内容

    def send_email(self):
        # 总的邮件内容，分为不同的模块
        msg_total = MIMEMultipart()
        #正文模块
        msg_raw = self.msg_raw
        msg=MIMEText(msg_raw,'html','utf-8')
        msg_total['Subject']= self.subject
        msg_total['From']= self.msg_from
        msg_total['To']= self.sendto
        msg_total.attach(msg)
        #附件模块
        #mfile = MIMEApplication(open('demo.txt','rb').read())
        #修改添加附件的头信息
        #mfile.add_header('Content-Dispostion','attachment',file_name = 'demo.txt')
        #mfile.add_header('Content-ID', '<0>')
        #mfile.add_header('X-Attachment-Id', '0')
        #附件模块添加到总的模块里面m
        #msg_total.attach(mfile)
        server = smtplib.SMTP_SSL(self.mailhost,self.port)
        # 登录 参数为用户名密码
        server.login(self.emailname, self.emailpwd)
        try:
            server.send_message(self.emailname,self.sendto, msg_total.as_string())
            print("发送成功")
        except Exception as e:
            print("发送失败")
            print(e)
        finally:
            server.quit()

if __name__ == '__main__':
    send_msg=SendEmail()
    send_msg.send_email()



