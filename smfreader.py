import json

class SMFReader:
    def read(self, smfrecord):
        raise NotImplementedError


def counter(f):
    count = 0
    def decorator(*args):
        nonlocal count
        count += 1
        print(count)
        return f(*args)

    return decorator


class SMF030Reader(SMFReader):
    @counter
    def read(self, smfrecord):
        header_file = open("./layout/header.json")
        header_obj = json.load(header_file)
        return header_obj