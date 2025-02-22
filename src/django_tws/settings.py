import pathlib
import tempfile


def temporary_database_url():
    tempdir = pathlib.Path(tempfile.gettempdir())
    db = tempdir / "tws.sqlite3"
    return f"sqlite://{db}"
