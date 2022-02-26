import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from data import token, group_id
from vk_api.utils import get_random_id


class VkBot:

    def __init__(self, token, group_id):
        self.token = token
        self.group_id = group_id

        pass

    def run(self):
        vk_session = vk_api.VkApi(token=self.token)
        longpoll = VkBotLongPoll(vk_session, self.group_id)
        vk = vk_session.get_api()

        for event in longpoll.listen():

            if event.type == VkBotEventType.MESSAGE_NEW:
                print('Новое сообщение!!!')
                print(event.object['message']['text'])
                print(event)
                vk.messages.send(
                    user_id=event.object['message']['from_id'],
                    random_id=get_random_id(),
                    message='Hello'
                )

        pass


my_vk_bot = VkBot(token=token, group_id=group_id)

if __name__ == '__main__':
    my_vk_bot.run()
