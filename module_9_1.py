def apply_all_func(int_list, *functions):
    res_dict = {}
    for i in range(len(functions)):
        res_functions = functions[i](int_list)
        res_dict[functions[i].__name__] = res_functions
    return res_dict

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
