import os


def when_ready(server):
    open("/tmp/app-initialized", "w").close()


worker_class = "gevent"
workers = int(os.environ.get("WORKERS", "1"))
threads = int(os.environ.get("THREADS", "1"))

worker_tmp_dir = "/dev/shm"
chdir = "quizhero-api"

max_requests = int(os.environ.get("GUNICORN_MAX_REQUESTS", "1000"))
max_requests_jitter = int(os.environ.get("GUNICORN_MAX_REQUESTS_JITTER", "25"))
graceful_timeout = 30
