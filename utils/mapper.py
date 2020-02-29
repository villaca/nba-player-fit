

def transform_responses(payload):
    list = []
    for entry in payload["data"]:
        i = 0
        dict = {}
        for field in entry:
            dict[payload["headers"][i]] = field
            i += 1
        list.append(dict)

    return list