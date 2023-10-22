from datetime import datetime, timedelta


def do_from_today():
    return datetime.now()


def do_to_today():
    return ((datetime.now() + timedelta(days=1))
            .replace(hour=0, minute=0, second=0, microsecond=0))
