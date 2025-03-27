"""
src/scavenger_hunt/renderers/header_renderer.py
Header renderer for scavenger hunt
"""
from reportlab.lib import colors
from reportlab.lib.units import inch

class HeaderRenderer:
    """Renders the title and instructions for the scavenger hunt page."""
    
    def __init__(self, canvas):
        self.canvas = canvas
    
    def draw(self, title, subtitle, instructions, page_width, page_height):
        """Draw title, subtitle, and instructions."""
        # Draw title
        self.canvas.setFont("DejaVuSans-Bold", 24)
        self.canvas.setFillColor(colors.Color(0.3, 0.3, 0.5))
        title_width = self.canvas.stringWidth(title, "DejaVuSans-Bold", 24)
        
        # Add title with shadow effect
        self.canvas.setFillColor(colors.Color(0.3, 0.3, 0.5, 0.3))
        self.canvas.drawString(
            (page_width - title_width) / 2 + 2, 
            page_height - 1.3 * inch - 2, 
            title
        )
        
        self.canvas.setFillColor(colors.Color(0.3, 0.3, 0.5))
        self.canvas.drawString(
            (page_width - title_width) / 2, 
            page_height - 1.3 * inch, 
            title
        )
        
        # Draw subtitle
        self.canvas.setFont("DejaVuSans-Bold", 18)
        self.canvas.setFillColor(colors.Color(0.4, 0.4, 0.6))
        subtitle_width = self.canvas.stringWidth(subtitle, "DejaVuSans-Bold", 18)
        self.canvas.drawString(
            (page_width - subtitle_width) / 2, 
            page_height - 1.7 * inch, 
            subtitle
        )
        
        # Draw decorative line under subtitle
        self.canvas.setStrokeColor(colors.Color(0.4, 0.4, 0.6))
        self.canvas.setLineWidth(1)
        line_width = 5 * inch
        self.canvas.line(
            (page_width - line_width) / 2, 
            page_height - 1.9 * inch,
            (page_width + line_width) / 2, 
            page_height - 1.9 * inch
        )
        
        # Draw instructions (with handling for long text)
        self.canvas.setFont("DejaVuSans", 11)
        self.canvas.setFillColor(colors.black)
        instructions_width = self.canvas.stringWidth(instructions, "DejaVuSans", 11)
        
        # Calculate instruction position and handle wrapping
        if instructions_width > page_width - 2 * inch:
            words = instructions.split()
            line1 = []
            line2 = []
            current_width = 0
            
            for word in words:
                word_width = self.canvas.stringWidth(word + " ", "DejaVuSans", 11)
                if current_width + word_width < page_width - 2 * inch:
                    line1.append(word)
                    current_width += word_width
                else:
                    line2.append(word)
            
            line1_text = " ".join(line1)
            line2_text = " ".join(line2)
            
            line1_width = self.canvas.stringWidth(line1_text, "DejaVuSans", 11)
            line2_width = self.canvas.stringWidth(line2_text, "DejaVuSans", 11)
            
            self.canvas.drawString((page_width - line1_width) / 2, page_height - 2.2 * inch, line1_text)
            self.canvas.drawString((page_width - line2_width) / 2, page_height - 2.4 * inch, line2_text)
            
            return 2.7 * inch  # Return the position where content should start
        else:
            self.canvas.drawString(
                (page_width - instructions_width) / 2, 
                page_height - 2.2 * inch, 
                instructions
            )
            return 2.5 * inch  # Return the position where content should start
