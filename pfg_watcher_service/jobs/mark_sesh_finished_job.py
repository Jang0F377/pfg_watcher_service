
from sqlalchemy.sql import text
from pfg_watcher_service.adapters import postgres



query = text(
    "SELECT * FROM seshes "
    "WHERE status != 'finished' "
    "AND proposed_date <= NOW()::Date "
    # "AND proposed_time <= NOW()::Time "
)


def mark_sesh_finished_job():
    db_session = postgres.get_session()
    finished_seshes = db_session.execute(query)
    print(f"finished_seshes: {finished_seshes.all()}")
    

    # for sesh in finished_seshes.scalar():
    #     print(sesh)

