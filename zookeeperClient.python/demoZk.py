#!/usr/bin/python
from kazoo.client import KazooClient
zk = KazooClient(hosts='127.0.0.1:2181')
zk.start()

if not zk.exists('/rabbit'):
    zk.create('/rabbit')
    zk.create('/rabbit/config')

print('Data in node: %s' % zk.get('/rabbit/config')[0])

zk.set('/rabbit/config','Hello from Python.')

# zk.delete('/rabbit/config')
# zk.delete('/rabbit')
