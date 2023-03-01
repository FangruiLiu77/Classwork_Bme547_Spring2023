import requests


server = "http://vcm-7631.vm.duke.edu:5002"
r = requests.get(server + "/get_patients/fl118")
print(r.text)

blood_type_F8 = requests.get(server + "/get_blood_type/F8").text
blood_type_F5 = requests.get(server + "/get_blood_type/F5").text
print(blood_type_F8)
print(blood_type_F5)

out_data = {"Name": "fl118", "Match": "No"}
post_answer = requests.post(server + "/match_check", json=out_data)
print(post_answer.text)
