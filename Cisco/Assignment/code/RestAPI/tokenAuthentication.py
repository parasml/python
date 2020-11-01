#--------------------------------------------------------
# To authenticate token
#-----------------------------
class tokenAuthentication:

    def __init__(self):
        pass
        

    # To authenticate token -----------------
    def authenticateToken(self, token):
        
        if token:
            return True
        else:
            return False

    # to generae new unique token -------------
    def generateToken(self):
        
        from uuid import uuid4
        rand_token = uuid4()

        print("rand_token = ", rand_token)

        return rand_token

'''
#---------------------------------------------
# Test Token
#---------------
oTokenAuthentication = tokenAuthentication()

strToken = oTokenAuthentication.generateToken()
print("strToken = ", strToken)

bSucess = oTokenAuthentication.authenticateToken(strToken)
print("bSucess = ", bSucess)
'''