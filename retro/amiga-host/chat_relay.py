"""Host-network bridge for an emulated Amiga guest.
The bridge is explicit and opt-in; it never exposes host filesystem APIs.
"""
import asyncio
from dataclasses import dataclass

@dataclass
class ChatMessage:
    peer: str
    text: str

class ChatRelay:
    def __init__(self, host="127.0.0.1", port=8765):
        self.host, self.port = host, port
        self.clients = set()

    async def _client(self, reader, writer):
        self.clients.add(writer)
        try:
            while line := await reader.readline():
                for peer in list(self.clients):
                    if peer is not writer:
                        peer.write(line)
                        await peer.drain()
        finally:
            self.clients.discard(writer)
            writer.close()
            await writer.wait_closed()

    async def serve(self):
        server = await asyncio.start_server(self._client, self.host, self.port)
        async with server:
            await server.serve_forever()
