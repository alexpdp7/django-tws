import pathlib
import sys
import subprocess
import tempfile


def run():
    tempdir = pathlib.Path(tempfile.gettempdir())
    db = tempdir / "tws.sqlite3"
    if db.exists():
        db.unlink()
    db_url = f"sqlite:///{db}"
    print("db_url", db_url)
    env = {
        "DATABASE_URL": db_url
    }
    subprocess.run([sys.executable, "-m", "showcase.dj.manage", "migrate"], check=True, env=env)
    subprocess.run([sys.executable, "-m", "showcase.dj.manage", "loaddevserverdata"], check=True, env=env)
    subprocess.run([sys.executable, "-m", "showcase.dj.manage", "runserver"], check=True, env=env)
