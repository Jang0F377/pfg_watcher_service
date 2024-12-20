import sys
from apscheduler.events import (
    EVENT_SCHEDULER_STARTED,
    EVENT_SCHEDULER_SHUTDOWN,
    EVENT_SCHEDULER_PAUSED,
    EVENT_SCHEDULER_RESUMED,
    EVENT_EXECUTOR_ADDED,
    EVENT_EXECUTOR_REMOVED,
    EVENT_JOBSTORE_ADDED,
    EVENT_JOBSTORE_REMOVED,
    EVENT_JOB_ADDED,
    EVENT_JOB_REMOVED,
    EVENT_JOB_EXECUTED,
    EVENT_JOB_ERROR,
    EVENT_JOB_MISSED,
)
from pfg_watcher_service.scheduler.scheduler import get_scheduler
from pfg_watcher_service.listeners.listeners import (
    scheduler_event_listener,
    executor_event_listener,
    job_event_listener
)


def main():

    try:
        scheduler = get_scheduler()
        
        scheduler.add_listener(
            scheduler_event_listener,
            EVENT_SCHEDULER_STARTED |
            EVENT_SCHEDULER_SHUTDOWN |
            EVENT_SCHEDULER_PAUSED |
            EVENT_SCHEDULER_RESUMED
        )
        scheduler.add_listener(
            executor_event_listener,
            EVENT_EXECUTOR_ADDED | EVENT_EXECUTOR_REMOVED
        )
        scheduler.add_listener(
            job_event_listener,
            EVENT_JOBSTORE_ADDED | EVENT_JOBSTORE_REMOVED |
            EVENT_JOB_ADDED | EVENT_JOB_REMOVED | EVENT_JOB_EXECUTED | 
            EVENT_JOB_ERROR | EVENT_JOB_MISSED
        )
        
        
        scheduler.start()
    except (KeyboardInterrupt, SystemExit, EOFError):
        print("\x1b[2K", end="\r")
        print("Exiting...")
    finally:
        scheduler.shutdown()


if __name__ == "__main__":
    sys.exit(main())
