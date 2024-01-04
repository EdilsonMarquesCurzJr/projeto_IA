from app import create_app
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
