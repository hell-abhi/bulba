import MySQLdb


class Connect:

    def __init__(self, host, user, passwd, db):

        self.db = MySQLdb.connect(
            host=host,
            user=user,
            passwd=passwd,
            db=db
        )
        self.cursor = self.db.cursor()

    def establish_connection(self):

        return self.cursor

    def __del__(self):

        self.db.close()
