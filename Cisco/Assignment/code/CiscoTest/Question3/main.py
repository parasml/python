#-----------------------------------------------------------
# Rest Api 
#------------
'''
Functionality:
1) Token based authentication to access API.
2) Create a new router details with unique loopbackand hostname values.
3) Update the routers details in the database based on IP.
4) Get the list of all the routers based on type(AG1/ CSS) using SAP ID.
5) Get the list of routers as per the given IP range values.
6) Delete record from dtabase based on IP
'''
#-----------------------------------------

#!flask/bin/python
from flask import Flask, jsonify, request

import tokenAuthentication
import createRouter
import connectDB

#--------------------------------------------
app = Flask(__name__)

# Token Authentiation ----------------------------------
@app.route('/token-authenticate', methods=['GET'])
def tokenAuthenticate():

    oTokenAuthentication = tokenAuthentication.tokenAuthentication()
    strToken = oTokenAuthentication.generateToken()
    #print("strToken = ", strToken)
    bSucess = oTokenAuthentication.authenticateToken(strToken)
    #print("bSucess = ", bSucess)
    return jsonify({'Sucess': bSucess})


# Create new Router details ----------------------------------
@app.route('/create-record', methods=['GET'])
def createRecord():

    oCreateRouter = createRouter.createRouter()
    routerDetails = oCreateRouter.getRouterDetails()

    return jsonify({'RouterDetails': routerDetails})

'''
# delete Router from DB ----------------------------------
@app.route('/delete-router/<ipaddress>', methods=['GET'])
def deleteRouter(ipaddress=None):

    # http://127.0.0.1:5000/delete-router/135.80.24.106
    #results1 = request.args.get('ipaddress', '0-100')
    oConnectDB = connectDB.connectDB()
    oConnectDB.deleteRecord(ipaddress)

    return jsonify({'Router Deleted': ipaddress})
'''
    
# delete Router from DB ----------------------------------
@app.route('/delete-router', methods=['GET','POST'])
def deleteRouter():

    ipaddress = request.form['ipaddress']
    print("ipaddress = ", ipaddress)
    oConnectDB = connectDB.connectDB()
    oConnectDB.deleteRecord(ipaddress)

    return jsonify({'Router Deleted': ipaddress})



'''
# Get matching Router IP's from DB ----------------------------------
@app.route('/get-matching-ip-address/<ipaddress>', methods=['GET'])
def getMatchingIPAddress(ipaddress=None):

    oConnectDB = connectDB.connectDB()
    lsRecord = oConnectDB.get_IP_Records(ipaddress)

    return jsonify({'MatchingRouterAddress': lsRecord})
'''

# Get matching Router IP's from DB ----------------------------------
@app.route('/get-matching-ip-address', methods=['GET'])
def getMatchingIPAddress():

    ipaddress = request.form['ipaddress']
    oConnectDB = connectDB.connectDB()
    lsRecord = oConnectDB.get_IP_Records(ipaddress)

    return jsonify({'MatchingRouterAddress': lsRecord})

if __name__ == '__main__':
    app.run(debug=True)




