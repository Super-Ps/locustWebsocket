

from locust import HttpLocust, TaskSet, task ,events ,TaskSequence
import json
from locust import web

@web.app.route("/added_page")
def my_added_page():
    return "Another page"
# class MyTaskSequence(TaskSequence):
#     @seq_task(1)
#     def first(self):
#         print('sequence11')
#     @seq_task(2)
#     def first(self):
#         print('sequence11')

class MyTaskSet(TaskSet):
    
    def on_start(self):
        self.payload={
            
            'code':'0112XyB72mf7nQ0b0fz72PWMB722XyBx',
            'appid':'wxce0321505ba7122b',
            'secret':'10c1f3dac03673032492752add69869a',
            'grant_type':'authorization_code'
            }
        print("初始化************")

    # @task(5)
    # def homePage(self):
    #     self.client.get('/')
        
    @task(5)
    def homePageB(self):

        response = self.client.post('/wx/login',data=self.payload ,catch_response=True)  
        print ('******',response.status_code)
        if response.ok:
            print('res',type(response),'res2',response.headers)
            result = response.json()
            print('result',result,'type',type(result) )

            if result['bodydata']['grant_type'] == 'aauthorization_code':
                response.success()
            else:
                response.failure('error')


    def on_stop(self):
        print('结束了**********')
# class WebsiteUser(HttpLocust):
    

#     # def __init__():
#     print('AAAAAAAA')
#     task_set = MyTaskSet
#     host = "https://test2-www.makex.cc/zh"
#     min_wait =5000
#     max_wait = 10000

class WebsiteUserB(HttpLocust):
    print('BBBBBBBB')
    task_set = MyTaskSet
    host = "http://localhost:3000"
    min_wait =3000
    max_wait = 5000



    


