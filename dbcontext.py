import sqlite3

class Context:
    DATABASE_PATH = 'your_database.db'

    @staticmethod
    def connect():
        conn = sqlite3.connect(Context.DATABASE_PATH)
        cursor = conn.cursor()
        return conn, cursor

    @staticmethod
    def disconnect(conn):
        conn.close()

    @staticmethod
    def create_table():
        conn, cursor = Context.connect()
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS result_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT,
            words TEXT,
            specWords INTEGER,
            symbols INTEGER,
            symbolsNoSpaces INTEGER,
            letters INTEGER,
            foreignWords INTEGER,
            waterPercentage REAL,
            marks INTEGER,
            stopWords INTEGER,
            wordsDistribution TEXT,
            wordsDistributionNoStopWords TEXT
        );
        '''
        cursor.execute(create_table_query)
        conn.commit()
        Context.disconnect(conn)

    @staticmethod
    def insert_result(result):
        try:
            conn, cursor = Context.connect()
            insert_data_query = '''
            INSERT INTO result_data (
                text, words, specWords, symbols, symbolsNoSpaces, letters, foreignWords, waterPercentage,
                marks, stopWords, wordsDistribution, wordsDistributionNoStopWords
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
            '''

            data_to_insert = (
                result.text, result.words, result.specWords, result.symbols,
                result.symbolsNoSpaces, result.letters, result.foreignWords,
                result.waterPercenatge, result.marks, result.stopWords,
                str(result.wordsDistribution), str(result.wordsDistributionNoStopWords)
            )

            cursor.execute(insert_data_query, data_to_insert)
            conn.commit()
            Context.disconnect(conn)
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    @staticmethod
    def get_all_results():
        conn, cursor = Context.connect()
        select_all_query = "SELECT * FROM result_data"
        cursor.execute(select_all_query)
        rows = cursor.fetchall()
        Context.disconnect(conn)
        return rows

    @staticmethod
    def delete_one_result(result_id):
        conn, cursor = Context.connect()
        delete_query = "DELETE FROM result_data WHERE id = ?"
        cursor.execute(delete_query, (result_id,))
        conn.commit()
        Context.disconnect(conn)
		