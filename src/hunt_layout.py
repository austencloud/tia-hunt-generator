"""
src/scavenger_hunt/hunt_layout.py
Layout settings for specimen scavenger hunt
"""
from reportlab.lib.units import inch

class HuntLayout:
    """
    Manages layout settings for the scavenger hunt checklist including dimensions,
    spacing, and page arrangement.
    """
    
    def __init__(self):
        # Two-column layout
        self.columns = 2
        self.column_spacing = 0.5 * inch
        
        # Title section
        self.title_margin_top = 1.3 * inch
        self.subtitle_margin_top = 1.7 * inch
        self.divider_margin_top = 1.9 * inch
        self.instructions_margin_top = 2.2 * inch
        self.content_start_y = 2.7 * inch
        
        # Category settings
        self.category_header_height = 28
        self.item_height = 18
        self.item_indent = 15
        self.checkbox_size = 12
        self.checkbox_text_offset = 20
        
        # Footer
        self.footer_y = 1.0 * inch
        self.social_footer_y = 0.8 * inch
        
        # Corner decorations
        self.corner_margin = 40
        self.corner_size = 30
    
    def calculate_margins(self, page_width, page_height):
        """Calculate page margins to center the content."""
        # Default side margins
        margin_x = 1 * inch
        
        # Calculate column width based on page width and margins
        self.column_width = (page_width - (2 * margin_x) - self.column_spacing) / 2
        
        return margin_x, self.content_start_y
    
    def get_title_position(self, page_width, text_width):
        """Calculate centered position for title text."""
        return (page_width - text_width) / 2
    
    def get_category_item_y(self, header_y, index):
        """Calculate the y position for a category item."""
        return header_y - ((index + 1) * self.item_height) - 5
