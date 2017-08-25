import os
startCommon = 'python '
addPatien = startCommon + 'addPatient.py'
addServiceOrder = startCommon + 'addServiceOrder.py'
register = startCommon + 'registerClosedLoop.py'
delServiceOrderList = startCommon + 'delServiceOrder\(list\).py'
delServiceOrderAccount = startCommon + 'delServiceOrder\(account\).py'
delServiceOrder = startCommon + 'delServiceOrder.py'
os.system(addPatien)
os.system(addServiceOrder)
os.system(register)
os.system(delServiceOrderList)
os.system(delServiceOrderAccount)
os.system(delServiceOrder)