import mysql.connector
from config import db_config

db = mysql.connector.connect(
  host=db_config.DB_HOST,
  user=db_config.DB_USER,
  password=db_config.DB_PASS,
  database=db_config.DB_NAME
)

cursor = db.cursor()

# Create ticket
def create_ticket(title, description):
  cursor.execute("INSERT INTO tickets (title, description) VALUES (%s, %s)", (title, description))
  db.commit()
  return cursor.lastrowid

# Get ticket details
def get_ticket(ticket_id):
  cursor.execute("SELECT * FROM tickets WHERE id=%s", (ticket_id,))
  return cursor.fetchone()

# Update ticket
def update_ticket(ticket_id, status):
  cursor.execute("UPDATE tickets SET status=%s WHERE id=%s", (status, ticket_id))
  db.commit()
  cursor.execute("SELECT status FROM tickets WHERE id=%s", (ticket_id,))
  return cursor.fetchone()[0]

# Delete ticket
def delete_ticket(ticket_id):
  cursor.execute("DELETE FROM tickets WHERE id=%s", (ticket_id,))
  db.commit()