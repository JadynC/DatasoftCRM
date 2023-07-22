import unittest
import mysql.connector
from crud import create_ticket
from crud import update_ticket
from config import db_config


class TestTickets(unittest.TestCase):

    def setUp(self):
        self.db = mysql.connector.connect(
            host=db_config.DB_HOST,
            user=db_config.DB_USER,
            password=db_config.DB_PASS,
            database=db_config.DB_NAME
        )
        self.cursor = self.db.cursor()

    def test_create_ticket(self):
        # # Insert with column names
        # self.cursor.execute("INSERT INTO tickets (id, title, description) VALUES (1, 'Title', 'Desc')")

        # # Assert id was inserted
        # result = self.cursor.execute("SELECT * FROM tickets WHERE id=1")
        # print(result)
        # self.assertEqual(result, 1)
        result = create_ticket('test','1')
        self.assertEqual(result, 1)

    def test_update_ticket(self):
        # # Insert ticket
        # self.cursor.execute("INSERT INTO tickets (id, title, description) VALUES (1, 'Title', 'Desc')")

        # # Update ticket
        # self.cursor.execute("UPDATE tickets SET status='closed' WHERE id=1")

        # # Assert ticket updated
        # result = self.cursor.execute("SELECT status FROM tickets WHERE id=1")
        # self.assertEqual(result, 'closed')

        result = update_ticket(1,'closed')
        self.assertEqual(result, 'closed')


    def tearDown(self):
        self.db.close()


if __name__ == '__main__':
    unittest.main()