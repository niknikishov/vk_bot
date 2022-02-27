from pprint import pprint

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
                # pprint(event)
                try:
                    if event.type == VkBotEventType.MESSAGE_NEW:
                        print(f"Новое сообщение от {event.object['message']['from_id']}!!!")
                        print(event.object['message']['text'])
                        # print(event)

                        vk.messages.send(
                            user_id=event.object['message']['from_id'],
                            random_id=get_random_id(),
                            message='Hello'
                        )
                    elif event.type == VkBotEventType.MESSAGE_TYPING_STATE:
                        print(f"{event.object['from_id']} печатает... для {event.object['to_id']}")
                        # print(event.object['message']['text'])
                        # print('i am here')
                        # print(event)
                        # vk.messages.send(
                        #     user_id=event.object['message']['from_id'],
                        #     random_id=get_random_id(),
                        #     message='Hello'
                        # )
                    elif event.type == VkBotEventType.MESSAGE_REPLY:  # возникает в случае отправки сообщения ботом
                        print('Новое сообщение:')               # событие типа ответ

                        print('От меня для: ', end='')

                        print(event.object['peer_id'])

                        print('Текст:', event.obj.text)
                        print()
                    else:
                        print(event)
                        print(f'Получено неизвестное событие')
                        # vk.messages.send(
                        #     user_id=event.object['message']['from_id'],
                        #     random_id=get_random_id(),
                        #     message='не знаю такую команду'
                        # )
                except Exception as err:
                    print('Error', err.args)
                    pass


my_vk_bot = VkBot(token=token, group_id=group_id)

if __name__ == '__main__':
    my_vk_bot.run()
