from PIL import Image
import os

class CleanImages():
    
    def resize_image(self, final_size: int, image_to_clean: Image):
        size = image_to_clean.size
        ratio = float(final_size) / max(size)
        # Apply ratio to width / height
        new_image_size = tuple([int(x*ratio) for x in size])
        image_to_clean = image_to_clean.resize(new_image_size, Image.ANTIALIAS)
        # create blank new image with 3 channels
        new_image = Image.new("RGB", (final_size, final_size))
        # paste resized image into new image
        new_image.paste(image_to_clean, ((final_size-new_image_size[0])//2, (final_size-new_image_size[1])//2))
        return new_image

    def clean_image_folder(self, images_folder: str, clean_images_folder: str):

        orig_path = images_folder
        clean_path = clean_images_folder
        dirs = os.listdir(orig_path)
        final_size = 512
        for n, item in enumerate(dirs, 1):
            # Only process image files
            if item.rsplit('.', 1)[-1] == "jpg":
                file_name = item.split(".")[0]
                orig_image = Image.open(f"{orig_path}{item}")
                clean_image = self.resize_image(final_size, orig_image)
                clean_image.save(f'{clean_path}{file_name}.jpg')
