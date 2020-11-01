#-----------------------------------------------------
# Generate Records
#--------------------
from faker import Faker
import pandas as pd
import uuid
import sys

print("-------------------")

def GenerateRecord(nTotalRecords):

    nTotalRecords = int(nTotalRecords[0])
    
    faker = Faker()

    dfRecord = pd.DataFrame()

    for n in range(nTotalRecords):

        routerDetails = {}

        routerDetails['hostName'] = faker.hostname()
        routerDetails['sapid'] = uuid.uuid4()
        routerDetails['loopback'] = faker.ipv4(network=False)
        routerDetails['macaddress'] = faker.mac_address()

        dfRecord = dfRecord.append(routerDetails, ignore_index=True)

    print(dfRecord)

    return dfRecord



#------------------------------------------------------
# Function Calls
#-------------------

if __name__ == "__main__":
    
    print("sys.argv[1:] = ", sys.argv[1:])
    GenerateRecord(sys.argv[1:])
