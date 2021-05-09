numbers = "12345678901"
other = " !@#$%^&*()_-+=/?.,<>~"
lower_to_number = "qMwNBrVtCyXuZiPoOpIaUsYdTfRgEhWjQkLlKzJxHcGvFbDnSmAe" \
                  "qMwNBrVtCyXuZiPoOpIaUsYdTfRgEhWjQkLlKzJxHcGvFbDnSmAe" \
                  "qMwNBrVtCyXuZiPoOpIaUsYdTfRgEhWjQkLlKzJxHcGvFbDnSmAe" \
                  "qMwNBrVtCyXuZiPoOpIaUsYdTfRgEhWjQkLlKzJxHcGvFbDnSmAe" \
                  "qMwNBrVtCyXuZiPoOpIaUsYdTfRgEhWjQkLlKzJxHcGvFbDnSmAe" \
                  "qMwNBrVtCyXuZiPoOpIaUsYdTfRgEhWjQkLlKzJxHcGvFbDnSmAe"
upper_to_number = "5Q7W6E4R2T5Y8U0I9O7P6A4S3D6F8G7H4J2K3L6Z4X9C8V6B5N1M"


def my_hash(the_hash = "Eyal1234#"):
    new_hash = []
    for long in range(len(the_hash)):
        if the_hash[long].isupper():
            pass
        elif the_hash[long].islower():
            pass
        elif the_hash[long] in other:
            pass
        elif the_hash[long] in numbers:
            pass
        # else:
        #     print("cant")
        #     exit()

    for long in range(len(the_hash)):
        if the_hash[long].isupper():
            new_hash.append(the_hash[long].lower())
        elif the_hash[long].islower():
            new_hash.append(the_hash[long].upper())
        elif the_hash[long] in numbers:
            new_hash.append(str(int(the_hash[long]) + 1))
        elif the_hash[long] in other:
            place = other.index(the_hash[long])
            new_hash.append(other[place + 1])
    return "".join(new_hash)


def part2(the_hash):
    new_hash = the_hash[::-1]
    together = []
    for i in range(len(the_hash)):
        together.append(tuple(zip(the_hash, new_hash))[i][0])
        together.append(tuple(zip(the_hash, new_hash))[i][1])
    # del together[len(the_hash)]
    # together.pop()
    # try:
    #     del together[2]
    #     del together[5]
    #     del together[8]
    #     del together[12]
    # except:
    #     pass
    return "".join(together)


def part3(the_hash):
    new_hash = []
    for e in range(len(the_hash)):
        if the_hash[e] in numbers:
            place = numbers.index(the_hash[e])
            new_hash.append(numbers[place + 1])
        elif the_hash[e] in other:
            place = other.index(the_hash[e])
            new_hash.append(other[place + 1])
        elif the_hash[e] in lower_to_number:
            place = lower_to_number.index(the_hash[e])
            new_hash.append(lower_to_number[place + 1])
        elif the_hash[e] in upper_to_number:
            place = lower_to_number.index(the_hash[e])
            new_hash.append(lower_to_number[place + 1])
    # try:
    #     del new_hash[0]
    #     del new_hash[1]
    #     del new_hash[8]
    #     del new_hash[12]
    # except:
    #
    #     pass
    return "".join(new_hash)[::-1] + "".join(new_hash)


def part4(the_hash):
    my_list = "qMwNeBrVtCyXuZiPoOpIaUsYdTfRgEhWjQkLlKzJxHcGvFbDnSmAe!@#$%^&*()_+~:{}><?/.,1234567890" \
              "qMwNeBrVtCyXuZiPoOpIaUsYdTfRgEhWjQkLlKzJxHcGvFbDnSmAe!@#$%^&*()_+~:{}><?/.,1234567890" \
              "qMwNeBrVtCyXuZiPoOpIaUsYdTfRgEhWjQkLlKzJxHcGvFbDnSmAe!@#$%^&*()_+~:{}><?/.,1234567890" \
              "qMwNeBrVtCyXuZiPoOpIaUsYdTfRgEhWjQkLlKzJxHcGvFbDnSmAe!@#$%^&*()_+~:{}><?/.,1234567890" \
              "qMwNeBrVtCyXuZiPoOpIaUsYdTfRgEhWjQkLlKzJxHcGvFbDnSmAe!@#$%^&*()_+~:{}><?/.,1234567890" \
              "qMwNeBrVtCyXuZiPoOpIaUsYdTfRgEhWjQkLlKzJxHcGvFbDnSmAe!@#$%^&*()_+~:{}><?/.,1234567890" \
              "qMwNeBrVtCyXuZiPoOpIaUsYdTfRgEhWjQkLlKzJxHcGvFbDnSmAe!@#$%^&*()_+~:{}><?/.,1234567890" \
              "qMwNeBrVtCyXuZiPoOpIaUsYdTfRgEhWjQkLlKzJxHcGvFbDnSmAe!@#$%^&*()_+~:{}><?/.,1234567890" \
              "qMwNeBrVtCyXuZiPoOpIaUsYdTfRgEhWjQkLlKzJxHcGvFbDnSmAe!@#$%^&*()_+~:{}><?/.,1234567890" \
              "qMwNeBrVtCyXuZiPoOpIaUsYdTfRgEhWjQkLlKzJxHcGvFbDnSmAe!@#$%^&*()_+~:{}><?/.,1234567890" \
              "qMwNeBrVtCyXuZiPoOpIaUsYdTfRgEhWjQkLlKzJxHcGvFbDnSmAe!@#$%^&*()_+~:{}><?/.,1234567890"
    list_of_list = []
    if len(the_hash) > len(my_list):
        return "too long hash"
    for i in range(len(the_hash)):
        loc = my_list.index(the_hash[i])
        newloc = loc + i
        list_of_list.append(my_list[newloc])
    return "".join(list_of_list)





