import json
import time
import gevent

import websocket

from locust import events, TaskSet, task,Locust




class WebSocketClient(object):
     
    def __init__(self, host):
        self.host = host
        self.ws = websocket.WebSocket()
        
 
    def connect(self, burl):
        start_time = time.time()
        try:
            self.conn = self.ws.connect(url=burl)
        except websocket.WebSocketTimeoutException as e:
            total_time = int((time.time() - start_time) * 1000)
            events.request_failure.fire(request_type="websockt", name='urlweb', response_time=total_time, exception=e)
        else:
            total_time = int((time.time() - start_time) * 1000)
            events.request_success.fire(request_type="websockt", name='urlweb', response_time=total_time, response_length=0)
        return self.conn
 
    def recv(self):
        return self.ws.recv()
 
    def send(self, msg):
        self.ws.send(msg)