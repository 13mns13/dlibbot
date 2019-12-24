import vk_api
import time, codecs
import os, sys, shutil, requests
import os.path, json, dlib

ff=codecs.open('ids.txt', 'w', encoding='utf8')

def main(token):
    res = ""
    for i in range(1, 574000000):
        if i%501==0:
            response(token, res[:len(res)-2])
            res =""
        else: res+="{}, ".format(i)  

def response(token, i):
    res = ""
    id = i
    try:
        items = requests.get("https://api.vk.com/method/users.get",params={
        "access_token":token, "user_ids":id, "fields":"photo_max_orig", "offset":0, "v":5.103}).json()["response"]

        for i in range(len(items)):
            res+="{}|{}|{} {}\n".format(items[i]["id"], items[i]["photo_max_orig"],items[i]["first_name"],items[i]["last_name"])
        print(id[id.rfind(",")+1:])
    except:
        pass
    f = open("ids.txt", "a",encoding='utf8')
    f.write(res)
    f.close()
        

main("token_id")

print('Done!')
