import pyaudio
import wave


class AudioRecorder:
    
    def __init__(self, output):
        self.CHUNK = 1024
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 2
        self.RATE = 44100
        self.output = output
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=self.FORMAT,
                        channels=self.CHANNELS,
                        rate=self.RATE,
                        input=True,
                        frames_per_buffer=self.CHUNK)
    
    def record(self, duration):
        print("* recording")
        frames = []
        for i in range(0, int(self.RATE / self.CHUNK * duration)):
            data = self.stream.read(self.CHUNK)
            frames.append(data)

        print("* done recording")

        self.wf = wave.open(self.output, 'wb')
        self.wf.setnchannels(self.CHANNELS)
        self.wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
        self.wf.setframerate(self.RATE)
        self.wf.writeframes(b''.join(frames))
        self.wf.close()

    def destroy(self):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()