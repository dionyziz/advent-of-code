with open('in.txt') as f:
  lines = f.readlines()

def safe(report):
  diffs = [b - a for a, b in zip(report, report[1:])]
  if any(diff > 0 for diff in diffs) and any(diff < 0 for diff in diffs):
    return False
  diffs = [abs(num) for num in diffs]
  return all(diff >= 1 and diff <= 3 for diff in diffs)

cnt = 0
for report in lines:
  nums = [int(num) for num in report.split()]
  for i in range(len(nums)):
    fixed = nums[:i] + nums[i+1:]
    if safe(fixed):
      cnt += 1
      break

print(cnt)
