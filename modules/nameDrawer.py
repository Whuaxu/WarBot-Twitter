from PIL import Image, ImageDraw, ImageFont

class NameDrawer:
    def __init__(self, image_path, output_path, font_path='arial.ttf', font_size=15):
        self.image_path = image_path
        self.output_path = output_path
        self.font_path = font_path
        self.font_size = font_size
        
        # Load image
        self.img = Image.open(image_path)
        self.draw = ImageDraw.Draw(self.img)
        self.font = ImageFont.truetype(font_path, font_size)

        # Spacing Configuration
        self.HORIZ = 150  # Spacing between columns
        self.VERT = 40    # Spacing between rows
        self.SUP = 50     # Space at the top
        self.LAT = 50     # Space on the sides
        
        self.maxNames = (self.img.width - 2 * self.LAT) // self.HORIZ  # Fit names per row

def draw_names(self, users):
        
        x, y = self.LAT, self.SUP

        for i, user in enumerate(users):
            self.draw.text((x, y), user, fill="black", font=self.font)

            # Move X coordinate for next column
            x += self.HORIZ

            # If we reach max names per row, move to the next line
            if (i + 1) % self.maxNames == 0:
                x = self.LAT  # Reset X
                y += self.VERT  # Move to next row

def save_image(self):

    self.img.save(self.output_path)
    print(f"Image saved at {self.output_path}")