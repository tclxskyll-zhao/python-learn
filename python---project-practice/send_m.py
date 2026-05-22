# 自动发送邮件脚本
import xlrd
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 1. 读取Excel数据
data = xlrd.open_workbook('名单1.xlsx')
sheet = data.sheets()[0]

# 存储收件人信息（如果需要批量发送）
email_list = []

for i in range(sheet.nrows):
    name = sheet.cell_value(i, 0)
    old_money = sheet.cell_value(i, 1)
    new_money = sheet.cell_value(i, 2)

    # 2. 登录邮箱
    smtp_obj = smtplib.SMTP_SSL('smtp.qq.com', 465)
    # 3. 授权码
    smtp_obj.login('975287570@qq.com', 'xjvgqgsgvjylbeei')
    # 4. 准备邮件内容
    to_person = 'skycoder1024@163.com'
    title=Header('测试邮件发送','utf-8')
    sendr=Header('975287570@qq.com')
    # 邮件正文（可以使用HTML格式）
    content = MIMEText(f'您好{name}，由于公司本季度盈利亏损，这里将大家的薪资调整，由 {old_money} 更改为 {new_money} ', 'html', 'utf-8')
    # 封装邮件信息
    content['From'] = sendr  # 发件人
    content['To'] = to_person  # 收件人
    content['Subject'] =title #主题
    # 4. 发送邮件
    try:
        smtp_obj.sendmail('975287570@qq.com', to_person, content.as_string())
        print(f"邮件发送成功！收件人：{to_person}")
    except Exception as e:
        print(f"发送失败：{e}")
    finally:
        smtp_obj.quit()