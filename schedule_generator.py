import logging
from datetime import datetime, timedelta


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename="schedule_generator.log",
)


class InvalidInputError(Exception):
    pass


def create_employee_schedule(days: int, work_days: int, rest_days: int, start_date: datetime) -> list[datetime]:
    """
    Given the number of working days per week for an employee, this function creates a schedule for a specified number of days 
    from a starting date. The schedule will include work days and rest days based on the number of work days per week and the 
    number of rest days per week.
    
    Args:
    - days: A positive integer representing the number of days to include in the schedule.
    - work_days: A positive integer representing the number of days the employee will work each week.
    - rest_days: A positive integer representing the number of days the employee will rest each week.
    - start_date: A datetime object representing the starting date for the schedule.
    
    Returns:
    - A list of datetime objects representing the schedule for the employee.
    """
    try:
        start_datetime = datetime.strptime(start_date, "%Y-%m-%d")
    except ValueError:
        logging.exception("Invalid date provided. Expected date format is: YYYY-MM-DD.")
        raise InvalidInputError("Invalid date provided. Expected date format is: YYYY-MM-DD.")
    
    try:
        if not all(isinstance(arg, int) and arg > 0 for arg in [days, work_days, rest_days]):
            raise InvalidInputError('All arguements should be numbers greater than zero!')
    
        schedule = []
        # Determine the number of weeks required based on the total number of days and the work and rest days per week
        weeks = days // (work_days + rest_days)
        
        # Loop through each week and add work and rest days accordingly
        for i in range(weeks):
            # Add work days
            for j in range(work_days):
                schedule.append(start_datetime)
                start_datetime += timedelta(days=1)
                
            # Add rest days
            for k in range(rest_days):
                start_datetime += timedelta(days=1)
        
        # Add any remaining work days if necessary
        remaining_days = days % (work_days + rest_days)
        for l in range(remaining_days):
            schedule.append(start_datetime)
            start_datetime += timedelta(days=1)
    
        return schedule
    except InvalidInputError:
        logging.exception(f'Invalid input arguments provided. Details: {days} {work_days} {rest_days}')
        raise InvalidInputError('Invalid input arguments provided. Arguments should be positive integers.')
