import pathlib
import sys
import subprocess
import tempfile


def run(module):
    tempdir = pathlib.Path(tempfile.gettempdir())
    db = tempdir / "tws.sqlite3"
    if db.exists():
        db.unlink()
    db_url = f"sqlite:///{db}"
    print("db_url", db_url)
    env = {
        "DATABASE_URL": db_url
    }
    subprocess.run([sys.executable, "-m", f"{module}.manage", "removedevservermigrations"], check=True, env=env)
    subprocess.run([sys.executable, "-m", f"{module}.manage", "makemigrations", "-n", "devserver_migration"], check=True, env=env)
    try:
       subprocess.run([sys.executable, "-m", f"{module}.manage", "migrate"], check=True, env=env)
       subprocess.run([sys.executable, "-m", f"{module}.manage", "loaddevserverdata"], check=True, env=env)
       subprocess.run([sys.executable, "-m", f"{module}.manage", "runserver"], check=True, env=env)
    finally:
        subprocess.run([sys.executable, "-m", f"{module}.manage", "removedevservermigrations"], check=True, env=env)
