import argparse
import contextlib
import pathlib
import sys
import subprocess
import tempfile


def run(module):
    tempdir = pathlib.Path(tempfile.gettempdir())
    db = tempdir / "tws.sqlite3"
    db_url = f"sqlite:///{db}"
    print("db_url", db_url)
    env = {"DATABASE_URL": db_url}

    parser = argparse.ArgumentParser()
    parser.add_argument("--command", default="runserver")
    parser.add_argument(
        "--no-reset-database", action="store_false", dest="reset_database"
    )
    parser.add_argument("--keep-database", action="store_true", dest="keep_database")
    args = parser.parse_args()

    with with_reset_database(
        module,
        db,
        env,
        reset_database=args.reset_database,
        keep_database=args.keep_database,
    ):
        subprocess.run(
            [sys.executable, "-m", f"{module}.manage", args.command],
            check=True,
            env=env,
        )


@contextlib.contextmanager
def with_reset_database(module, db, env, *, reset_database, keep_database):
    if reset_database:
        if db.exists():
            db.unlink()
        subprocess.run(
            [sys.executable, "-m", f"{module}.manage", "removedevservermigrations"],
            check=True,
            env=env,
        )
        subprocess.run(
            [
                sys.executable,
                "-m",
                f"{module}.manage",
                "makemigrations",
                "-n",
                "devserver_migration",
            ],
            check=True,
            env=env,
        )

    try:
        if reset_database:
            subprocess.run(
                [sys.executable, "-m", f"{module}.manage", "migrate"],
                check=True,
                env=env,
            )
            subprocess.run(
                [sys.executable, "-m", f"{module}.manage", "loaddevserverdata"],
                check=True,
                env=env,
            )
        yield
    finally:
        if reset_database:
            subprocess.run(
                [sys.executable, "-m", f"{module}.manage", "removedevservermigrations"],
                check=True,
                env=env,
            )
        if not keep_database:
            db.unlink()
