from PIL import Image, ImageDraw, ImageFont
import os

def create_cycling_gif(text, output_filename, width=200, height=200, bg_color=(0, 0, 0), text_color=(255, 255, 255), delay=250):
    frames = []
    script_dir = os.path.dirname(os.path.abspath(__file__))
    font_path = os.path.join(script_dir, "RobotoMono-Regular.ttf")
    try:
        font = ImageFont.truetype(font_path, 180)
    except IOError:
        print("Font file not found. Using default font.")
        font = ImageFont.load_default()
    for i in range(len(text) + 1):
        image = Image.new('RGB', (width, height), bg_color)
        draw = ImageDraw.Draw(image)
        if i < len(text):
            letter = text[i]
            bbox = draw.textbbox((0, 0), letter, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            x = (width - text_width) // 2
            ascent, descent = font.getmetrics()
            total_height = ascent + descent
            y = (height) // 2 - 120
            draw.text((x, y), letter, font=font, fill=text_color)
        frames.append(image)
    frames[0].save(
        output_filename,
        save_all=True,
        append_images=frames[1:],
        duration=delay,
        loop=0,
        disposal=2
    )

def generate_scrolling_text_gifs(text, output_folder="output_gifs"):
    if len(text) < 6:
        raise ValueError("Text must be at least 6 characters long.")
    padded_text = " " * 6 + text + " " * 6
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    for i in range(6):
        shifted_text = padded_text[i:] + padded_text[:i]
        output_filename = os.path.join(output_folder, f"gif_{i+1}.gif")
        create_cycling_gif(shifted_text, output_filename)
        print(f"Generated {output_filename}")

text = input("Enter the text (at least 6 characters): ")
generate_scrolling_text_gifs(text)