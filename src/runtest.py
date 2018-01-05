import sys
sys.path.append("/home/ccjh/demo_git/sele_po_demo")
import unittest, time, HTMLTestRunner
from config.parameter import test_case_path, report_name
from src.common import send_mail




suite = unittest.defaultTestLoader.discover(start_dir = test_case_path, pattern='test*.py')


if __name__ =="__main__":
    report = report_name+"Report.html"
    fb = open(report, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream = fb,
        title = "test",
        description = "u know"
    )
    runner.run(suite)
    fb.close()
    time.sleep(10)
    email = send_mail.send_mail()
    email.sendReport()