# Wi-Fi QR Code Generator

This Python script generates a QR code for your home Wi-Fi network.  
Guests can simply scan the QR code with their phone to connect instantly — no need to type the password.

---

## Features
- Generate a QR code containing your Wi-Fi SSID, password, and encryption type.
- Save the QR code as a PNG image (`wifi_qr.png`).
- Supports different encryption types (`WPA`, `WPA2`, `WEP`, or `nopass` for open networks).
- Customizable QR code appearance (size, border, colors).

---

## Requirements
Install the `qrcode` library (and Pillow for image handling):

```bash
pip install qrcode[pil]
