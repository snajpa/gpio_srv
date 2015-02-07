#!/usr/bin/env python

from twisted.internet import reactor, protocol
from twisted.protocols.basic import LineReceiver

from gpio import on, off, setup, valid


def decode(msg):
    msg, val = msg[0], msg[1:]
    try:
        val = int(val)
    except:
        val = None
    return (msg, val)



def handle(msg, val):
    if msg == 'e':
        if valid(val):
            print('enable:{0}'.format(val))
            on(val)
        else:
            print('out of range')

    elif msg == 'd':
        if valid(val):
            print('disable:{0}'.format(val))
            off(val)
        else:
            print('out of range')
    else:
        print('unknown cmd')


class GPIO(LineReceiver):

    def dataReceived(self, data):
        if len(data) >= 2:
            msg, val = decode(data)
            handle(msg, val)
            self.transport.write('ok\n')
        else:
            self.transport.write('nak\n')


PORT = 8008


def main():
    factory = protocol.ServerFactory()
    factory.protocol = GPIO
    reactor.listenTCP(PORT, factory)
    print 'Setup'
    setup()
    print 'Listening on {0}'.format(PORT)
    reactor.run()

if __name__ == '__main__':
    main()
