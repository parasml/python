import os

import os
import subprocess
import re

#--------------------------------------------------------
# To execute batch file
#------------------------
def executeBatchFile():
    batchPath = 'C:/Prashan/Cisco/Assignment/test.bat'

    import subprocess

    rc = subprocess.call(batchPath)

def getMachinePerformance():

    statistics = {}

    # Get Physical and Logical CPU Count
    physical_and_logical_cpu_count = os.cpu_count()

    print("physical_and_logical_cpu_count = ", physical_and_logical_cpu_count)

#----------------------------------------------
# function Calls
#------------------
#executeBatchFile()
#mon_performance()
getMachinePerformance()