#!/usr/bin/python
# -*- coding: UTF-8 -*-

import socket

myname = str(socket.getfqdn(socket.gethostname(  )))
print myname