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
            if current in mapping:
                new_string += mapping[current]
            if remain in mapping:
                new_string += mapping[remain]

            print(new_string)
            if new_string:
                encode_set.add(new_string)
            print("current/remain:",current, remain)
            return helper(current + remain[0], remain[1:])

    if not msg:
        return 0

    encode_set=set()

    for i in range(len(msg)):
        helper("".join(msg[0:i]), msg[i:])
    
    return len(encode_set)

alpha = {str(i): ch for i, ch in enumerate(string.ascii_lowercase, start=1)}
print(decode(alpha, "1211"))
# print(alpha)

