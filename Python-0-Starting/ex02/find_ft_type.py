def all_thing_is_obj(object: any) -> int :
    # obj_type = type(object)
    # if (obj_type.__name__ == "str") :
    #     print(object, "is in the kitchen :", obj_type)
    # else :
    #     print(obj_type.__name__.capitalize(), ":", obj_type)
    match object :
        case list() :
            print("List :", type(object))        
        case tuple() :
            print("Typle :", type(object))
        case set():
            print("Set :", type(object))
        case dict():
            print("Dict :", type(object))
        case str():
            print(object, "is in the kitchen :", type(object))
        case _:
            print("Type not found")
    return (42)
