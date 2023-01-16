# Define the elliptic curve parameters
a = 952
b = 873
p = 2063
G = EllipticCurve(GF(p),[a,b])

# Define the subgroup generator
P = G((1, 324))

# Alice's private key
alice_private_key = 31

# Bob's private key
bob_private_key = 19

# Alice's public key
alice_public_key = alice_private_key*P

print(alice_public_key)

# Bob's public key
bob_public_key = bob_private_key*P

print(bob_public_key)

# Alice's shared secret
alice_shared_secret = alice_private_key*bob_public_key

# Bob's shared secret
bob_shared_secret = bob_private_key*alice_public_key

# The x-coordinate of the shared secret is the same for both parties
print(alice_shared_secret.xy()[0])
print(bob_shared_secret.xy()[0])


#Copy above the codes to past sage input box following links: https://sagecell.sagemath.org/