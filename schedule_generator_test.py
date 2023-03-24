import datetime
from schedule_generator import create_employee_schedule


def test_create_employee_schedule():
    start_date = "2020-01-30"
    expected_output = [
        datetime.datetime(2020, 1, 30, 0, 0),
        datetime.datetime(2020, 1, 31, 0, 0),
        datetime.datetime(2020, 2, 2, 0, 0),
        datetime.datetime(2020, 2, 3, 0, 0),
    ]
    assert create_employee_schedule(days=5, work_days=2, rest_days=1, start_date=start_date) == expected_output
