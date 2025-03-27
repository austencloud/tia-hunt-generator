"""
src/scavenger_hunt/hunt_generator.py
Main generator class for specimen scavenger hunt
"""
import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

from card_layout import CardLayout
from categories import CATEGORIES, get_category_colors
from font_manager import FontManager
from items import ITEMS
from scavenger_hunt.hunt_layout import HuntLayout
from scavenger_hunt.renderers.background_renderer import BackgroundRenderer
from scavenger_hunt.renderers.header_renderer import HeaderRenderer
from scavenger_hunt.renderers.category_renderer import CategoryRenderer
from scavenger_hunt.renderers.checkbox_renderer import CheckboxRenderer
from scavenger_hunt.renderers.footer_renderer import FooterRenderer
from scavenger_hunt.renderers.corner_renderer import CornerRenderer


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
        # Draw background
        self.background_renderer.draw(0, 0, self.page_width, self.page_height)
        
        # Draw decorative corners
        self.corner_renderer.draw(40, 40, 30, self.page_width, self.page_height)
        
        # Draw header
        title_y = self.header_renderer.draw(
            "The Insect Asylum Collection", 
            "Specimen Scavenger Hunt",
            "Explore our collection and check off each fascinating specimen as you find it! Items are color-coded by category to help guide your search.",
            self.page_width,
            self.page_height
        )
        
        # Calculate layout
        margin_x, margin_y = self.layout.calculate_margins(
            self.page_width, self.page_height
        )
        
        # Organize items into columns
        categories_data = self._organize_categories()
        left_categories = categories_data["left_column"]
        right_categories = categories_data["right_column"]
        
        # Draw left column categories
        current_y = self.page_height - title_y
        for category, items in left_categories:
            category_height = self.category_renderer.draw(
                margin_x, 
                current_y, 
                category, 
                items, 
                self.checkbox_renderer,
                self.layout.column_width
            )
            current_y -= category_height + 15  # Add spacing between categories
        
        # Draw right column categories
        current_y = self.page_height - title_y
        for category, items in right_categories:
            category_height = self.category_renderer.draw(
                margin_x + self.layout.column_width + self.layout.column_spacing, 
                current_y,
                category, 
                items, 
                self.checkbox_renderer,
                self.layout.column_width
            )
            current_y -= category_height + 15  # Add spacing between categories
        
        # Draw footer
        total_items = sum(len(items) for category, items in left_categories + right_categories)
        self.footer_renderer.draw(
            self.page_width / 2,
            self.layout.footer_y, 
            total_items
        )
        
        # Save the PDF
        self.canvas.showPage()
        self.canvas.save()
        print(f"✨ Scavenger hunt PDF saved to: {os.path.abspath(self.output_file)}")
    
    def _organize_categories(self):
        """Organize categories into balanced columns."""
        # Group items by category
        categorized_items = {}
        for category, item in ITEMS:
            if category not in categorized_items:
                categorized_items[category] = []
            categorized_items[category].append(item)
        
        # Calculate total items
        total_items = sum(len(items) for items in categorized_items.values())
        target_items_per_column = total_items / 2
        
        # Distribute categories between columns
        left_column = []
        right_column = []
        current_column = left_column
        current_count = 0
        
        for category, items in sorted(categorized_items.items()):
            # If adding this category to the current column would exceed the target,
            # and we're still in the left column, switch to the right column
            if (current_count + len(items) > target_items_per_column and 
                current_column == left_column and 
                current_count > 0):
                current_column = right_column
                current_count = 0
            
            current_column.append((category, items))
            current_count += len(items)
        
        return {
            "left_column": left_column,
            "right_column": right_column
        }
