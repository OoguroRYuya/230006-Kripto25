from PIL import Image, ImageDraw, ImageFont

def encode_image(image_path, output_path, message):
    message += chr(0)  # terminator
    binary_message = ''.join([format(ord(c), '08b') for c in message])

    img = Image.open(image_path).convert("RGB")
    pixels = list(img.getdata())

    if len(binary_message) > len(pixels) * 3:
        raise ValueError("Pesan terlalu panjang untuk disisipkan ke dalam gambar ini!")

    new_pixels = []
    bit_index = 0
    for pixel in pixels:
        r, g, b = pixel
        new_rgb = []
        for color in (r, g, b):
            if bit_index < len(binary_message):
                new_rgb.append((color & ~1) | int(binary_message[bit_index]))
                bit_index += 1
            else:
                new_rgb.append(color)
        new_pixels.append(tuple(new_rgb))

    img.putdata(new_pixels)
    img.save(output_path)
    print(f"✅ Pesan berhasil disisipkan. Gambar terenkripsi disimpan di {output_path}")


def decode_image(stego_path, output_path=None):
    img = Image.open(stego_path).convert("RGB")
    pixels = list(img.getdata())

    bits = ""
    for pixel in pixels:
        for color in pixel:
            bits += str(color & 1)

    message = ""
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        if len(byte) < 8:
            continue
        char = chr(int(byte, 2))
        if char == chr(0):  # stop marker
            break
        message += char

    print(f"📥 Pesan tersembunyi: {message}")

    # Jika ingin langsung bikin gambar dengan pesan yang terlihat
    if output_path:
        decoded_img = Image.open(stego_path).convert("RGB")
        draw = ImageDraw.Draw(decoded_img)

        try:
            font = ImageFont.truetype("arial.ttf", 40)
        except:
            font = ImageFont.load_default()

        # Tulis pesan di gambar
        draw.text((20, 20), f"Pesan: {message}", fill=(255, 0, 0), font=font)
        decoded_img.save(output_path)
        print(f"📤 Gambar hasil decode disimpan di {output_path}")

    return message


# === Contoh penggunaan ===
# Encode
encode_image("raw.png", "stego.png", "Go Big")

# Decode + buat gambar dengan pesan terlihat
decode_image("stego.png", "decoded.png")
