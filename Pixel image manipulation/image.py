from PIL import Image
import numpy as np

def encrypt_image(input_path, output_path, key=42):
    # Open image
    img = Image.open(input_path)
    img_array = np.array(img)

    # Swap Red and Blue channels
    img_array[:, :, [0, 2]] = img_array[:, :, [2, 0]]

    # Apply XOR operation with key
    encrypted_array = img_array ^ key

    # Save encrypted image
    encrypted_img = Image.fromarray(encrypted_array)
    encrypted_img.save(output_path)
    print(f"Image encrypted and saved to {output_path}")

def decrypt_image(input_path, output_path, key=42):
    # Open encrypted image
    img = Image.open(input_path)
    img_array = np.array(img)

    # Reverse XOR operation
    decrypted_array = img_array ^ key

    # Swap Red and Blue channels back
    decrypted_array[:, :, [0, 2]] = decrypted_array[:, :, [2, 0]]

    # Save decrypted image
    decrypted_img = Image.fromarray(decrypted_array)
    decrypted_img.save(output_path)
    print(f"Image decrypted and saved to {output_path}")

# Example usage
encrypt_image("input.jpg", "encrypted.png")
decrypt_image("encrypted.png", "decrypted.png")
