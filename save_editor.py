# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 16:11:46 2021

@author: osman
"""
import base64
import json
from hashlib import sha1
import hmac
key=b"ke03m!5ng93nan7p24lyg343nml2o591"

"""112c7b22f3d5a22d9025f1f349a350f70ade98b4"""

f=open("save.dat","r")
save_file=open("save_edit.dat","wb")
data= f.read()
deco_data=base64.b64decode(data).decode("utf-8")
split_data=deco_data.split("#")[0]
json_data=json.loads(split_data)

for i in range(len(list(json_data["profiles"]["def"]["resources"].keys()))):
    res_list=list(json_data["profiles"]["def"]["resources"].keys())
    res_count=json_data["profiles"]["def"]["resources"][str(res_list[i])]["count"]
    json_data["profiles"]["def"]["resources"][str(res_list[i])]["count"]+=1e200
    json_data["profiles"]["def"]["resources"][str(res_list[i])]["unlocked"]==1
    json_data["profiles"]["def"]["resources"][str(res_list[i])]["collected"]==1
    print(str(i) + ":" + res_list[i])
    print(str(i) + ":" + str(res_count))
    print(str(i) + "new " + str(json_data["profiles"]["def"]["resources"][str(res_list[i])]["count"]))
    # res_count[i]+1000

for i in range(len(list(json_data["achievements"].keys()))):
    ach_list=list(json_data["achievements"].keys())
    json_data["achievements"][str(ach_list[i])]["claimed"]=1

for i in range(len((json_data["profiles"]["def"]["unique_leaves"].keys()))):
    unq_list=list(json_data["profiles"]["def"]["unique_leaves"].keys())
    json_data["profiles"]["def"]["unique_leaves"][str(unq_list[i])]["active"]+=1
json_hmac=json.dumps(json_data)

hashed=hmac.new(key,json_hmac.encode("utf-8"),sha1)
# print(json_data["profiles"]["def"]["resources"]["platinum"])
print(hashed.hexdigest())
# print(base64.b64encode(hashed.digest()).decode())

""" Edited Save File Creation """
# print(json_hmac+"#"+hashed.hexdigest()+"#")

json_save=json_hmac+"#"+hashed.hexdigest()+"#"
json_save_b64=base64.b64encode(json_save.encode("utf-8"))
save_file.write(json_save_b64)
f.close()
save_file.close()
# print(decoder.split()[-42:])
