import binascii
t = bytearray(str(input("Text: "), 'utf8')
h = binascii.hexlify(t)
b = bin(int(h, 16)).replace('b', '')
n = 8
bn = [b[i:i+n] for i in range(0, len(b), n)]


def decompress(compressed):
    decompressed = compressed
    decompressed = decompressed.replace("80", "00000000")
    decompressed = decompressed.replace("81", "11111111")
    decompressed = decompressed.replace("70", "0000000").replace("71", "1111111")
    decompressed = decompressed.replace("60", "000000").replace("61", "111111")
    decompressed = decompressed.replace("50", "00000").replace("51", "11111")
    decompressed = decompressed.replace("40", "0000").replace("41", "1111")
    decompressed = decompressed.replace("30", "000").replace("31", "111")
    print("Decompressed: " + decompressed)


for i in range(0, len(bn)):
    compressed = bn[i]
    compressed = compressed.replace("00000000", "80").replace("11111111", "81")
    compressed = compressed.replace("0000000", "70").replace("1111111", "71")
    compressed = compressed.replace("000000", "60").replace("111111", "61")
    compressed = compressed.replace("00000", "50").replace("11111", "51")
    compressed = compressed.replace("0000", "40").replace("1111", "41")
    compressed = compressed.replace("000", "30").replace("111", "31")
    print("Compressed: " + compressed)
    decompress(compressed)

