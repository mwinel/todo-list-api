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

        create_todo_table = "CREATE TABLE IF NOT EXISTS todos\
        (todo_id SERIAL PRIMARY KEY, title VARCHAR(140));"
        self.cursor.execute(create_todo_table)

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

    def insert_todo_data(self, title):
        """Insert todo data into the database."""
        todo_query = "INSERT INTO todos (title)\
        VALUES ('{}');".format(title)
        self.cursor.execute(todo_query)

    def fetch_all_todos(self):
        self.cursor.execute("SELECT * FROM todos")
        rows = self.cursor.fetchall()
        todos = []
        for row in rows:
            row = {'todo_id': row[0], 'title': row[1]}
            todos.append(row)
        return todos

    def drop_tables(self):
        """Drop tables if they exist."""
        query = "DROP TABLE IF EXISTS {0} CASCADE"
        tables = ["users"]
        for table in tables:
            self.cursor.execute(query.format(table))
