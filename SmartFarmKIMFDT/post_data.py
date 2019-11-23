def parse_keys(keys, post_inst):
    _res_dict = {}
    for k, t in keys.items():
        _res_dict[t[0]] = t[1](post_inst.get(k))
    return _res_dict

################# ITEMS TO PARSE #################

Plant_keys = {
    "type-name": ["type_name", str],
    "duration": ["duration", int],
}

##################################################

def parse_keys2(p_type, time, sensor):
    _res_dict = {}
    _res_dict["plant_type"] = str(p_type)
    _res_dict["start_plant_timestamp"] = str(time)
    _res_dict["end_plant_timestamp"] = str(time)
    _res_dict["sensor"] = str(sensor)
    _res_dict["keep_total"] = 0
    _res_dict["keep_unit"] = "none"
    _res_dict["is_harvested"] = False
    return _res_dict

def parse_keys4(date, total, unit):
    _res_dict = {}
    _res_dict["end_plant_timestamp"] = str(date)
    _res_dict["keep_total"] = int(total)
    _res_dict["keep_unit"] = str(unit)
    _res_dict["is_harvested"] = True
    return _res_dict

def parse_keys3(p_id, c_date, c_type, c_total, c_unit):
    _res_dict = {}
    _res_dict["plant_id"] = int(p_id)
    _res_dict["compost_date"] = str(c_date)
    _res_dict["compost_type"] = str(c_type)
    _res_dict["compost_total"] = int(c_total)
    _res_dict["compost_unit"] = str(c_unit)
    return _res_dict