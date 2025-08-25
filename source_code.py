import sounddevice
from scipy.io.wavfile import write
import os

# Create music directory if it doesn't exist
music_dir = "music"
if not os.path.exists(music_dir):
    os.makedirs(music_dir)

fs = 44100  # sample_rate
second = int(input(" Please enter the duration of time in second: ")) 
print("Recording has started ....\n")
record_voice = sounddevice.rec(int(second * fs), samplerate=fs, channels=2)
sounddevice.wait()

# Save to music folder
output_path = os.path.join(music_dir, "out.wav")
write(output_path, fs, record_voice)
print(f"Recording has Finished ....\nPlease check it in the '{music_dir}' folder.")
