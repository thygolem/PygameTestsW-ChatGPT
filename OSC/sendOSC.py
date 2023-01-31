from pythonosc import osc_message_builder
from pythonosc import udp_client

# Crear cliente OSC
client = udp_client.SimpleUDPClient("127.0.0.1", 4559)

# Crear mensaje OSC
msg = osc_message_builder.OscMessageBuilder(address="/test")
msg.add_arg(42)
msg = msg.build()

# Enviar mensaje
client.send(msg)
