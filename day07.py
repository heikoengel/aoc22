import json

with open("data07") as f:
    input = f.readlines()

filetree = []
cwd = []

# Build a file tree as a list of {path, size, type}
for line in input:
    if line.endswith("\n"):
        line = line[:-1]
    if line.startswith("$ ls"):
        continue  # ignore 'ls' command line, only parse output below
    elif line.startswith("dir"):
        continue  # ignore directories in the listing, no size information here
    elif line.startswith("$ cd"):  # dir command
        dest = line.split()[-1]
        if dest == "..":
            cwd = cwd[:-1]  # one level up
        else:
            cwd.append(dest)
            # add a trailing '/' in case there are files with the same name
            path = "/".join(cwd) + "/"
            filetree.append({'path': path, 'type': 'dir', 'size': 0})
    else:
        size, filename = line.split()
        path = "/".join(cwd) + "/" + filename
        filetree.append({'path': path, 'size': int(size), 'type': 'file'})

# calculate folder sizes from all files in subfolders
for entry in filetree:
    if entry['type'] != 'dir':
        continue  # only iterate over folders
    # get a list of all files within this directory
    subfiles = [x for x in filetree if (x['path'].startswith(entry['path']) and
                                        x['type'] == 'file')]
    # set folder size to sum of file sizes
    entry['size'] = sum([x['size'] for x in subfiles])

# Part 1
print(sum([x['size'] for x in filetree if (x['size'] <= 100000 and
                                           x['type'] == 'dir'])))

# Part 2
total_size = filetree[0]['size']
to_be_freed = total_size - (70000000 - 30000000)
min_size = min([x['size'] for x in filetree if (x['size'] >= to_be_freed and
                                                x['type'] == 'dir']))
print(min_size)
