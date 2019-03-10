import sqlite3
from sqlite3 import Error as sqlErr
import re as rex

def create_connection(db_file: str ="C:\sqlite\sqlite\Python210FinalDB.db"):
    """ Create or connect to a SQLite database """
    try:
        con = sqlite3.connect(db_file)
    except sqlErr as se:
        raise Exception('SQL Error in create_connection(): ' + se.__str__())
    except Exception as e:
        raise Exception('General Error in create_connection(): ' + e.__str__())
    return con

# SQL Validators
def check_for_extra_semicolon(sql_str):
    """Checks for an extra semicolon"""
    # print(len("Select;Delete From T1; ID, Name FROM T1;".split(';')) > 2)
    try:
        if len(sql_str.split(';')) > 2:
            raise sqlErr("Extra Semi-Colon Detected!")
    except Exception as e:
        raise e


def check_for_or(sql_str):
    """Checks for an injected OR in tampered WHERE Clause"""
    # print(rex.search("WHERE", "SELECT * FROM T1 WHERE", rex.IGNORECASE))
    # print(rex.search("or","FROM T1 WHERE ID = 1 or 1 = 1".split('WHERE')[1], rex.IGNORECASE))
    try:
        if rex.search("WHERE", sql_str, rex.IGNORECASE): #If it has a Where clause
            if rex.search(' or ', sql_str.split('WHERE')[1], rex.IGNORECASE) is not None:  # check injected OR
                raise sqlErr("OR Detected!")
    except Exception as e:
        raise e

def check_for_date(date_str): #Inventories table check
    try:
        if rex.match("\d\d\d\d-\d\d-\d\d", str(date_str)) is None:  # Returns None if not matched
            raise sqlErr("Not a Date!")
    except Exception as e:
        raise e

# def execute_sql_code(db_con: object = None, sql_code: str = ''):
#     """ Execute SQL code on a open connection """
#     try:
#         if db_con is not None and sql_code != '':
#             # Validate
#             check_for_extra_semicolon(sql_code);
#             check_for_or(sql_code);
#             # Connect and Run
#             with db_con:
#                 csr = db_con.cursor()
#                 csr.execute(sql_code)
#         else:
#             raise Exception('SQL Code or Connection is missing!')
#     except sqlite3.OperationalError as oe:
#         raise Exception('Table already exists(): ' + oe.__str__())
#     except sqlErr as se:
#         raise Exception('SQL Error in execute_sql_code(): ' + se.__str__() + 'That ID already exists, and ID is a primary key')
#     except Exception as e:
#         raise Exception('General Error in execute_sql_code(): ' + e.__str__())
#     return csr


class DBProcessor(object):
    def __init__(self, db_name: str = "C:\sqlite\sqlite\Python210FinalDB.db"):
        self.__db_name = db_name
        self.__db_con = self.create_connection(self.db_name)

    @property
    def db_name(self):  # Get DB Name
        return self.__db_name

    @property
    def db_con(self):  # Get Live Connection
        return self.__db_con

    # SQL Validators
    @staticmethod
    def check_for_extra_semicolon(sql_str):
        """Checks for an extra semicolon"""
        # print(len("Select;Delete From T1; ID, Name FROM T1;".split(';')) > 2)
        try:
            if len(sql_str.split(';')) > 2:
                raise sqlErr("Extra Semi-Colon Detected!")
        except Exception as e:
            raise e

    @staticmethod
    def check_for_or(sql_str):
        """Checks for an injected OR in tampered WHERE Clause"""
        # print(rex.search("WHERE", "SELECT * FROM T1 WHERE", rex.IGNORECASE))
        # print(rex.search("or","FROM T1 WHERE ID = 1 or 1 = 1".split('WHERE')[1], rex.IGNORECASE))
        try:
            if rex.search("WHERE", sql_str, rex.IGNORECASE):  # If it has a Where clause
                if rex.search(' or ', sql_str.split('WHERE')[1], rex.IGNORECASE) is not None:  # injected OR?
                    raise sqlErr("OR Detected!")
        except Exception as e:
            raise e

    @staticmethod
    def check_for_date(date_str):  # Inventories table check
        """Checks for an valid date string"""
        try:
            if rex.match("\d\d\d\d-\d\d-\d\d", str(date_str)) is None:
                raise sqlErr("Not a Date!")
        except Exception as e:
            raise e

    @staticmethod
    def check_for_product_name(product_name):  # Product table check
        """Checks to make sure the product name is a string"""
        try:
            if type(product_name) is not str:
                raise sqlErr("Not a valid product name!")
        except Exception as e:
            raise e

    @staticmethod
    def inventory_counts_check(inventory_counts):
        """Checks something in the inventory counts"""
        pass

    def create_connection(self, db_file: str="C:\sqlite\sqlite\Python210FinalDB.db"):
        """ Create or connect to a SQLite database """
        try:
            con = sqlite3.connect(db_file)
        except sqlErr as se:
            raise Exception('SQL Error in create_connection(): ' + se.__str__())
        except Exception as e:
            raise Exception('General Error in create_connection(): ' + e.__str__())
        return con

    def execute_sql_code(self, db_con: object = None, sql_code: str = ''):
        """ Execute SQL code on a open connection """
        db_con = self.db_con
        try:
            if db_con is not None and sql_code != '':
                # Validate
                self.check_for_extra_semicolon(sql_code);
                self.check_for_or(sql_code);
                # Connect and Run
                with db_con:
                    csr = db_con.cursor()
                    csr.execute(sql_code)
            else:
                raise Exception('SQL Code or Connection is missing!')
        except sqlErr as se:
            raise Exception('SQL Error in execute_sql_code(): ' + se.__str__())
        except Exception as e:
            raise Exception('General Error in execute_sql_code(): ' + e.__str__())
        return csr

    def build_ins_code(self):
        # Validate Input
        sql = str.format("INSERT Not Implemented Yet")
        return sql

    def build_upd_code(self):
        # Validate Input
        sql = str.format("UPDATE Not Implemented Yet")
        return sql

    def build_del_code(self):
        # Validate Input
        # Validate Input
        sql = str.format("DELETE Not Implemented Yet")
        return sql

    def build_sel_code(self):
        # Validate Input
        sql = str.format("SELECT Not Implemented Yet")
        return sql


class InventoryProcessor(DBProcessor):
    def build_ins_code(self, inventory_id: int, inventory_date: str):
        DBProcessor.check_for_date(inventory_date)
        sql = str.format("INSERT OR IGNORE INTO Inventories (InventoryID, InventoryDate) "
                         "VALUES ({id},'{date}');", id=inventory_id, date=inventory_date)
        return sql

    def build_upd_code(self, inventory_id: int, inventory_date: str):
        DBProcessor.check_for_date(inventory_date)
        sql = str.format("UPDATE Inventories SET InventoryDate = '{date}' "
                         "WHERE InventoryID = {id};", id=inventory_id, date=inventory_date)
        return sql

    def build_del_code(self, inventory_id: int):
        sql = str.format("DELETE FROM Inventories "
                         "WHERE InventoryID = {id};", id=inventory_id)
        return sql

    def build_sel_code(self, inventory_id: int = None):
        if inventory_id is not None:
            w = ' WHERE InventoryID = ' + str(inventory_id)
        else:
            w = ''
        sql = str.format("SELECT InventoryID, InventoryDate "
                         "FROM Inventories{WHERE};", WHERE=w)
        return sql

class ProductsProcessor(DBProcessor):
    def build_ins_code(self, product_id: int, product_name: str):
        DBProcessor.check_for_product_name(product_name)
        sql = str.format("INSERT OR IGNORE INTO Products (ProductID, ProductName) "
                         "VALUES ({id},'{name}');", id=product_id, name=product_name)
        return sql

    def build_upd_code(self, product_id: int, product_name: str):
        DBProcessor.check_for_product_name(product_name)
        sql = str.format("UPDATE Products SET ProductName = '{name}' "
                         "WHERE ProductID = {id};", id=product_id, name=product_name)
        return sql

    def build_del_code(self, product_id: int):
        sql = str.format("DELETE FROM Products WHERE ProductID = {id};", id=product_id)
        return sql

    def build_sel_code(self, product_id: int = None):
        if product_id is not None:
            w = ' WHERE ProductID = ' + str(product_id)
        else:
            w = ''
        sql = str.format("SELECT ProductID, ProductName "
                         "FROM Products{WHERE};", WHERE=w)
        return sql

class InventoryCountsProcessor(DBProcessor):
    def build_ins_code(self, inventory_id: int, product_id: int, inventory_count: int):
        DBProcessor.inventory_counts_check(inventory_count)
        sql = str.format("INSERT OR IGNORE INTO InventoryCounts (InventoryID, ProductID, Count) "
                         "VALUES ({invid}, {prodid}, '{count}');", invid=inventory_id, prodid=product_id, count=inventory_count)
        return sql

    def build_upd_code(self, inventory_id: int, product_id: int, inventory_count):
        DBProcessor.inventory_counts_check(inventory_count)
        sql = str.format("UPDATE InventoryCounts SET Count = '{count}' "
                         "WHERE ProductID = {prodid} AND InventoryID = {invid};", count=inventory_count, prodid=product_id, invid=inventory_id)
        return sql

    def build_del_code(self, inventory_id: int, product_id: int):
        sql = str.format("DELETE FROM InventoryCounts WHERE ProductID = {prodid} AND InventoryID = {invid};", prodid=product_id, invid=inventory_id)
        return sql

    def build_sel_code(self, inventory_id: int = None):
        if inventory_id is not None:
            w = ' WHERE InventoryID = ' + str(inventory_id)
        else:
            w = ''
        sql = str.format("SELECT InventoryID, ProductID, Count "
                         "FROM InventoryCounts{WHERE};", WHERE=w)
        return sql

class create_tables():
    def create_inventories_tbl(self):
        sql = str.format("CREATE TABLE if not exists Inventories (InventoryID int Primary Key, InventoryDate date);")
        return sql

    def create_products_tbl(self):
        sql = str.format("CREATE TABLE if not exists Products (ProductID int Primary Key, ProductName varchar(100));")
        return sql

    def create_inventorycounts_tbl(self):
        sql = str.format("CREATE TABLE if not exists InventoryCounts (InventoryID int, ProductID int, Count int, Primary Key (InventoryID,ProductID));")
        return sql

if __name__ == '__main__':

    #Create Tables for Testing
    DBProcessor().execute_sql_code(db_con=create_connection(), sql_code=create_tables().create_products_tbl())
    DBProcessor().execute_sql_code(db_con=create_connection(), sql_code=create_tables().create_inventories_tbl())
    DBProcessor().execute_sql_code(db_con=create_connection(), sql_code=create_tables().create_inventorycounts_tbl())

    #Insert Data
    DBProcessor().execute_sql_code(db_con=create_connection(), sql_code=ProductsProcessor().build_ins_code(8888,'MMouse'))
    DBProcessor().execute_sql_code(db_con=create_connection(), sql_code=InventoryProcessor().build_ins_code(8888,'2019-01-01'))
    DBProcessor().execute_sql_code(db_con=create_connection(), sql_code=InventoryCountsProcessor().build_ins_code(99, 5, 2))

    #Select Data - all run without errors, but I can only return the cursor object, not the data
    DBProcessor().execute_sql_code(db_con=create_connection(), sql_code=InventoryProcessor().build_sel_code())
    DBProcessor().execute_sql_code(db_con=create_connection(), sql_code=InventoryCountsProcessor().build_sel_code())
    DBProcessor().execute_sql_code(db_con=create_connection(), sql_code=ProductsProcessor().build_sel_code(5))

    #Update Data
    DBProcessor().execute_sql_code(db_con=create_connection(), sql_code=InventoryProcessor().build_upd_code(5,'2000-09-09'))
    DBProcessor().execute_sql_code(db_con=create_connection(), sql_code=ProductsProcessor().build_upd_code(5,'thing'))
    DBProcessor().execute_sql_code(db_con=create_connection(), sql_code=InventoryCountsProcessor().build_upd_code(100,100,90000))

    #Delete Data
    DBProcessor().execute_sql_code(db_con=create_connection(), sql_code=InventoryProcessor().build_del_code(5))
    DBProcessor().execute_sql_code(db_con=create_connection(), sql_code=ProductsProcessor().build_del_code(5))
    DBProcessor().execute_sql_code(db_con=create_connection(), sql_code=InventoryCountsProcessor().build_del_code(2,101))
