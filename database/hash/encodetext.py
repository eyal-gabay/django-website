from database.hash import ehash

lines = []


def file(file):
    with open(file, "r") as file:
        line = file.readline()
        while line:
            lines.append(ehash.encode(line))
            line = file.readline()
    return lines

# for i in lines:
#     print(i)
