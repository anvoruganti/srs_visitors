import cv2 # type: ignore
from pyzbar import pyzbar # type: ignore

def scan_qr_code(image_path):
    image = cv2.imread(image_path)
    qr_codes = pyzbar.decode(image)
    if qr_codes:
        return qr_codes[0].data.decode('utf-8')
    return None