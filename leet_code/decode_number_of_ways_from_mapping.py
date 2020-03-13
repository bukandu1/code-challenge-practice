# This problem was asked by Facebook.
# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
# You can assume that the messages are decodable. For example, '001' is not allowed.

import string

def decode(mapping, msg):
    """
    type(mapping) = dictinary
    type(msg) = string
    """

    def helper(current, remain):
        if not remain:
            return 

        else:
            # decode current and remain. if current and/or remain in mapping
            # save to string, else do not save
            new_string = ""
            print('current/remain', current, remain)
            if current and int(current) in mapping:
                key1 = int(current)
                new_string += mapping[key1]
            if remain and int(remain) in mapping:
                key2 = int(remain)
                new_string += mapping[key2]

            print(new_string)
            encode_set.add(new_string)
            print(encode_set)
            return helper(current + remain[0], remain[1:])

    if not msg:
        return msg

    encode_set=set()

    for i in range(len(msg)):
        print("".join(msg[0:i]), msg[i:])
        helper("".join(msg[0:i]), msg[i:])
    
    return len(encode_set)


# alpha = dict(zip(range(1, 27), string.ascii_lowercase))
alpha = {str(i): ch for i, ch in enumerate(string.ascii_lowercase, start=1)}
print(decode(alpha, "111"))
# print(alpha)

