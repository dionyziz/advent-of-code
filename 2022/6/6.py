with open('in.txt') as f:
  packet = f.read().strip()

for i in range(len(packet)):
  marker = packet[i:i+4]
  if len(set(marker)) == 4:
    print(i + 4)
    break
