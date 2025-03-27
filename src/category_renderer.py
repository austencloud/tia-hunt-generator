"""
src/scavenger_hunt/renderers/category_renderer.py
Category renderer for scavenger hunt
"""
from reportlab.lib import colors
from categories import get_category_colors

class CategoryRenderer:
    """Renders category sections with headers and items for the scavenger hunt."""
    
    def __init__(self, canvas, layout):
        self.canvas = canvas
        self.layout = layout
        
        # Define emoji for each category
        self.category_emojis = {
            "Minerals & Fossils": "🔵",
            "Shells & Marine": "🔷",
            "Plant Materials": "🟢",
            "Preserved Specimens": "🟡",
            "Animal Parts": "🟤",
            "Bones & Skulls": "⚪",
            "Resin Replicas": "🟠",
            "Miscellaneous": "⚫"
        }
    
    def draw(self, x, y, category, items, checkbox_renderer, width):
        """Draw a complete category section with header and items."""
        color_scheme = get_category_colors(category)
        header_height = self._draw_header(x, y, category, color_scheme, width)
        items_height = self._draw_items(x, y - header_height - 5, items, checkbox_renderer)
        
        return header_height + items_height + 5  # Total height of the category section
    
    def _draw_header(self, x, y, category, color_scheme, width):
        """Draw the category header with gradient background and decorative elements."""
        # Define colors
        start_color = colors.Color(
            min(color_scheme["color"].red * 1.2, 1.0),
            min(color_scheme["color"].green * 1.2, 1.0),
            min(color_scheme["color"].blue * 1.2, 1.0)
        )
        end_color = colors.Color(
            color_scheme["color"].red * 0.8,
            color_scheme["color"].green * 0.8,
            color_scheme["color"].blue * 0.8
        )
        
        # Draw gradient background
        self._draw_gradient_background(
            x, y - self.layout.category_header_height, 
            width, self.layout.category_header_height,
            start_color, end_color
        )
        
        # Get emoji for the category
        emoji = self.category_emojis.get(category, "•")
        
        # Draw category name
        self.canvas.setFillColor(color_scheme["text_color"])
        self.canvas.setFont("DejaVuSans-Bold", 14)
        text_y = y - self.layout.category_header_height + 18
        self.canvas.drawString(x + 10, text_y, f"{emoji}  {category}")
        
        # Draw accent corners
        self.canvas.setStrokeColor(color_scheme["text_color"])
        self.canvas.setLineWidth(1)
        corner_size = 8
        
        # Top-left
        self.canvas.line(
            x + 4, 
            y - 4, 
            x + 4 + corner_size, 
            y - 4
        )
        self.canvas.line(
            x + 4, 
            y - 4, 
            x + 4, 
            y - 4 - corner_size
        )
        
        # Top-right
        self.canvas.line(
            x + width - 4,
            y - 4,
            x + width - 4 - corner_size,
            y - 4
        )
        self.canvas.line(
            x + width - 4,
            y - 4,
            x + width - 4,
            y - 4 - corner_size
        )
        
        # Bottom-left
        self.canvas.line(
            x + 4, 
            y - self.layout.category_header_height + 4, 
            x + 4 + corner_size, 
            y - self.layout.category_header_height + 4
        )
        self.canvas.line(
            x + 4, 
            y - self.layout.category_header_height + 4, 
            x + 4, 
            y - self.layout.category_header_height + 4 + corner_size
        )
        
        # Bottom-right
        self.canvas.line(
            x + width - 4, 
            y - self.layout.category_header_height + 4, 
            x + width - 4 - corner_size, 
            y - self.layout.category_header_height + 4
        )
        self.canvas.line(
            x + width - 4, 
            y - self.layout.category_header_height + 4, 
            x + width - 4, 
            y - self.layout.category_header_height + 4 + corner_size
        )
        
        return self.layout.category_header_height
    
    def _draw_items(self, x, y, items, checkbox_renderer):
        """Draw all items for a category with checkboxes."""
        total_height = 0
        
        for i, item in enumerate(items):
            item_y = y - (i * self.layout.item_height)
            
            # Draw checkbox
            checkbox_renderer.draw(
                x + self.layout.item_indent, 
                item_y - self.layout.checkbox_size + 2,
                self.layout.checkbox_size
            )
            
            # Draw item text
            self.canvas.setFont("DejaVuSans", 10)
            self.canvas.setFillColor(colors.black)
            self.canvas.drawString(
                x + self.layout.item_indent + self.layout.checkbox_text_offset,
                item_y,
                item
            )
            
            total_height += self.layout.item_height
        
        return total_height
    
    def _draw_gradient_background(self, x, y, width, height, start_color, end_color, steps=10):
        """Draw a gradient background."""
        for i in range(steps):
            ratio = i / float(steps - 1)
            r = start_color.red + (end_color.red - start_color.red) * ratio
            g = start_color.green + (end_color.green - start_color.green) * ratio
            b = start_color.blue + (end_color.blue - start_color.blue) * ratio
            current_color = colors.Color(r, g, b)
            
            self.canvas.setFillColor(current_color)
            segment_height = height / steps
            
            self.canvas.rect(
                x, y + (i * segment_height),
                width, segment_height + 0.5,  # Slight overlap
                fill=1, stroke=0
            )
