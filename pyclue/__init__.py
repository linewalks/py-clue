from pyclue.connection import Connection


class CLUE:
  def __init__(self, host, port, username, password):
    self.host = host
    self.port = port
    self.username = username
    self.password = password

  def connect(self):
    return Connection(
        self.host,
        self.port,
        self.username,
        self.password
    )
