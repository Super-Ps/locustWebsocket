from locust import Locust ,events ,task,TaskSet
from testLocustA import WebSocketClient
import json


with open('./command.json', mode='r', encoding= 'utf-8') as f:
    command = json.load(f)
command_data = (command['mcore'][1], command['mcore'][2])


class WebsocketLocust(Locust):
    def __init__(self, *args, **kwargs):
        super(WebsocketLocust, self).__init__(*args, **kwargs)
        self.client = WebSocketClient(self.host)


class SupperDianCan(TaskSet):
    
    @task
    def test_baidu(self):
        self.url = 'ws://arduinoserver-test.makeblock.com/socket.io/?transport=polling&EIO=3&t=1573719118.613421'
 
        self.data = command_data
 
        self.client.connect(self.url)
        while True:
            recv = self.client.recv()
            print('####',recv)
            # if eval(recv)['type'] == 'keepalive':
            #     self.client.send(recv)
            # else:
            self.client.send(self.data)



class WebsiteUser(WebsocketLocust):
     
    task_set = SupperDianCan
 
    min_wait=5000
 
    max_wait=9000