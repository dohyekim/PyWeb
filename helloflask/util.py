from datetime import datetime, date, timedelta

# example: localhost:5000/dt?date=2019-02-09
def ymd(fmt):
    def trans(date_str):
        return datetime.strptime(date_str, fmt)
    return trans
