import os
import shutil
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont


class CardRenderer:
    def __init__(self, card_width=300, card_height=450):
        self.card_width = card_width
        self.card_height = card_height
        self.font_path = "arial.ttf"

    def render_card(self, card, current_folder="Duo_TCG/cards/current", archive_folder="Duo_TCG/cards/archive"):
        os.makedirs(current_folder, exist_ok=True)
        os.makedirs(archive_folder, exist_ok=True)

        filename = self.make_filename(card.name)
        output_path = os.path.join(current_folder, filename)

        # archive old version if it exists
        self.archive_existing_card(output_path, archive_folder)

        # create blank image
        image = Image.new("RGB", (self.card_width, self.card_height), "white")
        draw = ImageDraw.Draw(image)

        # draw card name
        title_font = ImageFont.truetype(self.font_path, 24)
        text_width, text_height = self.get_text_size(draw, card.name, title_font)
        draw.text(
            ((self.card_width - text_width) / 2, 20),
            card.name,
            fill="black",
            font=title_font
        )

        # draw description
        body_font = ImageFont.truetype(self.font_path, 16)
        description_lines = self.wrap_text(card.description, draw, body_font)

        y_offset = 60
        line_height = self.get_text_size(draw, "Ag", body_font)[1] + 5

        for line in description_lines:
            draw.text((20, y_offset), line, fill="black", font=body_font)
            y_offset += line_height

        image.save(output_path)
        print(f"Saved new card to: {output_path}")

        return image, output_path

    def wrap_text(self, text, draw, font):
        lines = []
        words = text.split()
        current_line = ""

        for word in words:
            test_line = f"{current_line} {word}".strip()
            if self.get_text_size(draw, test_line, font)[0] <= self.card_width - 40:
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word

        if current_line:
            lines.append(current_line)

        return lines

    def get_text_size(self, draw, text, font):
        bbox = draw.textbbox((0, 0), text, font=font)
        width = bbox[2] - bbox[0]
        height = bbox[3] - bbox[1]
        return width, height

    def archive_existing_card(self, output_path, archive_folder):
        if os.path.exists(output_path):
            base_name = os.path.basename(output_path)
            name, ext = os.path.splitext(base_name)

            timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
            archived_name = f"{name}_{timestamp}{ext}"
            archived_path = os.path.join(archive_folder, archived_name)

            shutil.move(output_path, archived_path)
            print(f"Archived old card to: {archived_path}")

    def make_filename(self, card_name):
        # lowercases the name and replaces spaces with underscores
        filename = card_name.lower().replace(" ", "_")

        # optional extra cleanup for problematic filename characters
        invalid_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
        for char in invalid_chars:
            filename = filename.replace(char, "")

        return f"{filename}.png"