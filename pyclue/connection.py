import grpc


class Connection:
  def __init__(self, host, port, username, password):
    self.host = host
    self.port = port
    self.username = username
    self.password = password

  def connect(self):
    channel = grpc.insecure_channel(f"{self.host}:{self.port}")
    
    

