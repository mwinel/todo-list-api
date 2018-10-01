import psycopg2


class Database:
    """
    This class defines and holds all database queries.
    """

    def __init__(self):
        """Initialize connection to the database."""
        self.connection = psycopg2.connect(
            database="todo", user="murungi", host="localhost",
            password="myPassword", port="5432"
        )
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()

    def create_tables(self):
        """Creates all database tables."""
        create_user_table = "CREATE TABLE IF NOT EXISTS users\
        (user_id SERIAL PRIMARY KEY, username VARCHAR(20),\
        password VARCHAR(40));"
        self.cursor.execute(create_user_table)

    def insert_user_data(self, username, password):
        """Insert user data into the database."""
        user_query = "INSERT INTO users (username, password)\
        VALUES ('{}', '{}');".format(username, password)
        self.cursor.execute(user_query)

    def get_by_argument(self, table, colunm, argument):
        query = "SELECT * FROM {} WHERE {} = '{}';".format(
            table, colunm, argument)
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        return result

    def fetch_all_users(self):
        self.cursor.execute("SELECT * FROM users")
        rows = self.cursor.fetchall()
        users = []
        for row in rows:
            row = {'user_id': row[0], 'username': row[1], 'password': row[2]}
            users.append(row)
        return users

    def drop_tables(self):
        """Drop tables if they exist."""
        query = "DROP TABLE IF EXISTS {0} CASCADE"
        tables = ["users"]
        for table in tables:
            self.cursor.excute(query.format(table))
