"""Shared configuration between DAGs"""
from datetime import datetime, timedelta

IETL_GIT_SHA = "e69ba56535702d0a53437567c5893eba2c8acd89"
IETL_VERSION = (
    "git+https://imbot:aSQ56KKT2M0P@bitbucket.org/infectious/ietl.git@" + IETL_GIT_SHA
)

DEFAULT_ARGS = {
    "owner": "Data Team",
    "depends_on_past": False,
    "start_date": datetime(2019, 2, 20),
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}
