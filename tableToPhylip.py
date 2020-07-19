#!/usr/bin/python3

import sys
import os


def get_areas_dictionary(tab_file):
    '''
    This function creates a dictionary with species names as keys
     and lists of  species ranges as values.
    '''
    sp_area_dic = {}
    
    for i in range(1,len(tab_file)):
        tmp_line = tab_file[i].split()
        sp_name = tmp_line[0]
        sp_range = [x.strip(",") for x in tmp_line[1:]]
        sp_area_dic[sp_name] = sp_range
    return sp_area_dic


def get_areas_list(areas_dictionary):
    '''
    This function creates a list of unique entries (names of the areas)
    '''
    area_list = []
    
    for key in areas_dictionary.keys():
        for val in areas_dictionary[key]:
            val_mod = val.rstrip(",").lstrip(",").lower().rstrip().lstrip()
            if val_mod not in area_list:
                area_list.append(val_mod)
    return sorted(area_list)


def distribution_code(areas_dict, list_areas):
    '''
    this function creates a dictionary with species names as keys and
     codes for presence/absence in a specific area as values
    '''
    codeMatrix = {k:"" for k in areas_dict.keys()}

    for area in list_areas:
        for key in areas_dict.keys():
            temp_list = []
            for value in areas_dict[key]:
                mod_value = value.rstrip(",").lstrip(",").lower().rstrip().lstrip()
                temp_list.append(mod_value)
            if area in temp_list:
                codeMatrix[key] = codeMatrix[key] + str(1)
            else:
                codeMatrix[key] = codeMatrix[key] + str(0)
            temp_list = []

    return codeMatrix


def write_file(dist_code, list_areas, name):
    '''
    This function creates a phylip formated file of spcies and distribution code
    '''
    areasNames = " ".join(list_areas)
    fext = os.path.splitext(name)[-1]
    base_fn = os.path.split(name)[-1]

    with open(base_fn.replace(fext, "_TABLE.txt"), "w") as out:
        out.write("{}\t{} ({})\n".format(len(dist_code), len(list_areas), areasNames))
        for key in dist_code.keys():
            out.write("{}\t{}\n".format(key, dist_code[key]))


if __name__ == "__main__":
    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
    dictionary_of_areas = get_areas_dictionary(data)
    list_of_areas = get_areas_list(dictionary_of_areas)
    list_of_codes = distribution_code(dictionary_of_areas, list_of_areas)
    write_file(list_of_codes, list_of_areas, sys.argv[1])