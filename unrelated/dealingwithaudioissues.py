import pyaudio

p = pyaudio.PyAudio()

print("Available Audio Output Devices (Speakers):")
for i in range(p.get_device_count()):
    device_info = p.get_device_info_by_index(i)
    if device_info['maxOutputChannels'] > 0:
        print(f"Device {i}: {device_info['name']}")