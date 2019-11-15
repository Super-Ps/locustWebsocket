from locust import HttpLocust, TaskSet, task 
import time
import json



with open('./command.json', mode='r', encoding= 'utf-8') as f:
    command = json.load(f)
command_data = (command['mcore'][1], command['mcore'][2])


class userAcions(TaskSet):
    def on_start(self):
        self.payload={
        
        'code':'0112XyB72mf7nQ0b0fz72PWMB722XyBx',
        'appid':'wxce0321505ba7122b',
        'secret':'10c1f3dac03673032492752add69869a',
        'grant_type':'authorization_code'
        }
    print("初始化************")


    @task
    def testA(self):
        response = self.client.post('/wx/login',data=self.payload )  
        print('1111',response)



class userInfomations(HttpLocust):
    task_set = userAcions
    print('BBBBBBBB')
    host = "http://localhost:3000"
    min_wait =3000
    max_wait = 5000

# if __name__ == "__main__":
#     print (command_data)

# print ('a',mainA())


