import requests


outdata = {"user": "Fangrui", "message": "Hello, this is Fangrui"}

r = requests.post("http://vcm-21170.vm.duke.edu:5001/add_message",
                  json=outdata)
print(r.text)

r_get = requests.get("http://vcm-21170.vm.duke.edu:5001/get_messages/Bill")
print(r_get.text)
