import time

hex_message = "747520736f727072657361207920726567616c6f206573746120656e20646973636f726420656e20232d736f756c2d667261676d656e74732c206469736672757461207920636f6d656e74616c6f2021"

print("ROOT ACCESS GRANTED...")
print("Executing: upload-memory-video-alltime.py")
print("Connecting to Discord Gateway...\n")
time.sleep(1)

print("Start uploading video into discord channel #-soul-fragments...")
percentages = [5, 18, 37, 64, 89, 99, 100]

for p in percentages:
    time.sleep(0.8) 
    print(f"Uploading... {p}%")

print("\nDone! Video successfully encrypted and deployed.")
print("-" * 50)

choice = input("Message from ADM: Do you want a clue for your gift ? [y/n]: ").strip().lower()

if choice == 'y':
    print("\nDecrypting hex payload...")
    time.sleep(1.5)
    decoded_msg = bytes.fromhex(hex_message).decode('utf-8')
    print(f"\n[ADM SYSTEM OVERRIDE]: {decoded_msg}\n")
else:
    print("\n[ADM SYSTEM]: Access granted. status: standing by. Go check Discord!! my future husband. 😉\n")