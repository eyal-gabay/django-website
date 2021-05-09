numbers = "1234567890"
other = " !@#$%^&*()_-+=/?.,<>~"
lower_to_number = "qMwNBrVtCyXuZiPoOpIaUsYdTfRgEhWjQkLlKzJxHcGvFbDnSmAe" \
                  "qMwNBrVtCyXuZiPoOpIaUsYdTfRgEhWjQkLlKzJxHcGvFbDnSmAe"
upper_to_number = "5Q7W6E4R2T5Y8U0I9O7P6A4S3D6F8G7H4J2K3L6Z4X9C8V6B5N1M"

def dehash(the_hash = "q^f9t0cqqMNDrOCJ.Op2vofO*ppIU~dLR%rL"):
    my_list = "qMwNeBrVtCyXuZiPoOpIaUsYdTfRgEhWjQkLlKzJxHcGvFbDnSmAe!@#$%^&*()_+~:{}><?/.,1234567890" \
              "qMwNeBrVtCyXuZiPoOpIaUsYdTfRgEhWjQkLlKzJxHcGvFbDnSmAe!@#$%^&*()_+~:{}><?/.,1234567890"
    list_of_list = []
    for i in range(len(the_hash)):
        loc = my_list.index(the_hash[i])
        newloc = loc - i
        list_of_list.append(my_list[newloc])
    return "".join(list_of_list)

def dehash2(the_hash):
    new_hash = []
    for e in range(len(the_hash)):
        if the_hash[e] in numbers:
            place = numbers.index(the_hash[e])
            new_hash.append(numbers[place - 1])
        elif the_hash[e] in other:
            place = other.index(the_hash[e])
            new_hash.append(other[place - 1])
        elif the_hash[e] in lower_to_number:
            place = lower_to_number.index(the_hash[e])
            new_hash.append(lower_to_number[place - 1])
        elif the_hash[e] in upper_to_number:
            place = lower_to_number.index(the_hash[e])
            new_hash.append(lower_to_number[place - 1])
    # try:
    #     del new_hash[0]
    #     del new_hash[1]
    #     del new_hash[8]
    #     del new_hash[12]
    # except:
    #     pass
    x = "".join(new_hash)[:int(len(new_hash) / 2)]
    return x[::-1]

def dehash3(the_hash):
    new_hash = the_hash[::-1]
    together = []
    after = []
    for i in range(len(the_hash)):
        together.append(tuple(zip(the_hash, new_hash))[i][0])
        together.append(tuple(zip(the_hash, new_hash))[i][1])
    x = "".join(together)
    for i in range(len(x)):
        if i % 2 == 0:
            after.append(x[i])
    y = "".join(after)
    return "".join(y)


def dehash4(the_hash):
    new_hash = []
    for long in range(len(the_hash)):
        if the_hash[long].isupper():
            new_hash.append(the_hash[long].lower())
        elif the_hash[long].islower():
            new_hash.append(the_hash[long].upper())
        elif the_hash[long] in numbers:
            new_hash.append(str(int(the_hash[long]) - 1))
        elif the_hash[long] in other:
            place = other.index(the_hash[long])
            new_hash.append(other[place - 1])
    x = "".join(new_hash)
    after = []
    for i in range(len(x)):
        if i % 2 == 0:
            after.append(x[i])
    y = "".join(after)
    return "".join(y)

