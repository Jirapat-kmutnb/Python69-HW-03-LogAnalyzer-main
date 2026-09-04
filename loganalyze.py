def analyze_user_activity(log_file_path: str) -> dict:
    users = set()
    action_counts = {}
    user_total_duration = {} 
    login_durations = []

    with open(log_file_path, "r") as f: # open file 
        for line in f: # loop through each line in the file
            line = line.strip() # remove leading/trailing whitespace
            if not line: # skip empty lines
                continue

            parts = line.split() # split line into parts
            if len(parts) != 4: # check if there are 4 parts
                continue

            timestamp, user_id, action, duration_str = parts # assign parts to variables

            try:
                duration = int(duration_str) # convert duration to integer
            except ValueError:
                continue 
            users.add(user_id) # add user to set
            action_counts[action] = action_counts.get(action, 0) + 1 # increment action count
            user_total_duration[user_id] = user_total_duration.get(user_id, 0) + duration # increment user total duration

            if action == "login":
                login_durations.append(duration)

    total_users = len(users)
    most_active_user = max(user_total_duration, key=user_total_duration.get) if user_total_duration else None
    average_session_time = sum(login_durations) / len(login_durations) if login_durations else 0.0

    return {
        "total_users": total_users,
        "action_counts": action_counts,
        "most_active_user": most_active_user,
        "average_session_time": average_session_time,
    }

if __name__ == "__main__":
    result = analyze_user_activity("activity.log")
    from pprint import pprint
    pprint(result)

# {'action_counts': {'login': 2, 'logout': 2, 'submit': 1, 'view': 2},
#  'average_session_time': 160.0,
#  'most_active_user': 'u002',
#  'total_users': 2}