class Select:

    def __init__(self, connection=None, columns=None, tables=None):

        if not connection:
            raise ValueError("Specify a Connect object")

        if not columns:
            raise ValueError("Specify column name(s)")

        if not tables:
            raise ValueError("Specify table name(s)")

        self.cursor = connection.establish_connection()

        self.columns = columns
        self.columns_size = len(columns)

        self.tables = tables
        self.table_size = len(tables)

        self.prepare_query()

    def prepare_query(self):

        self.query_string = "SELECT "

        if type(self.columns) is list:
            columns_iterator = 1
            for column in self.columns:
                if columns_iterator < self.columns_size:
                    self.query_string += column+", "
                elif columns_iterator == self.columns_size:
                    self.query_string += column+" "
                columns_iterator = columns_iterator+1

        if type(self.columns) is str:
            self.query_string += self.columns+" "

        self.query_string += "FROM "

        for table in self.tables:
            self.query_string += table

    def limit(self, limit_count):

        self.query_string += " LIMIT "+str(limit_count)

    def execute_query(self):

        self.cursor.execute(self.query_string)
        columns = self.cursor.description
        self.result = [
            {columns[index][0]:column for index, column in enumerate(value)}
            for value in self.cursor.fetchall()
            ]
        return self.result

    def print_query_string(self):

        print(self.query_string)
