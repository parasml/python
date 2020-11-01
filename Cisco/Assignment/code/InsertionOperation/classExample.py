# ------------------------------------
# To create a class
#---------------------
import json,urllib.request

class routerOperations:

    def __init__(self):

        print("Inside Router class")

        self.requestData()
        

    def insertRecord():
        pass

    def createRecord():
        pass

    def hardDelete():
        pass

    def softDelete():
        pass

    def requestData(self):
        
        data = urllib.request.urlopen("https://api.github.com/users?since=100").read()
        output = json.loads(data)
        print (type(output))
        print ("Len = ", len(output))


#-------------------------------------------
if __name__ == "__main__":
    print("Inside main")

    oRouterOperations = routerOperations()
