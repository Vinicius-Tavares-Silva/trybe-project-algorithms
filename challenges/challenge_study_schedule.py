def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None
    count = 0
    for period in permanence_period:
        begin, end = period
        if ((type(begin) or type(end)) == str) or None in period:
            return None
        if begin <= target_time <= end:
            count += 1
    return count
