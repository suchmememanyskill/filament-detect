from controllers.controller import Controller
import socket
import json
import time
import logging
import os

from runtime import Runtime

MESSAGE_REGISTER_AGENT = {
    "jsonrpc": "2.0",
    "method": "server.connection.identify",
    "params": {
        "client_name": "filament-detect",
        "version": "0.0.1",
        "type": "agent",
        "url": "https://github.com/suchmememanyskill/filament-detect"
    },
    "id": 4656
}

MESSAGE_REGISTER_REMOTE_COMMAND = {
    "jsonrpc": "2.0",
    "method": "connection.register_remote_method",
    "params": {
        "method_name": "filament_start_detecting"
    }
}

class MoonrakerRemoteMethodController(Controller):
    def __init__(self, config: dict):
        super().__init__(config)
        self.moonraker_socket_path = str(config["moonraker_socket_path"])
        self.socket =  socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.runtime : Runtime

    def loop(self):
        while not os.path.exists(self.moonraker_socket_path):
            logging.warning(f"Moonraker socket not found at {self.moonraker_socket_path}, retrying in 2 seconds...")
            time.sleep(2)

        self.socket.connect(self.moonraker_socket_path)
        time.sleep(0.1)
        self.socket.sendall(json.dumps(MESSAGE_REGISTER_AGENT).encode("utf-8") + b'\x03')
        time.sleep(0.1)
        self.socket.sendall(json.dumps(MESSAGE_REGISTER_REMOTE_COMMAND).encode("utf-8") + b'\x03')
        time.sleep(0.1)

        while True:
            data = self.socket.recv(4096)
            if not data:
                raise Exception("Moonraker socket connection closed")
            
            try:
                # TODO: It's possible we are receiving a partial message. Should probably wait til we receive \x03
                
                data = data.rstrip(b"\x03")

                #with open("/tmp/last_moonraker_message.bin", "wb") as f:
                #    f.write(data)

                message_str = data.decode("utf-8").strip()
                logging.debug(f"Received data from Moonraker socket: '{message_str}'")
                message = json.loads(message_str)
                if "method" in message and message["method"] == "filament_start_detecting":
                    params = message.get("params", {})
                    channel = params.get("channel", None)
                    if channel is not None:
                        self.runtime.start_reading_tag(channel)
            except Exception as e:
                print(f"Error processing message: {e}")