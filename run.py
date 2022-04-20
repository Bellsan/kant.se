#!/usr/bin/env python3
import os
from app import create_app
from livereload import Server
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))
    app = create_app()
    server = Server(app.wsgi_app)
    server.serve()