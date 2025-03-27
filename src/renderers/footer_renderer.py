"""
src/scavenger_hunt/renderers/footer_renderer.py
Footer renderer for scavenger hunt
"""
from reportlab.lib import colors
from font_manager import FontManager

class FooterRenderer:
    """Renders the footer section for the scavenger hunt page."""
    
    def __init__(self, canvas):
        self.canvas = canvas
    
    def draw(self, x, y, total_items):
        """Draw footer with total count and social media info."""
        self.canvas.saveState()
        
        # Draw total count text
        footer_font = FontManager.get_footer_font()
        self.canvas.setFont(footer_font, 11)
        self.canvas.setFillColor(colors.Color(0.3, 0.3, 0.5))
        
        footer_text = f"How many specimens can you find? Record your total here: ____ / {total_items}"
        footer_width = self.canvas.stringWidth(footer_text, footer_font, 11)
        
        self.canvas.drawString(
            x - (footer_width / 2), 
            y, 
            footer_text
        )
        
        # Draw social media text
        social_text = "Share your discovery journey with us on social media using #InsectAsylumCollection"
        social_width = self.canvas.stringWidth(social_text, footer_font, 11)
        
        self.canvas.drawString(
            x - (social_width / 2), 
            y - 20, 
            social_text
        )
        
        self.canvas.restoreState()