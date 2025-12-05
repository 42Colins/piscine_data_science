def NULL_not_found(object: any) -> int:
    if object != object:
        print("Cheese : nan", type(object))
        return 0
    match object:
        case None:
            print("Nothing : None", type(object))
        case False:
            print("Fake : False", type(object))
        case 0:
            print("Zero : 0", type(object))
        case str():
            if (len(object) == 0):
                print("Empty :", object, type(object))
            else:
                print("Type not Found")
                return 1
        case _:
            print("Type not Found")
            return 1
    return (0)
