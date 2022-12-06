with open('in.txt') as f:
  packet = f.read().strip()

for i in range(len(packet)):
  marker = packet[i:i+14]
  if len(set(marker)) == 14:
    print(i + 14)
    break
