"""
src/hunt_generator.py
Main generator class for specimen scavenger hunt
"""

import os
import math
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from font_manager import FontManager
from hunt_layout import HuntLayout

from items import ITEMS
from renderers.corner_renderer import CornerRenderer
from renderers.footer_renderer import FooterRenderer
from renderers.header_renderer import HeaderRenderer
from renderers.background_renderer import BackgroundRenderer
from renderers.category_renderer import CategoryRenderer
from renderers.checkbox_renderer import CheckboxRenderer


class ScavengerHuntGenerator:
    """
    Main class for generating the specimen scavenger hunt PDF.
    Coordinates the layout, rendering, and PDF creation process.
    """

    def __init__(self, output_file="specimen_scavenger_hunt.pdf"):
        """Initialize the generator with output file and components."""
        self.output_file = output_file
        self.page_width, self.page_height = letter

        # Register fonts
        FontManager.register_fonts()

        # Create layout
        self.layout = HuntLayout()

        # Create canvas
        self.canvas = canvas.Canvas(output_file, pagesize=letter)

        # Create renderers
        self.background_renderer = BackgroundRenderer(self.canvas)
        self.header_renderer = HeaderRenderer(self.canvas)
        self.category_renderer = CategoryRenderer(self.canvas, self.layout)
        self.checkbox_renderer = CheckboxRenderer(self.canvas)
        self.footer_renderer = FooterRenderer(self.canvas)
        self.corner_renderer = CornerRenderer(self.canvas)

    def generate_hunt_pdf(self):
        """Generate the complete scavenger hunt PDF."""
        # Organize categories into balanced pages
        categorized_items = self._organize_categories()

        # Calculate total pages needed (first page + continuation pages)
        total_pages = 2  # We'll use exactly 2 pages for now

        # Draw first page
        self._draw_first_page(categorized_items["page1"])

        # Draw second page
        self._draw_continuation_page(categorized_items["page2"], 2, total_pages)

        # Save the PDF
        self.canvas.save()
        print(f"✨ Scavenger hunt PDF saved to: {os.path.abspath(self.output_file)}")

    def _draw_first_page(self, categories):
        """Draw the first page with title, instructions, and initial categories."""
        # Draw background
        self.background_renderer.draw(0, 0, self.page_width, self.page_height)

        # Draw decorative corners
        self.corner_renderer.draw(40, 40, 30, self.page_width, self.page_height)

        # Draw header
        title_y = self.header_renderer.draw(
            "The Insect Asylum Collection", "Specimen Scavenger Hunt",
            "Explore our collection and check off each fascinating specimen as you find it!\n"
            "Items are color-coded by category to help guide your search.",
            self.page_width, self.page_height,
        )

        # Calculate margins
        margin_x, margin_y = self.layout.calculate_margins(
            self.page_width, self.page_height
        )

        # Draw categories in two columns
        left_categories = categories["left_column"]
        right_categories = categories["right_column"]

        # Draw left column categories
        current_y = self.page_height - title_y
        for category, items in left_categories:
            category_height = self.category_renderer.draw(
                margin_x,
                current_y,
                category,
                items,
                self.checkbox_renderer,
                self.layout.column_width,
            )
            current_y -= (
                category_height + self.layout.category_spacing
            )  # Add spacing between categories

        # Draw right column categories
        current_y = self.page_height - title_y
        for category, items in right_categories:
            category_height = self.category_renderer.draw(
                margin_x + self.layout.column_width + self.layout.column_spacing,
                current_y,
                category,
                items,
                self.checkbox_renderer,
                self.layout.column_width,
            )
            current_y -= (
                category_height + self.layout.category_spacing
            )  # Add spacing between categories

        # Add page break
        self.canvas.showPage()

    def _draw_continuation_page(self, categories, page_num, total_pages):
        """Draw a continuation page with remaining categories."""
        # Draw background
        self.background_renderer.draw(0, 0, self.page_width, self.page_height)

        # Draw decorative corners
        self.corner_renderer.draw(40, 40, 30, self.page_width, self.page_height)

        # Draw simplified header
        header_y = self.header_renderer.draw_page_header(
            "The Insect Asylum Collection",
            page_num,
            total_pages,
            self.page_width,
            self.page_height,
        )

        # Calculate margins
        margin_x, margin_y = self.layout.calculate_margins(
            self.page_width, self.page_height
        )

        # Draw categories in two columns
        left_categories = categories["left_column"]
        right_categories = categories["right_column"]

        # Draw left column categories
        current_y = self.page_height - header_y
        for category, items in left_categories:
            category_height = self.category_renderer.draw(
                margin_x,
                current_y,
                category,
                items,
                self.checkbox_renderer,
                self.layout.column_width,
            )
            current_y -= (
                category_height + self.layout.category_spacing
            )  # Add spacing between categories

        # Draw right column categories
        current_y = self.page_height - header_y
        for category, items in right_categories:
            category_height = self.category_renderer.draw(
                margin_x + self.layout.column_width + self.layout.column_spacing,
                current_y,
                category,
                items,
                self.checkbox_renderer,
                self.layout.column_width,
            )
            current_y -= (
                category_height + self.layout.category_spacing
            )  # Add spacing between categories

        # Draw footer with total count
        total_items = sum(
            len(items)
            for _, items in left_categories
            + right_categories
            + categories["left_column"]
            + categories["right_column"]
        )

        self.footer_renderer.draw(
            self.page_width / 2, self.layout.footer_y, total_items
        )

        # Add page break
        self.canvas.showPage()

    def _organize_categories(self):
        """Organize categories into multiple pages with balanced columns."""
        # Group items by category
        categorized_items = {}
        for category, item in ITEMS:
            if category not in categorized_items:
                categorized_items[category] = []
            categorized_items[category].append(item)

        # Define which categories go on which page
        # This is a simplified approach that manually assigns categories to pages
        # Page 1: Minerals & Fossils, Shells & Marine, Plant Materials, Preserved Specimens
        # Page 2: Animal Parts, Bones & Skulls, Resin Replicas, Miscellaneous

        page1_categories = [
            "Minerals & Fossils",
            "Shells & Marine",
            "Plant Materials",
            "Preserved Specimens",
        ]
        page2_categories = [
            "Animal Parts",
            "Bones & Skulls",
            "Resin Replicas",
            "Miscellaneous",
        ]

        # Sort categories by their order in the lists above
        page1_data = [
            (cat, categorized_items[cat])
            for cat in page1_categories
            if cat in categorized_items
        ]

        page2_data = [
            (cat, categorized_items[cat])
            for cat in page2_categories
            if cat in categorized_items
        ]

        # Create custom balanced columns
        page1_left = [
            (page1_categories[0], categorized_items[page1_categories[0]]),
            (page1_categories[1], categorized_items[page1_categories[1]]),
        ]

        page1_right = [
            (page1_categories[2], categorized_items[page1_categories[2]]),
            (page1_categories[3], categorized_items[page1_categories[3]]),
        ]

        # Page 2 has Animal Parts (largest) on the left, and the rest on the right
        page2_left = [(page2_categories[0], categorized_items[page2_categories[0]])]

        page2_right = [
            (page2_categories[1], categorized_items[page2_categories[1]]),
            (page2_categories[2], categorized_items[page2_categories[2]]),
            (page2_categories[3], categorized_items[page2_categories[3]]),
        ]

        return {
            "page1": {"left_column": page1_left, "right_column": page1_right},
            "page2": {"left_column": page2_left, "right_column": page2_right},
        }
