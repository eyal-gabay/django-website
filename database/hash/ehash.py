from database.hash import the_ehash, deehash, encodetext

encode = lambda hash: the_ehash.part4(the_ehash.part3(the_ehash.part2(the_ehash.my_hash(hash))))
decode = lambda hash: deehash.dehash4(deehash.dehash3(deehash.dehash2(deehash.dehash(hash))))
# file = lambda file: encodetext.file(file)

if __name__ == '__main__':
    print(encode("eyal1"))
    print(encode("eyal12"))
    print(encode("eyal12%"))
    print(decode("h*f7t8cGqZNL?Gv,xysX$%iROSq%"))
    # lines = file("text")
    # for i in lines:
    #     print(i)
# 3q6M9wMNeeVByrZVtoXOipOIaaYUfsEY
# 306q9MMweNVeyBrZCiuPPopOUpdI