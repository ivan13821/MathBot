import psycopg2

from database.config import get_db_params

class Database:



    # подключение и создание бд ------------------------------------------------------------------------------------------
    def __init__(self, modyl_name):
        self.conn = None
        self.cur = None
        self.connect_to_db(modyl_name)

    def connect_to_db(self, modyl_name):
        params = get_db_params()
        print('Подключаюсь к PostgreSQL...')
        try:
            self.conn = psycopg2.connect(**params)
            self.conn.autocommit = True
            self.cur = self.conn.cursor()
            print(f'Успешно подключен для работы с {modyl_name}')
            #self.create_tables_if_they_do_not_exists()
        except Exception as error:
            print(error)




    def execute_query(self, query, params=None):
        try:
            if params is not None:
                self.cur.execute(query, params)
            else:
                self.cur.execute(query)
        except psycopg2.InterfaceError as e:
            print(e)
            print("Не удалось выполнить запрос из-за ошибки подключения. Пытаюсь подключиться к базе заново")
            self.connect_to_db()
            self.cur.execute(query, params)


    def create_tables_if_they_do_not_exists(self):
        self.execute_query("""CREATE TABLE IF NOT EXISTS users (
                                chat_id serial primary key,
                                level int
                                )""")
    


    #работа с бд -----------------------------------------------------------------------------------------------------------------




    def insert_user(self, chat_id: int, level_plus: int = 1, level_minus: int = 1, level_mult: int = 1, level_division: int = 1) -> None:

        """Добавление нового пользователя """

        self.execute_query(f"""INSERT INTO users (chat_id, level_plus, level_minus, level_mult, level_division)
                                    values
                                    ({chat_id}, {level_plus}, {level_minus}, {level_mult}, {level_division})""")


    def update_user(self, chat_id: int, level_plus: int = None, level_minus: int = None, level_mult: int = None, level_division: int = None):

        query = """UPDATE users SET """

        sets = []

        if level_plus is not None: sets.append(f'level_plus = {level_plus}')
        if level_minus is not None: sets.append(f'level_minus = {level_minus}')
        if level_mult is not None: sets.append(f'level_mult = {level_mult}')
        if level_division is not None: sets.append(f'level_division = {level_division}')

        query += ', '.join(sets) + ' '
        query += f"WHERE chat_id={chat_id}"

        self.execute_query(query)


    def select_levels(self, chat_id):
        self.execute_query(f"""Select level_plus, level_minus, level_mult, level_division from users where chat_id={chat_id}""")

        return self.cur.fetchone()