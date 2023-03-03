import mysql.connector

class Core:
    def __init__(self) -> None:
        self.__connectDb()
        
    def __connectDb(self):
        try:
            self.conn = mysql.connector.connect(
                host = 'localhost',
                database = 'qtdb',
                user = 'root',
                password = 'root'
            )
        except Exception as err:
            print(err)
        # else:
        #     print('Ulandi.')

    def createTable(self):
        try:
            with self.conn.cursor() as cursor:
                sql = '''CREATE TABLE if not exists user (
                        id serial,
                        productname VARCHAR(32) unique,
                        price VARCHAR(32),
                        amount VARCHAR(32)
                        );'''
                cursor.execute(sql)
        except Exception as err:
            print(err)
        else:
            print('jadval yasaldi')
        
    def insertUser(self,pname,pprice,pamount):
        try:
            with self.conn.cursor() as cursor:
                query = f'''insert into user (productname,price,amount) values ('{pname}','{pprice}','{pamount}')'''
                cursor.execute(query)
        except Exception as err:
            print(err)
        else:
            print('malumot kiritildi')
            self.conn.commit()
    def getinfo(self):
        try:
            with self.conn.cursor() as cursor:
                query='''select productname,price,amount from user;'''
                cursor.execute(query)
                result=cursor.fetchall()
        except Exception as err:
            print(err)
        else:
            return result
    def searchinfo(self,w):
        if w ==' ':
            self.getinfo()
        else:
            try:
                with self.conn.cursor() as cursor:
                    search = f'''select productname,price,amount from user where productname like "{w}%"'''
                    cursor.execute(search)
                    result=cursor.fetchall()
            except Exception as err:
                print(err)
            else:
                return result

    def delinfo(self,d):
        if d=='':
            self.getinfo()
        else:
            try:
                with self.conn.cursor() as cursor:
                    dell = f'''delete from user where productname = "{d}"'''
                    cursor.execute(dell)
            except Exception as err:
                print(err)
            else:
                self.conn.commit()
# git hubdan ozgartrdm
