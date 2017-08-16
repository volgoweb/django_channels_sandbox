import json
from channels.channel import Group

from .apps import TasksConfig


def ws_connect(message):
    Group(TasksConfig.name).add(message.reply_channel)


def ws_message(message):
    text_json = json.dumps({
        'title': message.content['text'],
        'sender': message.reply_channel.name,
    })
    context = {
        'text': text_json,
    }
    Group(TasksConfig.name).send(context)


def ws_disconnect(message):
    Group(TasksConfig.name).discard(message.reply_channel)
