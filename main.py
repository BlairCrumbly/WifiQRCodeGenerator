import qrcode

ssid = "WifiNetworkName"
password = "WifiPassword"
encryption = "WPA" #WPA is most common - if your network requires a password do WPA (or WPA2). if there is no password do "nopass"

#formatting for QR sstring

wifi_config = f"WIFI:T:{encryption};S:{ssid};P:{password};;"

#gen QR code

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L, #has ERROR_CORRECT_M, ERROR_CORRECT_H etc built in but L becauce space effiecient but less robust
    box_size=10,
    border=4,
)

#encoding the wifi config data
qr.add_data(wifi_config)
qr.make(fit=True)

#save img
img = qr.make_image(fill_color="black", back_color="white")
img.save("wifi_qr.png")

print("QR code generated and saved as wifi_qr.png")