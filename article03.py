# 了解bytes,str与unicode的区别
import os
def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value    # Instance of str


def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value    # Instance of bytes


# 在python2中：
with open('/tmp/random.bin', 'w') as f:
    f.write(os.urandom(10))

# 在python3中：
with open('random.bin', 'wb') as f:
    f.write(os.urandom(10))

