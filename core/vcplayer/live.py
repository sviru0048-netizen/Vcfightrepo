# =========================================
# KRISH X STAR LIVE VC PLAYER
# =========================================

import asyncio
import sounddevice as sd

from pytgcalls.types.input_stream import AudioPiped


class LiveVC:

    def __init__(self, pytgcalls, chat_id):

        self.call_py = pytgcalls
        self.chat_id = chat_id

        print("🔥 KRISH X STAR VC PLAYER LOADED")

    async def start_live(self):

        filename = "live.raw"

        samplerate = 48000
        channels = 2

        print("🎙️ LIVE VOICE STARTED")

        while True:

            recording = sd.rec(
                int(5 * samplerate),
                samplerate=samplerate,
                channels=channels,
                dtype="int16"
            )

            sd.wait()

            recording.tofile(filename)

            try:

                await self.call_py.change_stream(
                    self.chat_id,
                    AudioPiped(filename)
                )

                print("🔊 LIVE STREAMING RUNNING")

            except Exception as e:

                print(f"❌ STREAM ERROR: {e}")

            await asyncio.sleep(0.1)
