# https://www.hackinscience.org/exercises/bencode-bdecode

def _bencode_int(i: int) -> bytes:
    return bytes(f'i{i}e', 'UTF-8')

def _bencode_str(s: str) -> bytes:
    size = len(bytes(s, 'UTF-8'))
    return bytes(f'{size}:{s}', 'UTF-8')

def _bencode_list(l: list) -> bytes:
    res = b'l'
    for i in l:
        res += bencode(i)
    return res + b'e'

def _bencode_dict(d: dict) -> bytes:
    res = b'd'
    for key, value in d.items():
        res += bencode(key) + bencode(value)
    return res + b'e'

def bencode(elem) -> bytes:
    if isinstance(elem, int):
        return _bencode_int(elem)
    elif isinstance(elem, str):
        return _bencode_str(elem)
    elif isinstance(elem, list):
        return _bencode_list(elem)
    elif isinstance(elem, dict):
        return _bencode_dict(dict(sorted(elem.items())))
    else:
        raise ValueError(f"Cannot bencode {elem}")

    
def _bdecode_int(enc: str) -> tuple[int, str]:
    ipos = enc.find('e')
    if ipos == -1:
        raise ValueError(f"Cannot bdecode {enc}")
    return int(enc[1:ipos]), enc[ipos+1:]

def _bdecode_str(enc: str) -> tuple[str, str]:
    semic_pos = enc.find(':')
    if semic_pos == -1:
        raise ValueError(f"Cannot bdecode {enc}")
    size = int(enc[:semic_pos])
    return enc[semic_pos+1:semic_pos+size+1], enc[semic_pos+size+1:] 

def _bdecode_list(enc: str) -> tuple[list, str]:
    res = []
    enc = enc[1:]
    while enc[0] != 'e':
        tmp, enc = _bdecode(enc)
        res += [tmp]
    return res, enc[1:]

def _bdecode_dict(enc: str) -> tuple[dict, str]:
    res = {}
    enc = enc[1:]
    while enc[0] != 'e':
        key, enc = _bdecode(enc)
        value, enc = _bdecode(enc)
        res[key] = value
    return res, enc[1:]

def _bdecode(enc: str) -> tuple[any, str]:
    if enc[0] in '0123456789':
        return _bdecode_str(enc)
    elif enc[0] == 'i':
        return _bdecode_int(enc)
    elif enc[0] == 'l':
        return _bdecode_list(enc)
    elif enc[0] == 'd':
        return _bdecode_dict(enc)
    else:
        raise ValueError(f"Cannot bdecode {enc}")
    
def bdecode(enc: bytes) -> any:
    return _bdecode(enc.decode('UTF-8'))[0]

if __name__ == "__main__":
    test_obj = {
        "2":"yolo",
        "list":[-42,"foo"], 
        "num": 4,
        "test":{"tt":"qq"}
    }
    test_benc = b'd1:24:yolo4:listli-42e3:fooe3:numi4e4:testd2:tt2:qqee'
    enc = bencode(test_obj)
    print(enc)
    assert(enc == test_benc)
    dec = bdecode(enc)
    print(dec)
    assert(dec == test_obj)