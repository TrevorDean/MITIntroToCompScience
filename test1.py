def roundfloat(number, places):
    stringnum = str(number)
    number_list = list(stringnum)
    period = stringnum.index(".")
    index_to_round = period+places+1
    number_list_int = []
    print("numberlist: ", number_list, "period:", period, "index to round:", index_to_round)
    if int(number_list[index_to_round]) >= 5:
        for x in number_list:
            if isinstance(x, int):
                number_list_int.append(x)
            else:
                number_list_int.append(".")
        int(number_list[index_to_round-1]) += 1
        print(number_list)


val1 = roundfloat(2.555, 2)
print(val1)