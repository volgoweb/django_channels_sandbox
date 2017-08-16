import os
import channels.asgi

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'channels_sandbox.core.settings')
channel_layer = channels.asgi.get_channel_layer()
