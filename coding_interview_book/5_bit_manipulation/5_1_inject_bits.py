# M get's injected into N at point j.

def fit_bits(M, N, i, j):
    # Sets ones for j-i to zero.
    temp_mask = (1 << (j - i + 1)) - 1

    # Move ones left i spaces and flip bits.
    mask = ~(temp_mask << i) + (1 << 32)

    N_masked = N & mask

    return N_masked + (M << i)



print(bin(fit_bits(0b10101, 0b1111111111, 2, 8)))
