import requests

# Super properties:
# os: Windows
# client_build_number: 420420
xsp = 'ewogICJvcyI6ICJXaW5kb3dzIiwKICAiY2xpZW50X2J1aWxkX251bWJlciI6IDQyMDQyMAp9'

# Headers- Token and Super properties
headers = {
        'authorization': 'your token here',
        'X-Super-Properties': xsp
}

# URL
url = 'https://canary.discord.com/api/v10/auth/sessions'

# GET Request
get_sessions = requests.get(url, headers=headers).json()
sessions = get_sessions['user_sessions']

# Show what it returned
for session in sessions:
    client_info = session['client_info']

    print(f'''[{sessions.index(session)}]

ID Hash: {session['id_hash']}
Last used: {session['approx_last_used_time']}

Client information>
OS: {client_info['os']}
Platform: {client_info['platform']}
Location: {client_info['location']}
------------------------------------------------------
''')
