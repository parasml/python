#-------------------------------------------------------------------
# To create router
# new Router details
# Chek if already exists, if yes, create new one...
#------------------
import connectDB
from faker import Faker

class createRouter:

    def __init__(self):

        self.routerDetails = {}

        self.oConnectDB = connectDB.connectDB()



    def getRouterDetails(self):

        faker = Faker()
        self.routerDetails['ipAddress'] = faker.ipv4() 
        self.routerDetails['hostName'] = faker.hostname()
        self.routerDetails['domainName'] = faker.domain_name()
        self.routerDetails['domainWord'] = faker.domain_word()
        self.routerDetails['TLD'] = faker.tld()
        self.routerDetails['loopBack'] = faker.ipv4(network=False)


        bIP_Exits = self.checkIfRouterAlreadyExists()

        print("bIP_Exits = ", bIP_Exits)



        if bIP_Exits == True:

            self.getRouterDetails()  # To get new Router details -----------------
        
        else:
            self.updateRouterDetails()

        
        print("self.routerDetails = ", self.routerDetails)

        return self.routerDetails


    def checkIfRouterAlreadyExists(self):
        
        bSucess = self.oConnectDB.checkIfRecordAlreadExists(self.routerDetails['ipAddress'])
        return bSucess

    def updateRouterDetails(self):

        print("Function updateRouterDetails")
        self.oConnectDB.updateInsertRecord(self.routerDetails)


#--------------------------------------------------------------
# Local Testing
#----------------
'''
oCreateRouter = createRouter()
oCreateRouter.getRouterDetails()
'''






