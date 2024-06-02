import qrcode
import segno


def generate_wifi_qr_code(ssid, password, encryption_type='WPA'):
    # Wi-Fi network configuration string
    wifi_config = f"WIFI:T:{encryption_type};S:{ssid};P:{password};;"

    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Add WiFi configuration data to QR code
    qr.add_data(wifi_config)

    # Generate QR code image
    qr.make(fit=True)

    # Get PIL image object
    img = qr.make_image(fill_color="black", back_color="white")

    # Save QR code image
    img.save("wifi_qr_code.png")

    qrc = segno.make(wifi_config)
    qrc.save("segno code.png", scale=1, dark="darkblue")


def createWiFiQRCode():
    wifi_ssid = input("What is your Wi-Fi name?")
    wifi_password = input("What is your Wi-Fi password?")
    generate_wifi_qr_code(wifi_ssid, wifi_password)