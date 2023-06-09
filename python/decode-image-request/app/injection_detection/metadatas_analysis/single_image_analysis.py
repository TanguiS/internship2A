import datetime
import time


def convert_date_str(date_str: str) -> float:
    return float(datetime.datetime.strptime(date_str, "%Y:%m:%d %H:%M:%S").timestamp())


def single_date_consistency(date_time_sec: float, max_latency: float = 60.0) -> bool:
    return time.time() - date_time_sec <= max_latency
