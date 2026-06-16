import sys
from PIL import Image

def decode_image(encoded_image_path):
    img = Image.open(encoded_image_path)
    width, height = img.size
    
    binary_message = ""
    # Trích xuất các bit cuối cùng từ ảnh
    for row in range(height):
        for col in range(width):
            pixel = img.getpixel((col, row))
            for color_channel in range(3):
                binary_message += format(pixel[color_channel], '08b')[-1]
                
    message = ""
    # Chuyển đổi các chuỗi 8-bit thành ký tự
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        if len(byte) < 8:
            break
            
        # Kiểm tra chuỗi kết thúc '1111111111111110' đã được gán ở hàm encrypt
        if binary_message[i:i+16] == '1111111111111110':
            break
            
        char = chr(int(byte, 2))
        
        # (Giữ lại đoạn logic theo tài liệu) Kết thúc thông điệp khi gặp dấu '\0'
        if char == '\0': 
            break
            
        message += char
        
    return message

def main():
    if len(sys.argv) != 2:
        print("Usage: python decrypt.py <encoded_image_path>")
        return
        
    encoded_image_path = sys.argv[1]
    decoded_message = decode_image(encoded_image_path)
    print("Decoded message:", decoded_message)

if __name__ == "__main__":
    main()