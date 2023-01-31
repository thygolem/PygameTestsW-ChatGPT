from pythonosc import dispatcher
from pythonosc import osc_server
import threading


def handle_message(address, *args):
    print("Mensaje recibido en dirección {} con argumentos {}".format(address, args))

# Crear dispatcher
dispatcher = dispatcher.Dispatcher()
dispatcher.map("/test", handle_message)

# Crear servidor OSC
server = osc_server.ThreadingOSCUDPServer(("127.0.0.1", 4559), dispatcher)

# Iniciar servidor en segundo plano
print("Serving on {}".format(server.server_address))
server_thread = threading.Thread(target=server.serve_forever)
server_thread.start()
