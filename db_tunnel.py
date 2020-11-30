from sshtunnel import SSHTunnelForwarder

DB_HOST = 'cs.westminstercollege.edu'
DB_SSH_PORT = 2322
DB_SSH_USER = 'student'
DB_PORT = 3306

# Private RSA key used for the ssh connection
PRIVATE_KEY = """-----BEGIN RSA PRIVATE KEY-----
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
-----END RSA PRIVATE KEY-----

"""

class DatabaseTunnel:
    
    def __init__(self, sshKeyfile):
        pass
    
    def open(self):
        self.tunnel = SSHTunnelForwarder(
            DB_HOST,
            ssh_username=DB_SSH_USER,
            ssh_port=DB_SSH_PORT,
            ssh_pkey=self.getKeyfile(),
            remote_bind_address=('127.0.0.1', DB_PORT)
        )
        
        self.tunnel.start()
    
    def close(self):
        self.tunnel.stop()
        
    def getForwardedPort(self):
        return self.tunnel.local_bind_port
    
    def getKeyfile(self):
        import os.path
        keyfile = 'id_rsa.cmpt307.tunnel'
        if not os.path.isfile(keyfile):
            with open(keyfile, 'w') as f:
                print(PRIVATE_KEY, file=f, end='')
        return keyfile
    
    def __enter__(self):
        self.open()
        return self
    
    def __exit__(self, *args):
        self.close()
