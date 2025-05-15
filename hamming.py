def calculate_redundant_bits(m):
    r = 0
    while 2**r < m + r + 1:
        r += 1
    return r
def position_redundant_bits(data, r):
    j, k, m = 0, 1, len(data)
    res = ''
    for i in range(1, m + r + 1):
        if i == 2**j:
            res += '0'
            j += 1
        else:
            res += data[k-1]
            k += 1
    return res
def calculate_parity_bits(arr, r):
    n = len(arr)
    for i in range(r):
        parity = 0
        for j in range(1, n + 1):
            if j & (2**i) == 2**i:
                parity ^= int(arr[j-1])
        arr = arr[:2**i-1] + str(parity) + arr[2**i:]
    return arr
def detect_error(arr, r):
    n = len(arr)
    res = 0
    for i in range(r):
        val = 0
        for j in range(1, n + 1):
            if j & (2**i) == 2**i:
                val ^= int(arr[j-1])
        res += val * (2**i)
    return res
def encode(data):
    m = len(data)
    r = calculate_redundant_bits(m)
    arr = position_redundant_bits(data, r)
    return calculate_parity_bits(arr, r)
def decode(data):
    r = 0
    while 2**r < len(data):
        r += 1
    error_pos = detect_error(data, r)
    if error_pos == 0:
        return ''.join([data[i-1] for i in range(1, len(data)+1) if not (i & (i-1) == 0)])
    else:
        data_list = list(data)
        data_list[error_pos-1] = '1' if data_list[error_pos-1] == '0' else '0'
        corrected_data = ''.join(data_list)
        return ''.join([corrected_data[i-1] for i in range(1, len(corrected_data)+1) if not (i & (i-1) == 0)])
if __name__ == "__main__":
    choice = input("Enter 1 to encode, 2 to decode: ")
    if choice == '1':
        data = input("Enter data bits: ")
        encoded = encode(data)
        print(f"Encoded data: {encoded}")
    elif choice == '2':
        data = input("Enter received data bits: ")
        decoded = decode(data)
        print(f"Decoded data: {decoded}")