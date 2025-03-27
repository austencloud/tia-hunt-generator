"""
Font management for scavenger hunt
"""

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


class FontManager:
    """
    Handles font registration and management for the scavenger hunt.
    """

    @staticmethod
    def register_fonts():
        """Register all required fonts for the scavenger hunt."""
        try:
            # Register DejaVu font family
            pdfmetrics.registerFont(TTFont("DejaVuSans", "DejaVuSans.ttf"))
            pdfmetrics.registerFont(TTFont("DejaVuSans-Bold", "DejaVuSans-Bold.ttf"))
            pdfmetrics.registerFont(
                TTFont("DejaVuSans-Oblique", "DejaVuSans-Oblique.ttf")
            )
            pdfmetrics.registerFont(
                TTFont("DejaVuSans-BoldOblique", "DejaVuSans-BoldOblique.ttf")
            )
            pdfmetrics.registerFont(TTFont("DejaVuSerif", "DejaVuSerif.ttf"))
            pdfmetrics.registerFont(TTFont("DejaVuSerif-Bold", "DejaVuSerif-Bold.ttf"))

            print("✅ Fonts registered successfully.")
        except Exception as e:
            print(f"⚠️ Warning: Could not register DejaVu fonts ({e})")
            print("📝 Using standard fonts instead.")

    @staticmethod
    def get_header_font():
        """Get the appropriate font for headers."""
        return "DejaVuSans-Bold"

    @staticmethod
    def get_title_font():
        """Get the appropriate font for titles."""
        return "DejaVuSans-Bold"

    @staticmethod
    def get_subtitle_font():
        """Get the appropriate font for subtitles."""
        return "DejaVuSans-Bold"

    @staticmethod
    def get_body_font():
        """Get the appropriate font for body text."""
        return "DejaVuSans"

    @staticmethod
    def get_footer_font():
        """Get the appropriate font for footer text."""
        return "DejaVuSans-Oblique"

    @staticmethod
    def get_category_font(category=None):
        """Get the appropriate font for category headers."""
        # This could be expanded to use different fonts for different categories
        return "DejaVuSans-Bold"

    @staticmethod
    def get_item_font(category=None):
        """Get the appropriate font for category items."""
        # This could be expanded to use different fonts for different categories
        return "DejaVuSans"
