import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/pranjal/robot_ws/argo-test/install/twist_stamper'
