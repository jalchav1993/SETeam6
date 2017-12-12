import pymysql
import numpy
class configurationDB:

    def __init__(self):
        self.__connect = self.connect()
        self.__connection
     
    def isset(self):
        return self in locals()
            
        
    def connect(self):
        if not self.isset(self.connection):
            self.__connection = pymysql.connect(host="earth.cs.utep.edu", user = "aquiroz10", passwd="cs4311", db="aquiroz10")                 
            
        if self.__connection is False:
            print("UNABLE TO CONNECT TO DATABASE")
            
        return self.__connection
    
    def close(self):
        if self.isset(self.__connection):
            self.__connection.close()
            self.__connection = None 
     
    def getError(self):
        if not self.isset(self.__connection):
            return "No connection established"
        return self.__connect.Error
    
               
    def select(self):
        db = self.__connect
        result = db.query(self)
        if result is False:
            print ("UNABLE TO SELECT",self.getError())
        rows = []
        row = result.fetchall()
        while row is not None:
            rows.append(row)
        return rows
    
    def insert(self):
        db = self.__connect
        db.query(self)
        if db.affected_rows() == 0:
            print ("INSERT failed check for duplicate entry")
        if db.affected_rows() < 0:
            print ("UPDATE failed: ",self.getError())
            
            
    def prepare(self):
        db = self.__connect
        stmt = db.prepare(self)
        if stmt == False:
            print("Unable to prepare statement: ", self.getError())
        return stmt
    
    def execute(self):
        stmt = self.execute()
        result = stmt._do_get_result()
        stmt.close()
        return result