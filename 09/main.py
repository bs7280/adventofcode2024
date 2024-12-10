def p1(data):
    file_blocks = {}
    free_blocks = []
    file_id = 0
    disk_map = []
    for i, d in enumerate(data):
        if i % 2 == 0:
            disk_map += [str(file_id)] * int(d)
            file_id += 1
        else:
            disk_map += ["."] * int(d)
            free_blocks.append((i, int(d)))
    print("".join(disk_map))

    # Fold left and right to track empty spaces and latest file
    empty_pos = 0
    latest_file = len(disk_map) - 1

    iters = 0
    while latest_file > empty_pos:
        if disk_map[empty_pos] != ".":
            empty_pos += 1
        if disk_map[latest_file] == ".":
            latest_file -= 1

        if (disk_map[empty_pos] == ".") and (disk_map[latest_file] != "."):
            file_id = disk_map[latest_file]
            disk_map[empty_pos] = file_id
            disk_map[latest_file] = "."
            empty_pos += 1
            latest_file -= 1

        i += 1
        if i > len(disk_map) + 100:
            breakpoint()

    # Get checksum
    print(sum([i * int(d) for i, d in enumerate(disk_map) if d != "."]))


def p2(data):
    file_blocks = []
    free_blocks = []
    file_id = 0
    disk_map = []
    for i, d in enumerate(data):
        if i % 2 == 0:
            file_blocks.append(
                {
                    "file_id": file_id,
                    "start": len(disk_map),
                    "end": len(disk_map) + int(d),
                }
            )
            disk_map += [str(file_id)] * int(d)
            file_id += 1
        else:
            free_blocks.append((len(disk_map), len(disk_map) + int(d)))
            disk_map += ["."] * int(d)
    # print("".join(disk_map))

    # Fold left and right to track empty spaces and latest file
    for file in file_blocks[::-1]:
        blocksize = file["end"] - file["start"]
        # Loop through all free blocks left to right
        for i, b in enumerate(free_blocks):
            if b[1] - b[0] >= blocksize and b[0] < file["start"]:
                # Swap above
                for j in range(blocksize):
                    disk_map[b[0] + j] = str(file["file_id"])
                # disk_map[b[0] : b[0] + blocksize] = disk_map[
                #    file["start"] : file["end"]
                # ]
                for j in range(blocksize):
                    disk_map[file["start"] + j] = "."
                # disk_map[file["start"] : file["end"]] = ["."] * blocksize

                # Pop off the free block
                if b[1] - b[0] == blocksize:
                    free_blocks.pop(i)
                    break
                else:
                    free_blocks[i] = (b[0] + blocksize, b[1])
                    break

        # print("".join(disk_map))
    # print("".join(disk_map))

    print(sum([i * int(d) for i, d in enumerate(disk_map) if d != "."]))


with open("data.txt") as f:
    data = f.read()

# Each file can have at most of 9 blocks?
# every other number is a file block, the others are empty blocks
test_data = "2333133121414131402"
test_data = "12345"

p1(test_data)

p2(data)
