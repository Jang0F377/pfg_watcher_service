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

LOG_PREFIX = "[SCHEDULER]"


class SchedulerEventCodes:
    STARTED = EVENT_SCHEDULER_STARTED
    SHUTDOWN = EVENT_SCHEDULER_SHUTDOWN
    PAUSED = EVENT_SCHEDULER_PAUSED
    RESUMED = EVENT_SCHEDULER_RESUMED


class ExecutorEventCodes:
    ADDED = EVENT_EXECUTOR_ADDED
    REMOVED = EVENT_EXECUTOR_REMOVED


class JobEventCodes:
    JOBSTORE_ADDED = EVENT_JOBSTORE_ADDED
    JOBSTORE_REMOVED = EVENT_JOBSTORE_REMOVED
    ADDED = EVENT_JOB_ADDED
    REMOVED = EVENT_JOB_REMOVED
    EXECUTED = EVENT_JOB_EXECUTED
    ERROR = EVENT_JOB_ERROR
    MISSED = EVENT_JOB_MISSED


def scheduler_event_listener(event):
    log = LOG_PREFIX
    match event.code:
        case SchedulerEventCodes.STARTED:
            log += " Started"
        case SchedulerEventCodes.SHUTDOWN:
            log += " Shutting down"
        case SchedulerEventCodes.PAUSED:
            log += " Paused"
        case SchedulerEventCodes.RESUMED:
            log += " Resuming"
        case _:
            log += " Unknown event"
    print(log)


def executor_event_listener(event):
    log = LOG_PREFIX + " Executor: "
    match event.code:
        case ExecutorEventCodes.ADDED:
            log += " Added"
        case ExecutorEventCodes.REMOVED:
            log += " Removed"
        case _:
            log += " Unknown event"
    print(log)


def job_event_listener(event):
    log = LOG_PREFIX + " Job: "
    match event.code:
        case JobEventCodes.JOBSTORE_ADDED:
            log += " Jobstore added"
        case JobEventCodes.JOBSTORE_REMOVED:
            log += " Jobstore removed"
        case JobEventCodes.ADDED:
            log += " Added"
        case JobEventCodes.REMOVED:
            log += " Removed"
        case JobEventCodes.EXECUTED:
            log += " Executed"
        case JobEventCodes.ERROR:
            log += " Error"
        case JobEventCodes.MISSED:
            log += " Missed"
        case _:
            log += " Unknown event"
    print(log)
