
class MailConfig:

    host = ''

    port = 0

    address = ''

    password = ''

    def __init__(self, host, port, address, password):
        self.host = host
        self.port = port
        self.address = address
        self.password = password