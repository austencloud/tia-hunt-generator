"""
src/scavenger_hunt/renderers/category_renderer.py
Category renderer for scavenger hunt
"""

from reportlab.lib import colors
from categories import get_category_colors
from font_manager import FontManager


class CategoryRenderer:
    """Renders category sections with headers and items for the scavenger hunt."""

    def __init__(self, canvas, layout):
        self.canvas = canvas
        self.layout = layout

    def draw(self, x, y, category, items, checkbox_renderer, width):
        """Draw a complete category section with header and items."""
        color_scheme = get_category_colors(category)
        header_height = self._draw_header(x, y, category, color_scheme, width)

        # Add extra spacing after header
        items_spacing = 8  # Reduced spacing after header to fit more content
        items_height = self._draw_items(
            x, y - header_height - items_spacing, items, checkbox_renderer
        )

        return (
            header_height + items_height + items_spacing
        )  # Total height of the category section

    def _draw_header(self, x, y, category, color_scheme, width):
        """Draw the category header with gradient background and decorative elements."""
        start_color = colors.Color(
            min(color_scheme["color"].red * 1.2, 1.0),
            min(color_scheme["color"].green * 1.2, 1.0),
            min(color_scheme["color"].blue * 1.2, 1.0),
        )
        end_color = colors.Color(
            color_scheme["color"].red * 0.8,
            color_scheme["color"].green * 0.8,
            color_scheme["color"].blue * 0.8,
        )

        header_height = self.layout.category_header_height
        self._draw_rounded_gradient_background(
            x, y - header_height, width, header_height, start_color, end_color, radius=6
        )

        self.canvas.setFillColor(colors.black)
        category_font = FontManager.get_category_font(category)
        font_size = 15  # Increased from 14 to make category headers bigger
        self.canvas.setFont(category_font, font_size)

        text_height = font_size * 0.75
        text_y = (
            y - (header_height / 2) - (text_height / 3) - 2
        )  # Adjusted to move text down slightly

        text_width = self.canvas.stringWidth(category, category_font, font_size)
        text_x = x + (width - text_width) / 2

        self.canvas.drawString(text_x, text_y, category)

        self.canvas.setStrokeColor(colors.black)
        self.canvas.setLineWidth(1)
        corner_size = 8

        self.canvas.line(x + 8, y - 8, x + 8 + corner_size, y - 8)
        self.canvas.line(x + 8, y - 8, x + 8, y - 8 - corner_size)
        self.canvas.line(x + width - 8, y - 8, x + width - 8 - corner_size, y - 8)
        self.canvas.line(x + width - 8, y - 8, x + width - 8, y - 8 - corner_size)
        self.canvas.line(
            x + 8, y - header_height + 8, x + 8 + corner_size, y - header_height + 8
        )
        self.canvas.line(
            x + 8, y - header_height + 8, x + 8, y - header_height + 8 + corner_size
        )
        self.canvas.line(
            x + width - 8,
            y - header_height + 8,
            x + width - 8 - corner_size,
            y - header_height + 8,
        )
        self.canvas.line(
            x + width - 8,
            y - header_height + 8,
            x + width - 8,
            y - header_height + 8 + corner_size,
        )

        return header_height

    def _draw_items(self, x, y, items, checkbox_renderer):
        """Draw all items for a category with checkboxes."""
        total_height = 0
        item_font = FontManager.get_item_font()
        font_size = 14  # Increased font size from 12 to 14
        
        # Create compact layout for categories with many items
        is_large_category = len(items) > 12
        item_height = self.layout.item_height + (4 if not is_large_category else 2)  # Increased spacing

        for i, item in enumerate(items):
            item_y = y - (i * item_height)

            # Draw checkbox - improved vertical alignment
            checkbox_y = item_y - self.layout.checkbox_size + 2
            checkbox_renderer.draw(
                x + self.layout.item_indent, checkbox_y, self.layout.checkbox_size
            )

            # Draw item text - improved vertical alignment
            # Adjust text baseline to align with checkbox center
            text_baseline = (
                checkbox_y + (self.layout.checkbox_size / 2) - (font_size / 3)
            )

            self.canvas.setFont(item_font, font_size)
            self.canvas.setFillColor(colors.black)
            self.canvas.drawString(
                x + self.layout.item_indent + self.layout.checkbox_text_offset,
                text_baseline,
                item,
            )

            total_height += item_height

        return total_height

    def _draw_rounded_gradient_background(
        self, x, y, width, height, start_color, end_color, radius=6, steps=10
    ):
        """Draw a rounded rectangle with gradient background."""
        # Draw main gradient in rounded rectangle
        self.canvas.saveState()

        # First draw the gradient in standard rectangles
        segment_height = height / steps
        for i in range(steps):
            ratio = i / float(steps - 1)
            r = start_color.red + (end_color.red - start_color.red) * ratio
            g = start_color.green + (end_color.green - start_color.green) * ratio
            b = start_color.blue + (end_color.blue - start_color.blue) * ratio
            current_color = colors.Color(r, g, b)

            self.canvas.setFillColor(current_color)
            # Use slightly smaller width/height to ensure complete coverage
            self.canvas.rect(
                x,
                y + (i * segment_height),
                width,
                segment_height + 0.5,  # Slight overlap
                fill=1,
                stroke=0,
            )

        # Then clip to a rounded rectangle to achieve the final effect
        path = self.canvas.beginPath()
        path.roundRect(x, y, width, height, radius)
        self.canvas.clipPath(path, stroke=0)

        # Draw a border with same color as the darker gradient color
        self.canvas.setStrokeColor(end_color)
        self.canvas.setLineWidth(0.75)
        self.canvas.roundRect(x, y, width, height, radius, fill=0, stroke=1)

        self.canvas.restoreState()