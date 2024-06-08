from database.connection import get_db_connection

class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        self.id = id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id

    def __repr__(self):
        return f'<Article {self.title}>'
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if hasattr(self, '_title'):
            raise AttributeError("Cannot change title after it has been set")
        if not isinstance(value, str):
            raise TypeError("Title must be a string")
        if not (5 <= len(value) <= 50):
            raise ValueError("Title must be between 5 and 50 characters")
        self._title = value

    def author(self):
        return get_author(self.id)

    def magazine(self):
        return get_magazine(self.id)

def get_author(article_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = """
        SELECT a.*
        FROM authors a
        INNER JOIN articles ar ON ar.author_id = a.id
        WHERE ar.id = ?
    """
    cursor.execute(sql, (article_id,))
    author_data = cursor.fetchone()

    if author_data:
        return author_data  # Return author data directly
    else:
        return None

def get_magazine(article_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = """
        SELECT m.*
        FROM magazines m
        INNER JOIN articles ar ON ar.magazine_id = m.id
        WHERE ar.id = ?
    """
    cursor.execute(sql, (article_id,))
    magazine_data = cursor.fetchone()

    if magazine_data:
        return magazine_data  # Return magazine data directly
    else:
        return None
