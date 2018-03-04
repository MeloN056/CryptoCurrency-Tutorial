p = 2**256 - 2**32 - 2**9 - 2**8 - 2**7 - 2**6 - 2**4 - 1

Gx = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
Gy = 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8

print("p = ", p)
print("Gx = ", Gx)
print("Gy = ", Gy)

# y^2 = x^3 + 7 mod p -> y^2 - x^3 - 7 = 0 mod p
print("Gy^2 - Gx^3 - 7 mod p = ",(Gy**2 - Gx**3 - 7) % p)