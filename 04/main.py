import datetime
import re
from helpers.get_input import get_lines


def do_main(debug_mode=False):
    lines = get_lines('04', debug_mode)

    events = {}
    lines = sorted(lines)
    id = None

    for line_index, line in enumerate(lines):
        timestamp = re.search(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}", line)[0]
        date_time = datetime.datetime.strptime(timestamp, "%Y-%m-%d %H:%M")
        if re.search(r"#\d+", line):
            id = re.search(r"#\d+", line)[0]
            if date_time.hour == 23:
                date_time += datetime.timedelta(days=1)
            date_time = date_time.replace(hour=0, minute=0)
        event = "asleep" if "asleep" in line else "awake"

        if id not in events:
            events[id] = {}
        if date_time.date() not in events[id]:
            events[id][date_time.date()] = {"events":{}, "times":[]}
        events[id][date_time.date()]["events"][date_time.minute] = event

    total_sleep = {}
    good_minutes_all = {}
    good_minutes_max = 0
    good_minutes_max_id = ""
    good_minutes_max_minute = 0
    for id in events:
        total_sleep[id] = 0
        good_minutes_all[id] = [0 for _ in range(60)]
        for day in events[id]:
            for i in range(60):
                closest = max((x for x in events[id][day]["events"].keys() if x <= i))
                asleep = True if events[id][day]["events"][closest] == "asleep" else False
                events[id][day]["times"].append(asleep)
                if asleep:
                    total_sleep[id] += 1
                    good_minutes_all[id][i] += 1
        if max(good_minutes_all[id]) > good_minutes_max:
            good_minutes_max = max(good_minutes_all[id])
            good_minutes_max_id = id
            good_minutes_max_minute = good_minutes_all[id].index(max(good_minutes_all[id]))

    id_with_max_sleep = max(total_sleep, key=total_sleep.get)
    good_minute = good_minutes_all[id_with_max_sleep].index(max(good_minutes_all[id_with_max_sleep]))
    print(good_minute * int(id_with_max_sleep[1:]))

    print(int(good_minutes_max_id[1:])*good_minutes_max_minute)


if __name__ == '__main__':
    do_main(False)