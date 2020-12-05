with open('in.txt') as f:
  lines = f.read().splitlines()

password = {}
count = 0
for line in lines:
  if line == '':
    valid = (len(password) == 8) or (len(password) == 7 and 'cid' not in password)
    count += valid
    password = {}
  else:
    data = line.split(' ')
    for word in data:
      key, value = word.split(':')
      password[key] = value

print(count)
