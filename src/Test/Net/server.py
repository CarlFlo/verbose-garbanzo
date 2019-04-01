import socket
import time
import asyncio


def main():
    # Create a socket object
    s = socket.socket()
    host = socket.gethostname()
    port = 12345
    s.bind((host, port))

    # Now wait for client connection.
    s.listen(5)                 
    while True:
        # Establish connection with client.
        c, addr = s.accept()
        handleConnection(c, addr)


async def handleConnection(c, addr):
    print('Got connection from', addr)

    for x in range(5):
        string = str.format('Thank you for connecting {}', x)
        byteArray = str.encode(string)
        c.send(byteArray)
        await asyncio.sleep(.5)


    c.close()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())