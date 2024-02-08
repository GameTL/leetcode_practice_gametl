class Solution:
    def hammingWeight(self, n: int) -> int:
        # num_map = [-2147483648, 1073741824, 536870912, 268435456, 134217728, 67108864, 33554432, 16777216, 8388608, 4194304, 2097152, 1048576, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
        # x = str(n)
        # print(x)
        sum = 0
        # for i in range(len(x)):
        #     print(x[i], num_map[i])
        #     sum += int(x[int(i)]) * num_map[i]
        # return sum
        for i in str(n):
            sum += int(i)
        return sum

# x = [2**i for i in range(32)][::-1]
x = Solution()

# print(x.hammingWeight(00000000000000000000000010000000))
# print(x.hammingWeight(00000000000000000000000000001011))
print(x.hammingWeight(10000000000000000000000011))
print(x.hammingWeight(1011))