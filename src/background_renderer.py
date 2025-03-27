"""
src/scavenger_hunt/renderers/background_renderer.py
Background renderer for scavenger hunt
"""
import random
from reportlab.lib import colors

class BackgroundRenderer:
    """Renders the background for the scavenger hunt page."""
    
    def __init__(self, canvas):
        self.canvas = canvas
    
    def draw(self, x, y, width, height):
        """Draw the full background with subtle pattern."""
        # Draw base gradient
        self._draw_gradient_background(x, y, width, height)
        
        # Draw subtle pattern
        self._draw_subtle_pattern(x, y, width, height)
    
    def _draw_gradient_background(self, x, y, width, height, steps=20):
        """Draw a gradient background for the entire page."""
        start_color = colors.Color(0.95, 0.95, 1.0)  # Light blue-gray
        end_color = colors.Color(1.0, 1.0, 1.0)      # White
        
        for i in range(steps):
            ratio = i / float(steps - 1)
            r = start_color.red + (end_color.red - start_color.red) * ratio
            g = start_color.green + (end_color.green - start_color.green) * ratio
            b = start_color.blue + (end_color.blue - start_color.blue) * ratio
            current_color = colors.Color(r, g, b)
            
            self.canvas.setFillColor(current_color)
            segment_height = height / steps
            self.canvas.rect(
                x, y + i * segment_height,
                width, segment_height + 1,  # Slight overlap
                fill=1, stroke=0
            )
    
    def _draw_subtle_pattern(self, x, y, width, height):
        """Draw a subtle dot pattern on the background."""
        pattern_color = colors.Color(0.5, 0.5, 0.8, 0.05)
        self.canvas.setFillColor(pattern_color)
        
        # Draw a grid of small dots
        spacing = 15
        dot_size = 0.8
        
        for i in range(int(width / spacing) + 1):
            for j in range(int(height / spacing) + 1):
                # Add some random offset for a more natural look
                offset_x = random.uniform(-1.5, 1.5)
                offset_y = random.uniform(-1.5, 1.5)
                
                dot_x = x + (i * spacing) + offset_x
                dot_y = y + (j * spacing) + offset_y
                
                if dot_x >= x and dot_x <= x + width and dot_y >= y and dot_y <= y + height:
                    self.canvas.circle(dot_x, dot_y, dot_size, fill=1, stroke=0)
