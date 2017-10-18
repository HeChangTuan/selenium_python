# coding=utf-8
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')
# 测试用例 调用
import os
import ConfigParser

cf = ConfigParser.ConfigParser()
cf.read("config.conf")
commons = cf.options("common")
# addPatien = python addPatient.python 新增病人
# addServiceOrder = python addServiceOrder.py 预约
# register = python registerClosedLoop.py 注册
# delServiceOrderList = python delServiceOrder\(list\).py 删除预约 (查看所有预约列表版)
# delServiceOrderAccount = python delServiceOrder\(account\).py 删除预约 (首页账号进入版)
# delServiceOrder = python delServiceOrder.py 删除预约 (卡片预约详情进入版)
# editPatient = python editPatient.py 修改就诊人
# delPatient = python delPatient.py 删除就诊人
# initiateChatAccount = python initiateChat\(account\).py 发起会话 (首页账号进入版)
# initiateChatDoctor = python initiateChat\(doctor\).py 发起会话 (联系医生进入版)
for common in commons:
  runcommon = 'python ' + cf.get("common", common)
  os.system(runcommon)