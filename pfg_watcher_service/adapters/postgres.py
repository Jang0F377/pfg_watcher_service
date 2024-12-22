from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker, Session
from pfg_watcher_service import config


def db_dsn(
    dialect: str,
    user: str,
    host: str,
    port: int,
    database: str,
    driver: str | None = None,
    password: str | None = None,
) -> str:
    scheme = dialect
    if driver:
        scheme += f"+{driver}"
    if password:
        password = f":{password}"
    else:
        password = ""

    return f"{scheme}://{user}{password}@{host}:{port}/{database}"


engine = create_engine(
    db_dsn(
        dialect=config.BACKEND_DB_DIALECT,
        user=config.BACKEND_DB_USER,
        host=config.BACKEND_DB_HOST,
        port=config.BACKEND_DB_PORT,
        database=config.BACKEND_DB_NAME,
        driver=None,
        password=config.BACKEND_DB_PASSWORD,
    ),
    poolclass=None,
)

_session_maker = sessionmaker(engine)


def get_session() -> Session:
    return _session_maker()
