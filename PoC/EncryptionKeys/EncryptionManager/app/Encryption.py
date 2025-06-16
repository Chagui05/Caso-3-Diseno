from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os
import base64


def encrypt_dek_with_kek(dek: bytes, kek: bytes):
    iv = os.urandom(12)  # de 96 bits
    encryptor = Cipher(
        algorithms.AES(kek),
        modes.GCM(iv),
        backend=default_backend()
    ).encryptor()

    ciphertext = encryptor.update(dek) + encryptor.finalize()

    return {  # se pasan a base64 para poder ser transmitidos en htttp
        'iv': base64.b64encode(iv).decode(),
        'ciphertext': base64.b64encode(ciphertext).decode(),
        'tag': base64.b64encode(encryptor.tag).decode()
    }


def generar_tripleta_deks(representatives, admin):

    # 1. Generación de clave maestra
    dek = os.urandom(32)  # se usan 256 bits

    # 2. Se crean KEKs para la empresa y data pura vida
    kek_empresa = os.urandom(32)
    kek_dpv = os.urandom(32)

    # 3. Cifrar la DEK con cada KEK
    data_empresa = {
        "nombre": admin,
        "dek": encrypt_dek_with_kek(dek, kek_empresa),
        "kek": base64.b64encode(kek_empresa).decode()
    }

    data_dpv = {
        "nombre": "dpv",
        "dek": encrypt_dek_with_kek(dek, kek_dpv),
        "kek": base64.b64encode(kek_dpv).decode()
    }

    # 4. Se crean las distintas keks y deks para los representantes
    data_representatives = []

    for i in range(len(representatives)):
        kek = os.urandom(32)
        data_representatives.append({
            "nombre": representatives[i],
            "kek": base64.b64encode(kek).decode(),
            "dek": encrypt_dek_with_kek(dek, kek)
        })

        # 5. Se retorna los resultados
    return {
        'representantes': data_representatives,
        'empresa': data_empresa,
        'dpv': data_dpv,
    }