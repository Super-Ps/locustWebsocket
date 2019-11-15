from locust import TaskSet, task, Locust, events
from socketclient import SocketIOClient
import time
import json
with open('./command.json', mode='r', encoding= 'utf-8') as f:
    command = json.load(f)
command_data = (command['mcore'][1], command['mcore'][2])

class SocketIOLocust(Locust):
    def __init__(self, *args, **kwargs):
        super(SocketIOLocust, self).__init__(*args, **kwargs)
        self.client = SocketIOClient()

class ArduinoCompileTask(TaskSet):

    @task
    def arduinoCompile(self):
        
        start_time = time.time()
        try:
            self.client.connect('http://arduinoserver-test.makeblock.com')
            resd = self.client.emit("compileReq", command_data)
            print('emitEnd',resd)
            self.client.wait()
        except Exception as e:
            total_time = int((time.time() - start_time) * 1000)
            events.request_failure.fire(request_type="socket", name='total', response_time=total_time, exception=e)
        else:
            # total_time = int((time.time() - start_time) * 1000)
            total_time = int((self.client.get_result_time() - start_time) * 1000)
            events.request_success.fire(request_type="socket", name='total', response_time=total_time, response_length=0)


class ExtServiceLocust(SocketIOLocust):
    task_set = ArduinoCompileTask
    min_wait = 5000
    max_wait = 5000