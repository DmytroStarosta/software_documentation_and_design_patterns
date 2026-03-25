from app.presentation.app_presentation import app_presentation
from app import create_app


app = create_app()

if __name__ == '__main__':
    with app.app_context():
        print('Create DB')

        is_create_db = app_presentation.create_db()
        print('DB created' if is_create_db else 'DB not created')