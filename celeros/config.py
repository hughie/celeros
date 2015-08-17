class Default(object):
    DEBUG = False
    TESTING = False

    # NOTE : useful only for sending task. worker get URL from cmd line args
    REDIS_URL = 'redis://localhost:6379/0'
    CELERY_BROKER_URL = REDIS_URL
    CELERY_RESULT_BACKEND = REDIS_URL
    CELERY_ACCEPT_CONTENT = ['application/json']
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_RESULT_SERIALIZER = 'json'

    CELERY_ALWAYS_EAGER = False  # FOR NOW : Always put into the queue
    # TODO : ?maybe? use True to match rapp/task behavior and start locally if possible, otherwise push into queue...

    CELERY_REDIS_SCHEDULER_URL = "redis://localhost:6379/1"
    CELERY_REDIS_SCHEDULER_KEY_PREFIX = 'tasks:meta:'

class Development(Default):
    DEBUG = True


class Production(Default):
    pass


class Testing(Default):
    TESTING = True


