from channels.routing import route

channel_routing = {
    'websocket.connect': 'tasks.consumers.ws_connect',
    'websocket.receive': 'tasks.consumers.ws_message',
    'websocket.disconnect': 'tasks.consumers.ws_disconnect',
}
