from app import create_app
from modules.database import init_db


if __name__ == '__main__':
    init_db()
    create_app().run()
