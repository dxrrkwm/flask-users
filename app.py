import os

from flask import Flask

from app import create_app
from app.extensions import db


app: Flask = create_app()


with app.app_context():
    os.makedirs(app.instance_path, exist_ok=True)
    print(f"Instance path: {app.instance_path}")
    try:
        db.create_all()
        print("Database created")
    except Exception as e:
        print(f"Error creating database: {e}")


@app.cli.command("init-db")
def init_db() -> None:
    db.create_all()
    print("Database created")


if __name__ == "__main__":
    print("Starting app")
    app.run(host="0.0.0.0", port=5000, debug=False)
