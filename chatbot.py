from fbchat import Client, log
from time import sleep

# Danh sách các UID sẽ nhận được tin nhắn
uids = [
    "<UID1>",
    "<UID2>",
    "<UID3>",
    "<UID4>",
    "<UID5>"
]
# Thời gian nghỉ giữa các lần gửi tin nhắn
SLEEP_EACH_MSG = 5

from fbchat import log, Client


class EchoBot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsRead(thread_id)

        log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))

        if author_id == self.uid and thread_id == self.uid:
            for uid in uids:
                self.markAsDelivered(uid, message_object.uid)
                self.send(message_object, thread_id=uid, thread_type=thread_type)
                sleep(SLEEP_EACH_MSG)


client = EchoBot('<USERNAME>', '<PASSWORD>')
client.listen()
