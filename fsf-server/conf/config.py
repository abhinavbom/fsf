#!/usr/bin/env python
#
# Basic configuration attributes for scanner. Used as default
# unless the user overrides them. 
#

import socket

SCANNER_CONFIG = { 'LOG_PATH' : '/home/fsf-logs/',
                   'YARA_PATH' : '/home/fsf/fsf-server/yara/rules.yara',
                   'PID_PATH' : '/tmp/scanner.pid',
                   'EXPORT_PATH' : '/tmp',
                   'TIMEOUT' : 60,
                   'MAX_DEPTH' : 10 }

SERVER_CONFIG = { 'IP_ADDRESS' : socket.gethostname(),
        'PORT' : 5800 }
