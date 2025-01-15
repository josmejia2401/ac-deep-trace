from src.main.main import Main

socket = None
try:
    socket = Main()
    socket.run()
except KeyboardInterrupt as ex:
    print(ex)
    socket.stop()