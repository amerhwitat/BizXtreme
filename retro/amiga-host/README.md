# Amiga network + RNN bridge

The emulator remains the CPU/device boundary. A separate host adapter can
provide opt-in TCP chat and an RNN/LLM assistant. It does not inject code into
the guest, expose host files, or bypass emulator isolation.

Default chat endpoint: 127.0.0.1:8765. Bind to a LAN address only after the
operator explicitly configures firewall/authentication controls.
