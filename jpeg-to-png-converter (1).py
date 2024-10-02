import os
from PIL import Image

def convert_jpeg_to_png(input_path, output_path):
    try:
        with Image.open(input_path) as img:
            img.save(output_path, 'PNG')
        return True
    except Exception as e:
        print(f"Conversion failed: {str(e)}")
        return False

def main():
    print("JPEG to PNG Converter")
    
    while True:
        # Get input file path
        input_file = input("Enter the path to the JPEG file (or 'q' to quit): ")
        
        if input_file.lower() == 'q':
            break
        
        # Check if the file exists and has a valid format
        if not os.path.exists(input_file) or not input_file.lower().endswith(('.jpg', '.jpeg')):
            print("JPEG not available or invalid format.")
            continue
        
        # Generate output file path
        output_file = os.path.splitext(input_file)[0] + '.png'
        
        print("Converting JPEG to PNG...")
        
        # Perform the conversion
        if convert_jpeg_to_png(input_file, output_file):
            print(f"Conversion successful. PNG file saved as: {output_file}")
        else:
            print("Conversion failed.")

if __name__ == "__main__":
    main()
