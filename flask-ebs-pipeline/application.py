# -*- coding: utf-8 -*-
"""Provide commands for starting the application, creating the database and seeding the database."""
from api import create_app

application = create_app()


if __name__ == '__main__':
    application.run(host='0.0.0.0', debug=True)
