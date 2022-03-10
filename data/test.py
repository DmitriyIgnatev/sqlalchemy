from requests import get, post, delete

print(post('http://localhost:5000/api/jobs',
           json={'id': 2,
                 'team_leader': 5,
                 'job': 'chlenosos',
                 'work_size': 15,
                 'collaborators': "23",
                 'start_date': '2022-02-26 20:52:45.132339',
                 'is_finished': 0}).json())
