import pprint

count_1 = 0
count_2 = 0
count_3 = 0

with open("1.txt", encoding= "utf-8")as f_1:
    for line in f_1:
        count_1 += 1
    file_name_1 = "1.txt"

    with open(file_name_1, "r", encoding= "utf-8")as f_1:
        
        data_1 = [line.rstrip() for line in f_1.readlines()]
        print(data_1)


with open("2.txt", encoding= "utf-8")as f_2:

    for line in f_2:
        count_2 += 1
    file_name_2 = "2.txt"

    with open(file_name_2, "r", encoding= "utf-8")as f_2:
        data_2 = [line.rstrip() for line in f_2.readlines()]
        print(data_2)

with open("3.txt", encoding= "utf-8")as f_3:

    for line in f_3:
        count_3 += 1
    file_name_3 = "3.txt"

    with open(file_name_3, "r", encoding= "utf-8")as f_3:

        data_3 = [line.rstrip() for line in f_3.readlines()]
        print(data_3)



dict_1 = {"name": file_name_1,"quantity": count_1 , "data": data_1, }
dict_2 = {"name": file_name_2,"quantity": count_2 , "data": data_2, }
dict_3 = {"name": file_name_3,"quantity": count_3 , "data": data_3, }

dict_list = [dict_1, dict_2, dict_3]
sorted_dict_list = sorted(dict_list, key=lambda x: x["quantity"])

# print(sorted_dict_list)

with open("result.txt", "w", encoding= "utf-8") as f:
    for dict in sorted_dict_list:

        f.write(f"{dict["name"]}\n")
        f.write(f"{dict["quantity"]}\n")
        f.writelines(f"{string}\n" for string in dict["data"])

