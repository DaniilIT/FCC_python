def add_time(start, duration, dow=None):
    start_time_row = start.split()
    start_time = [int(time) for time in start_time_row[0].split(':')]
    if start_time_row[1] == 'PM':
        start_time[0] += 12

    duration_time = [int(time) for time in duration.split(':')]
    new_time = [st + dt for st, dt in zip(start_time, duration_time)]

    if new_time[1] > 59:
        new_time[0] += 1
        new_time[1] -= 60

    days = 0
    while new_time[0] > 23:
        new_time[0] -= 24
        days += 1

    hd = 'AM'
    if new_time[0] == 0:
        new_time[0] = 12
    elif new_time[0] > 11:
        hd = 'PM'

    if new_time[0] > 12:
        new_time[0] -= 12

    new_time = f'{new_time[0]}:{new_time[1]:02} {hd}'

    dows = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    if dow:
        new_time += f', {dows[(dows.index(dow.capitalize()) + days) % 7]}'

    if days == 1:
        new_time += ' (next day)'
    elif days > 1:
        new_time += f' ({days} days later)'

    return new_time
