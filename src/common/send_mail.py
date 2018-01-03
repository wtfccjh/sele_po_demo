import sys
sys.path.append("/home/ccjh/demo_git/sele_po_demo")
import os
import smtplib
from config import parameter
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import log




class send_mail:
    def __init__(self):
        self.mylog = log.log()
    
    def email_init(self, report, reportName):
        with open(report,'rb')as f:
            mail_body = f.read()
    
        msg = MIMEMultipart()
        msg.attach(MIMEText(mail_body,'html','utf-8'))
        report_file = MIMEText(mail_body,'html', 'utf-8')
        report_file["Content-Disposition"] = 'attachment;filename='+reportName
        msg.attach(report_file)
        msg['Subject'] = reportName
        msg['From'] = parameter.email_name
        msg['To'] = parameter.email_To
        try:
            server = smtplib.SMTP(parameter.smtp_sever)
            server.login(parameter.email_name, parameter.email_password)
            server.sendmail(msg['From'],msg['To'].split(';'), msg.as_string())
            server.quit()
        except smtplib.SMTPException:
            self.mylog.error('error'+__file__)
    
    def sendReport(self):
        report_list = os.listdir(parameter.report_path)
        report_list.sort(key=lambda fn: os.path.getmtime(parameter.report_path+fn) if not os.path.isdir(parameter.report_path+fn) else 0)
        new_report = os.path.join(parameter.report_path, report_list[-1])
        self.email_init(new_report, report_list[-1])