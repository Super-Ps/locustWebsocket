from locust import Locust, events
import time, socketio

class SocketIOClient():
    
    def __init__(self):
        # self.connect_time = 0
        # self.result_time = 0
        # self.disconnect_time = 0
        self.ws = socketio.Client()
        self.ws.on("disconnect", self.on_disconnect)
        self.ws.on("compileRsp", self.on_compileRsp)

    def connect(self, burl):
        self.connect_time = time.time()
        return self.ws.connect(burl)
        
    def emit(self, event, data, namespace=None):
        return self.ws.emit(event, data, namespace)

    def wait(self):
        return self.ws.wait()

    def on_disconnect(self):
        self.disconnect_time = time.time()
        return self.ws.disconnect()

    def on_compileRsp(self, data):
        self.result_time = time.time()

    def get_result_time(self):
        return self.result_time