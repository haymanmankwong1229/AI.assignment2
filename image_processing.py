from PIL import Image
import os

def compress_images(input_folder, output_folder, quality=75):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            img_path = os.path.join(input_folder, filename)
            img = Image.open(img_path)

            # 設置質量並保存
            output_path = os.path.join(output_folder, filename.replace(filename.split('.')[-1], 'jpeg'))
            img.save(output_path, 'JPEG', quality=quality)

            # 檢查文件大小
            while os.path.getsize(output_path) > 50 * 1024:  # 大小超過 50KB
                quality -= 5
                if quality < 50:  # 最低質量限制
                    break
                img.save(output_path, 'JPEG', quality=quality)

if __name__ == "__main__":
    input_folder = 'path/to/input/classified/Anger'  
    input_folder = 'path/to/input/classified/Confuse'  
    input_folder = 'path/to/input/classified/Happiness'
    input_folder = 'path/to/input/classified/Sadness'
    input_folder = 'path/to/input/classified/Surprise'
    input_folder = 'path/to/input/classified/others'
    output_folder = 'path/to/output/classified/Anger'  
    output_folder = 'path/to/output/classified/Confuse'  
    output_folder = 'path/to/output/classified/Happiness'
    output_folder = 'path/to/output/classified/Sadness'
    output_folder = 'path/to/output/classified/Surprise'
    output_folder = 'path/to/output/classified/others'
    compress_images(input_folder, output_folder)