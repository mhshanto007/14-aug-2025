from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageEnhance
import numpy as np

# Load your image
user_image = Image.open("/Users/md.mahedihassan/My Data/Photos/It's me/IMG_1301.jpg").convert("RGB")

# Step 1: Crop and resize to focus on the face
width, height = user_image.size
new_width = min(width, height)
left = (width - new_width) // 2
top = (height - new_width) // 3  # Adjust for better face framing
right = left + new_width
bottom = top + new_width

cropped = user_image.crop((left, top, right, bottom))
resized = cropped.resize((800, 800))

# Step 2: Convert to grayscale and darken
gray_image = ImageOps.grayscale(resized)
darkened = ImageEnhance.Brightness(gray_image).enhance(0.4)

# Step 3: Create binary code overlay
binary_overlay = Image.new("RGBA", darkened.size, (0, 0, 0, 0))
draw = ImageDraw.Draw(binary_overlay)

# Load a monospaced font (adjust path as needed)
font = ImageFont.truetype("DejaVuSansMono.ttf", 14)

# Draw binary numbers
cols = 80
rows = 80
for col in range(cols):
    for row in range(rows):
        char = np.random.choice(["0", "1"])
        x = col * 10
        y = row * 10
        draw.text((x, y), char, fill=(0, 153, 255, 120), font=font)

# Step 4: Merge binary overlay with portrait
composite = Image.alpha_composite(darkened.convert("RGBA"), binary_overlay)

# Save and show result
composite.save("binary_portrait.png")
composite.show()

print("hello world")
