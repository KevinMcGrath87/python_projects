


def make_list(*args, **kwargs):
    myList = []
    for each in args, kwargs:
        myList.append(each)
    for x in args:
        print(x)
    for each in myList:
        print(each)

make_list("x", "you", "zed zed", 0, mammet = 'banana', larang = "isotope")