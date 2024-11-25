import qrcode

# WiFi credentials
ssid = "Your_SSID"
password = "Your_Password"
security_type = "WPA"  # Can be 'WPA', 'WEP', or 'nopass' for no password

# Generate WiFi QR code
wifi_config = f"WIFI:T:{security_type};S:{ssid};P:{password};;"
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(wifi_config)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill='black', back_color='white')

# Save the image file
img.save("wifi_qr_code.png")

print("WiFi QR code generated and saved as wifi_qr_code.png")