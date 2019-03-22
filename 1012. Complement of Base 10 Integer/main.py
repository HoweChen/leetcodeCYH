class Solution:
    def bitwiseComplement(self, N: int) -> int:
        # use bitwise XOR
        N_bin_str = bin(N)
        marker = "0b"+"1"*len(N_bin_str[2:])
        return int(N_bin_str, 2) ^ int(marker, 2)
