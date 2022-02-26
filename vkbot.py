import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from data import token, group_id


class VkBot:

    def __init__(self, token, group_id):
        self.token = token
        self.group_id = group_id

        pass

    def run(self):
        vk_session = vk_api.VkApi(token=self.token)
        longpoll = VkBotLongPoll(vk_session, self.group_id)

        for event in longpoll.listen():

            if event.type == VkBotEventType.MESSAGE_NEW:
                print('Новое сообщение!!!')

        pass


my_vk_bot = VkBot(token=token, group_id=group_id)

if __name__ == '__main__':
    my_vk_bot.run()
