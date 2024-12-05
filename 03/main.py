import re

test_str = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
text = test_str
if False:
    with open("input.txt", "r") as fh:
        text = fh.read()
pattern = r"mul\((\d+),(\d+)\)"

matches = re.finditer(pattern, text)

total = 0
for match in matches:
    group1 = int(match.group(1))
    group2 = int(match.group(2))
    product = group1 * group2
    total += product
    # print(f"Match: {match.group(0)}, Group 1: {group1} Group 2: {group2}")
print()
print(total)

# Part 2
test_str = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
text = test_str
if True:
    with open("input.txt", "r") as fh:
        text = fh.read()
pattern_do = r"do\(\)"
pattern_dont = r"don't\(\)"

matches_do = re.finditer(pattern_do, text, re.IGNORECASE)
matches_dont = re.finditer(pattern_dont, text, re.IGNORECASE)
matches = re.finditer(pattern, text)

indicies_do = [m.start() for m in matches_do]
indicies_dont = [m.start() for m in matches_dont]
indicies_match = dict(
    [(m.start(), (int(m.group(1)), int(m.group(2)))) for m in matches]
)

allowed = True
total = 0
for i in range(len(text)):
    if i in indicies_dont:
        allowed = False
    elif i in indicies_do:
        allowed = True
    elif i in indicies_match:
        if allowed:
            print(f"mult({indicies_match[i][0]}, {indicies_match[i][1]})")
            total += indicies_match[i][0] * indicies_match[i][1]

print(total)
breakpoint()
