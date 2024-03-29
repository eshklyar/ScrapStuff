def correct(s):
    # substitutions = {"5": "S", "0": "O", "1": "I"}
    # return ''.join([substitutions.get(c, c) for c in s])
    substitutions = {"5": "S", "0": "O", "1": "I"}
    return ''.join([substitutions.get(c, c) for c in s])

def trans(s):
    table = str.maketrans("IAEO".lower(), "1@30")
    tr = s.translate(table)
    return tr

print(trans("edik"))
    # for c in s:
    #     # print(substitutions.keys())
    #     for x in substitutions.keys():
    #         if str(x) == c:.
    #             print(f" c is {c} and value is {substitutions.get(int(c))}")
    #         else:
    #             print(c)


    # print(f"substitutions.keys() {substitutions.keys()}")
    # print(f"substitutions.items() {substitutions.fromkeys()}")

    # for c in s:
        # if c in substitutions.keys()

    # x = [c for c in s if c in substitutions.keys()]
    # print(x)
    # return ''.join({5: "S", 0: "O", 1: "I"}.get(c, c) for c in s)


print(correct("DUBL1N"))

    # match status:
    #         case 400:
    #             return "Bad request"
    #         case 404:
    #             return "Not found"
    #         case 418:
    #             return "I'm a teapot"
    #
    #
    # "".join([])
    # lang = input("What's the programming language you want to learn? ")
    #
    # match lang:
    #     case "JavaScript":
    #         return "haha"




# int day = 4;
#   switch (day) {
#   case 1:
#     cout << "Monday";
#     break;
#   case 2:

def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"

        # If an exact match is not confirmed, this last case will be used if provided
        case _:
            return "Something's wrong with the internet"