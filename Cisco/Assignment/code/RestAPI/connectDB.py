#-------------------------------------------------------------
# To connect Router Database
#----------------------------
import psycopg2
import config


class connectDB:
    

    def __init__(self):

        self.postgresConn = psycopg2.connect(dbname=config.PG_DATABASE_NAME, host=config.PG_DATABASE_HOST, port=config.PG_DATABASE_PORT, user=config.PG_DATABASE_USER, password=config.PG_DATABASE_PASSWORD)
        #print("postgrescon = ", postgrescon)

        self.cursor = self.postgresConn.cursor()

    def updateInsertRecord(self, metaDataInfo):

        #print("metaDataInfo = ", metaDataInfo)

        postgres_insert_query = """ 
            INSERT INTO routerinfo
            (ipAddress, hostName, domainName, domainWord, TLD, loopBack)
            VALUES (%s,%s,%s,%s,%s,%s)
            """

        record_to_insert = (
            metaDataInfo['ipAddress'],
            metaDataInfo['hostName'],
            metaDataInfo['domainName'],
            metaDataInfo['domainWord'],
            metaDataInfo['TLD'],
            metaDataInfo['loopBack']
        )

        self.cursor.execute(postgres_insert_query, record_to_insert)

        self.postgresConn.commit()
        count = self.cursor.rowcount

        print("count = ", count)


    # To delete particular record --------------------------
    def deleteRecord(self, ipAddress):

        strQuery = """DELETE FROM routerinfo WHERE ipaddress = %s;"""

        record_to_delete = (ipAddress,)


        self.cursor.execute(strQuery, record_to_delete)
        self.postgresConn.commit()


    # To get Records ------------------------------------------
    def get_IP_Records(self, ipaddress):

        sql_select_query = "select * from routerinfo where ipaddress LIKE %s;"
        self.cursor.execute(sql_select_query, ('%'+str(ipaddress)+'%',))
        lsRecord = self.cursor.fetchall()
        print("lsRecord = ", lsRecord)
        #print("record = ", type(record))
        return lsRecord
        
    # To check if record Alread exists --------------------------
    def checkIfRecordAlreadExists(self, ipaddress):


        sql_select_query = "select * from routerinfo where ipaddress = %s;"
        self.cursor.execute(sql_select_query, (str(ipaddress),))
        record = self.cursor.fetchone()
        print("record = ", record)
        #print("record = ", type(record))
        
        if record is not None:
            return True
        else:
            return False

    # To close DB connection ---------------------------------------
    def closeConnection(self):
        try:
            if(self.postgresConn):
                self.cursor.close()
                self.postgresConn.close()
                print("PostgreSQL connection is closed")
        except:
            print("Error occured while closing postgres connections")



#--------------------------------------------------------------
# Local testing
#----------------
'''
oConnectDB = connectDB()
oConnectDB.get_IP_Records('19')
deleteRecord('190.106.79.181')
'''