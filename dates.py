import pendulum

def period_range(start_date: pendulum.DateTime, end_date: pendulum.DateTime, step_type: str = 'months', steps: int = 2):
    if step_type not in ("years", "months", "weeks", "days", "hours", "minutes"):
        raise ValueError("Invalid step_type must be one of: years, months, weeks, days, hours, minutes")

    if steps <= 0:
        raise ValueError("steps must be greater than zero")

    period = end_date - start_date

    return period.range(step_type, steps)
