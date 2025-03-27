"""
src/renderers/checkbox_renderer.py
Checkbox renderer for scavenger hunt
"""
from reportlab.lib import colors

class CheckboxRenderer:
    """Renders checkboxes for scavenger hunt items."""
    
    def __init__(self, canvas):
        self.canvas = canvas
    
    def draw(self, x, y, size=12):
        """Draw a checkbox."""
        self.canvas.saveState()
        
        # Draw the box with slightly thicker lines for better visibility
        self.canvas.setStrokeColor(colors.black)
        self.canvas.setLineWidth(0.75)  # Increased from 0.5 for better visibility
        self.canvas.rect(
            x, y, 
            size, size, 
            fill=0, stroke=1
        )
        
        self.canvas.restoreState()