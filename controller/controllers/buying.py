from datetime import datetime

def validate_date_and_request_date(trans_date, date_expected):
    date = datetime.strptime(trans_date, "%Y-%m-%d").date()
    date_exp = datetime.strptime(date_expected, "%Y-%m-%d").date()

    if date > date_exp:
        raise Exception("Date Expected must not be before Transaction Date ")