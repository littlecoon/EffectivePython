import json
#handle = open('tmp/random_data.txt')    # May raise IOError
#try:
#    data = handle.read()     # May raise UnicodeDecodeError
#finally:
#    handle.close()   #always runs after  try:     


def load_json_key(data,key):
    try:
        result_dict = json.loads(data)
    except ValueError as e:
        raise KeyError from e
    else:
        return result_dict[key]


data ='''{'23':'zjx','34':'ccp'}'''
test = load_json_key(data, '33')
print(test)


UNDEFINED = object()

def divide_json(path):
    handle = open(path, 'r+')
    try:
        data = handle.read()
        op = json.loads(data)
        value = (
            op['numerator']
            op['denominator'])
    except ZeroDivisionError as e:
        return UNDEFINED
    else:
        op['result'] = Value
        result = json.dumps(op)
        handle.seek(0)
        handle.write(result)
        return Value 
    finally:
        handle.close()