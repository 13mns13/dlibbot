from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType 
import vk_api, json, requests,  random 

vk = vk_api.VkApi(token="ce9f69be5936ff4e75d66ca746b94a962ef0b9049b3d009728d4642921ab595d3d6c8de2bbd699200accf")
vk._auth_token()
vk.get_api()
longpoll = VkBotLongPoll(vk,189998531)

def get_button(label, color, payload=""):
    return dict(action=dict(type="text", payload=json.dumps(payload), label=label), color=color)

class vk_bot:
    def main(self):
        for event in longpoll.listen():
            
                if event.type == VkBotEventType.MESSAGE_NEW:
                    if event.object.peer_id != event.object.from_id:
                        id = event.object.peer_id
                    elif event.object.peer_id == event.object.from_id:
                        id = event.object.from_id
                    body = event.object.text
                    self.switch(id, body)

    def send_messages(self, id, text):
        vk.method('messages.send',{'peer_id': id,'message':text,'random_id':0})           
    
    def random_text(self):
        a = ["тест"]
        res = a[random.randint(0,len (a)-1)]
        return res
    
    def push_chat(self, id):
        a = vk.method('messages.getConversationMembers',{'peer_id': id, 'group_id':189998531})
        profiles = a["profiles"]
        res = self.random_text()
        for i in range(len(profiles)):
            res += "@id{}(&#8300;)\n".format(profiles[i]['id'])
        self.send_messages(id, res)

    def switch(self, id, body):
        if "!!" == body[0:2]:
            self.push_chat(id)

if __name__ == "__main__":
    print("Запущен.")
    api = vk_bot();
    while True: 
        api.main()
