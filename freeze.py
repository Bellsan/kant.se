#!/usr/bin/env python3
from flask_frozen import Freezer
from app import create_app
if __name__ == '__main__':
    app = create_app()
    freezer = Freezer(app)
    freezer.run(debug=True)