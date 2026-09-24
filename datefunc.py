import datetime as datetime

current_date=None

def get_date_today():

    return datetime.datetime.now(datetime.timezone.utc).date()


def set_current_date(date):
     #global variable must first be defined
    global current_date
    current_date = date


def get_current_date():
    return current_date


def date_minus_one(date):
    return date - datetime.timedelta(days=1)


def date_plus_one(date):
    return date + datetime.timedelta(days=1)

def apodify(date:datetime.date):
    return date.strftime('%y%m%d')
