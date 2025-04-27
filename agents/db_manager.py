import sqlite3
from datetime import datetime


class DatabaseManager:
    def __init__(self, db_name='agents_memory.db'):
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()

    def create_tables(self):
        # Create the tables (if they don't already exist)
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS context (
            id INTEGER PRIMARY KEY,
            topic TEXT,
            content TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );
        """)
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS interactions (
            id INTEGER PRIMARY KEY,
            agent_name TEXT,
            action TEXT,
            content TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );
        """)
        self.conn.commit()

    def save_context(self, topic, content):
        """Store context to be remembered."""
        self.cursor.execute("INSERT INTO context (topic, content) VALUES (?, ?)", (topic, content))
        self.conn.commit()

    def get_context(self, topic):
        """Retrieve context based on the topic."""
        self.cursor.execute("SELECT content FROM context WHERE topic = ? ORDER BY created_at DESC LIMIT 1", (topic,))
        result = self.cursor.fetchone()
        return result[0] if result else None

    def log_interaction(self, agent_name, action, content):
        """Log the interaction between agents."""
        self.cursor.execute("INSERT INTO interactions (agent_name, action, content) VALUES (?, ?, ?)", (agent_name, action, content))
        self.conn.commit()

    def close(self):
        self.conn.close()
