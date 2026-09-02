import os
import shutil
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont


class CardRenderer:
    def __init__(self, card_width=300, card_height=450):
        self.card_width = card_width
        self.card_height = card_height

        self.font_path = "arial.ttf"
        self.italic_font_path = "ariali.ttf"

    def render_card(
        self,
        card,
        current_folder="Duo_TCG/cards/current",
        archive_folder="Duo_TCG/cards/archive"
    ):
        os.makedirs(current_folder, exist_ok=True)
        os.makedirs(archive_folder, exist_ok=True)

        filename = self.make_filename(card.name)
        output_path = os.path.join(current_folder, filename)

        self.archive_existing_card(output_path, archive_folder)

        image = Image.new(
            "RGB",
            (self.card_width, self.card_height),
            "white"
        )

        draw = ImageDraw.Draw(image)

        self.draw_name(draw, card)
        self.draw_energy(draw, card)
        self.draw_traits(draw, card)

        ability_end_y = self.draw_ability(draw, card)
        self.draw_description(draw, card, ability_end_y + 10)

        self.draw_stats(draw, card)

        image.save(output_path)

        print(f"Saved new card to: {output_path}")

        return image, output_path

    def draw_name(self, draw, card):
        font = ImageFont.truetype(self.font_path, 24)

        width, _ = self.get_text_size(
            draw,
            card.name,
            font
        )

        x = (self.card_width - width) / 2

        draw.text(
            (x, 15),
            card.name,
            fill="black",
            font=font
        )

    def draw_energy(self, draw, card):
        font = ImageFont.truetype(self.font_path, 16)

        text = f"Energy: {card.energy}"

        width, _ = self.get_text_size(
            draw,
            text,
            font
        )

        x = (self.card_width - width) / 2

        draw.text(
            (x, 48),
            text,
            fill="black",
            font=font
        )

    def draw_traits(self, draw, card):
        font = ImageFont.truetype(self.font_path, 15)

        text = (
            f"{card.capability} / "
            f"{card.descriptor} / "
            f"{card.distinction}"
        )

        width, _ = self.get_text_size(
            draw,
            text,
            font
        )

        x = (self.card_width - width) / 2

        draw.text(
            (x, 245),
            text,
            fill="black",
            font=font
        )

    def draw_ability(self, draw, card):
        y = 275

        font, lines, line_height = self.fit_ability_text(
            draw,
            card.ability,
            start_size=14,
            min_size=10,
            max_width=self.card_width - 40,
            max_height=60
        )

        for line in lines:
            draw.text((20, y), line, fill="black", font=font)
            y += line_height

        return y

    def draw_description(self, draw, card, start_y):
        font = ImageFont.truetype(self.italic_font_path, 11)

        lines = self.wrap_text(
            card.description,
            draw,
            font,
            max_width=self.card_width - 40
        )

        y = start_y
        line_height = self.get_text_size(draw, "Ag", font)[1] + 3

        for line in lines:
            width, _ = self.get_text_size(draw, line, font)
            x = self.card_width - width - 20

            draw.text((x, y), line, fill="black", font=font)
            y += line_height

    def draw_stats(self, draw, card):
        font = ImageFont.truetype(self.font_path, 18)

        attack_text = f"ATK {card.attack}"
        life_text = f"LIFE {card.life}"

        draw.text(
            (20, 415),
            attack_text,
            fill="black",
            font=font
        )

        life_width, _ = self.get_text_size(
            draw,
            life_text,
            font
        )

        draw.text(
            (
                self.card_width - life_width - 20,
                415
            ),
            life_text,
            fill="black",
            font=font
        )

    def fit_ability_text(self, draw, text, start_size=14, min_size=10, max_width=None, max_height=60):
        if max_width is None:
            max_width = self.card_width - 40

        font_size = start_size

        while font_size >= min_size:
            font = ImageFont.truetype(self.font_path, font_size)
            lines = self.wrap_text(text, draw, font, max_width)
            line_height = self.get_text_size(draw, "Ag", font)[1] + 4
            total_height = len(lines) * line_height

            if total_height <= max_height:
                return font, lines, line_height

            font_size -= 1

        # fallback if nothing fits cleanly
        font = ImageFont.truetype(self.font_path, min_size)
        lines = self.wrap_text(text, draw, font, max_width)
        line_height = self.get_text_size(draw, "Ag", font)[1] + 4
        return font, lines, line_height

    def wrap_text(self, text, draw, font, max_width):
        lines = []
        words = text.split()
        current_line = ""

        for word in words:
            test_line = f"{current_line} {word}".strip()

            if self.get_text_size(
                draw,
                test_line,
                font
            )[0] <= max_width:
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word

        if current_line:
            lines.append(current_line)

        return lines

    def get_text_size(self, draw, text, font):
        bbox = draw.textbbox(
            (0, 0),
            text,
            font=font
        )

        width = bbox[2] - bbox[0]
        height = bbox[3] - bbox[1]

        return width, height

    def archive_existing_card(
        self,
        output_path,
        archive_folder
    ):
        if os.path.exists(output_path):
            base_name = os.path.basename(output_path)
            name, ext = os.path.splitext(base_name)

            timestamp = datetime.now().strftime(
                "%Y-%m-%d_%H%M%S"
            )

            archived_name = (
                f"{name}_{timestamp}{ext}"
            )

            archived_path = os.path.join(
                archive_folder,
                archived_name
            )

            shutil.move(
                output_path,
                archived_path
            )

            print(
                f"Archived old card to: "
                f"{archived_path}"
            )

    def make_filename(self, card_name):
        filename = (
            card_name
            .lower()
            .replace(" ", "_")
        )

        invalid_chars = [
            "<", ">", ":", '"',
            "/", "\\", "|", "?",
            "*"
        ]

        for char in invalid_chars:
            filename = filename.replace(
                char,
                ""
            )

        return f"{filename}.png"