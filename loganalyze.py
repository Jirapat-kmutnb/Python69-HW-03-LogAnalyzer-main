
from collections import defaultdict
from datetime import datetime

def analyze_user_activity(log_file_path: str) -> dict:
    user_actions = defaultdict(int)
    action_counts = defaultdict(int)
    user_sessions = defaultdict(list)

    with open(log_file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            
            # Splitting comma, tab, or space-separated log lines
            parts = line.replace(',', ' ').split()
            if len(parts) < 3:
                continue

            # Assuming log format: TIMESTAMP USER_ID ACTION
            # Example timestamp format: 2026-09-04T10:00:00 or ISO/Unix format
            timestamp_str, user_id, action = parts[0], parts[1], parts[2].lower()

            action_counts[action] += 1
            user_actions[user_id] += 1

            # Parse ISO timestamps or numeric epoch timestamps
            try:
                dt = datetime.fromisoformat(timestamp_str)
            except ValueError:
                dt = datetime.fromtimestamp(float(timestamp_str))
                
            user_sessions[user_id].append((dt, action))

    # Determine most active user by total action count
    most_active_user = max(user_actions, key=user_actions.get) if user_actions else None

    # Calculate average session durations (time between login and logout)
    session_durations = []
    for user, logs in user_sessions.items():
        logs.sort(key=lambda x: x[0])  # ensure chronological order
        login_time = None
        
        for dt, action in logs:
            if action == 'login':
                login_time = dt
            elif action == 'logout' and login_time:
                duration = (dt - login_time).total_seconds()
                session_durations.append(duration)
                login_time = None

    avg_session_time = (
        sum(session_durations) / len(session_durations)
        if session_durations else 0.0
    )

    return {
        'action_counts': dict(action_counts),
        'average_session_time': round(avg_session_time, 1),
        'most_active_user': most_active_user,
        'total_users': len(user_actions)
    }

if __name__ == "__main__":
    result = analyze_user_activity("activity.log")
    from pprint import pprint
    pprint(result)
    
# {'action_counts': {'login': 2, 'logout': 2, 'submit': 1, 'view': 2},
#  'average_session_time': 160.0,
#  'most_active_user': 'u002',
#  'total_users': 2}