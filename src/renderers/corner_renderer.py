"""
src/scavenger_hunt/renderers/corner_renderer.py
Corner renderer for scavenger hunt
"""
from reportlab.lib import colors

class CornerRenderer:
    """Renders decorative corners for the scavenger hunt page."""
    
    def __init__(self, canvas):
        self.canvas = canvas
    
    def draw(self, margin, size, corner_size, page_width, page_height):
        """Draw decorative corners on the page."""
        self.canvas.saveState()
        
        # Set appearance
        self.canvas.setStrokeColor(colors.Color(0.4, 0.4, 0.6))
        self.canvas.setLineWidth(1.5)
        
        # Draw top-left corner
        self.canvas.line(
            margin, 
            page_height - margin, 
            margin + corner_size, 
            page_height - margin
        )
        self.canvas.line(
            margin, 
            page_height - margin, 
            margin, 
            page_height - margin - corner_size
        )
        
        # Draw top-right corner
        self.canvas.line(
            page_width - margin, 
            page_height - margin, 
            page_width - margin - corner_size, 
            page_height - margin
        )
        self.canvas.line(
            page_width - margin, 
            page_height - margin, 
            page_width - margin, 
            page_height - margin - corner_size
        )
        
        # Draw bottom-left corner
        self.canvas.line(
            margin, 
            margin, 
            margin + corner_size, 
            margin
        )
        self.canvas.line(
            margin, 
            margin, 
            margin, 
            margin + corner_size
        )
        
        # Draw bottom-right corner
        self.canvas.line(
            page_width - margin, 
            margin, 
            page_width - margin - corner_size, 
            margin
        )
        self.canvas.line(
            page_width - margin, 
            margin, 
            page_width - margin, 
            margin + corner_size
        )
        
        self.canvas.restoreState()
