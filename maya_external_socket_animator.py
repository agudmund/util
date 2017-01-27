import socket    
import random

class Connect( object ):
    def __init__( self , port=4700 ):
        #self.ip = socket.gethostbyname(socket.gethostname())
        self.port = port

    def send( self , command='' ):
        """Sends a command from an external script to Maya's command port"""

        client = socket.socket( socket.AF_INET , socket.SOCK_STREAM )
        client.connect( ( "127.0.0.1" , self.port ) )
        client.send( command )

        result = client.recv( 1024 )
        #client.close()

        return result

_c = Connect()
m = 250

_c.send('python("import random;cmds.polyCube();cmds.move(random.randint(0,%s),random.randint(0,%s),random.randint(0,%s))")'%(m,m,m))
_c.send('python("cmds.select(random.choice(cmds.ls(type=\\"mesh\\")))")')

_c.send('python("cmds.move(random.randint(0,50),random.randint(0,50),random.randint(0,50))")')
_c.send('python("cmds.rotate(random.randint(0,50),random.randint(0,50),random.randint(0,50))")')
_c.send('python("cmds.scale(random.randint(1,5),random.randint(1,5),random.randint(3,5))")')
_c.send('python("import random;cmds.pointLight();cmds.move(random.randint(0,100),random.randint(0,100),random.randint(0,100))")')

#for /i %s in (1,1,5000) do python pingit.py
