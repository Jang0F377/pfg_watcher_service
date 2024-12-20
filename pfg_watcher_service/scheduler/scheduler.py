import os
from datetime import timezone
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor



PFG_WATCHER_POSTGRES_URL = os.getenv("PFG_WATCHER_POSTGRES_URL")
PFG_WATCHER_POSTGRES_TABLENAME = os.getenv("PFG_WATCHER_POSTGRES_TABLENAME")



jobstores = {
    'default': SQLAlchemyJobStore(
        url=PFG_WATCHER_POSTGRES_URL,
        tablename=PFG_WATCHER_POSTGRES_TABLENAME
    )
}

executors = {
    'default': ThreadPoolExecutor(10)
}
job_defaults= {
    'coalesce': False, # default
    'max_instances': 3 # default
}




class SchedulerManager:
    _instance: BlockingScheduler | None = None

    @classmethod
    def get_scheduler(cls) -> BlockingScheduler:
        if cls._instance is None:
            cls._instance = BlockingScheduler(
                jobstores=jobstores,
                executors=executors,
                job_defaults=job_defaults,
                timezone=timezone.utc
            )
        return cls._instance

# Replace the get_scheduler function with this
get_scheduler = SchedulerManager.get_scheduler


