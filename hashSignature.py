import rsa

public_key, private_key = rsa.newkeys(2048)
print("[+] RSA key pair generated.")

message = b"Transfer $1000 to Mark"
print(f"[*] Original Message: {message.decode()}")

signature = rsa.sign(message, private_key, 'SHA-256')
print(f"[*] Signature: {signature.hex()[:80]}...")

try:
    rsa.verify(message, signature, public_key)
    print("[+] Test 1: Signature is VALID.")
except rsa.VerificationError:
    print("[-] Test 1: Signature is INVALID.")

tampered = b"Transfer $1000 to Oscar"
print(f"\n[*] Tampered Message: {tampered.decode()}")
try:
    rsa.verify(tampered, signature, public_key)
    print("[+] Test 2: Signature is VALID.")
except rsa.VerificationError:
    print("[-] Test 2: Signature is INVALID (tampering detected).")