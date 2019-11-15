import json
import time
import gevent

from websocket import create_connection

from locust import HttpLocust, TaskSet, task
from locust.events import request_success


with open('./command.json', mode='r', encoding= 'utf-8') as f:
    command = json.load(f)
command_data = (command['mcore'][1], command['mcore'][2])





print('command_data',command_data)
class EchoTaskSet(TaskSet):
    def on_start(self):
        ws = create_connection('http://arduinoserver-test.makeblock.com/')
        # print('ws',ws)
        self.ws = ws

        def _receive():
            while True:
                res = ws.recv()
                data = json.loads(res)
                end_at = time.time()
                response_time = int((end_at - data['start_at']) * 1000000)
                request_success.fire(
                    request_type='WebSocket Recv',
                    name='test/ws/echo',
                    response_time=response_time,
                    response_length=len(res),
                )

        gevent.spawn(_receive)

    def on_quit(self):
        self.ws.close()

    # @task
    def sent(self):
        start_at = time.time()
        # body = json.dumps({'message': 'hello, world', 'user_id': self.user_id, 'start_at': start_at})
        self.ws.send(command_data)
        request_success.fire(
            request_type='WebSocketSent',
            name='test/ws/echo',
            response_time=int((time.time() - start_at) * 1000000),
            response_length=len(command_data),
        )

class EchoLocust(HttpLocust):
    task_set = EchoTaskSet
    min_wait = 10000
    max_wait = 10000