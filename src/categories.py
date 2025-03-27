"""
Categories and color schemes for display item cards and scavenger hunt
"""

from reportlab.lib import colors

# Define categories with their color schemes
CATEGORIES = {
    "Minerals & Fossils": {
        "color": colors.Color(0.6, 0.6, 0.9),  # Lighter blue-purple
        "text_color": colors.white,
        "gradient_start": colors.Color(0.7, 0.7, 1.0),
        "gradient_end": colors.Color(0.85, 0.85, 1.0),
        "border_color": colors.Color(0.5, 0.5, 0.8),
        "pattern_color": colors.Color(0.7, 0.7, 1.0, 0.1),
    },
    "Shells & Marine": {
        "color": colors.Color(0.2, 0.7, 0.7),  # Turquoise
        "text_color": colors.white,
        "gradient_start": colors.Color(0.3, 0.8, 0.8),
        "gradient_end": colors.Color(0.5, 0.9, 0.9),
        "border_color": colors.Color(0.1, 0.6, 0.6),
        "pattern_color": colors.Color(0.3, 0.8, 0.8, 0.1),
    },
    "Plant Materials": {
        "color": colors.Color(0.3, 0.7, 0.4),  # Green
        "text_color": colors.white,
        "gradient_start": colors.Color(0.4, 0.8, 0.5),
        "gradient_end": colors.Color(0.6, 0.9, 0.7),
        "border_color": colors.Color(0.2, 0.6, 0.3),
        "pattern_color": colors.Color(0.4, 0.8, 0.5, 0.1),
    },
    "Preserved Specimens": {
        "color": colors.Color(0.8, 0.7, 0.2),  # Amber
        "text_color": colors.black,
        "gradient_start": colors.Color(0.9, 0.8, 0.3),
        "gradient_end": colors.Color(1.0, 0.9, 0.5),
        "border_color": colors.Color(0.7, 0.6, 0.1),
        "pattern_color": colors.Color(0.9, 0.8, 0.3, 0.1),
    },
    "Animal Parts": {
        "color": colors.Color(0.7, 0.5, 0.3),  # Brown
        "text_color": colors.white,
        "gradient_start": colors.Color(0.8, 0.6, 0.4),
        "gradient_end": colors.Color(0.9, 0.8, 0.6),
        "border_color": colors.Color(0.6, 0.4, 0.2),
        "pattern_color": colors.Color(0.8, 0.6, 0.4, 0.1),
    },
    "Bones & Skulls": {
        "color": colors.Color(0.7, 0.7, 0.7),  # Gray
        "text_color": colors.black,
        "gradient_start": colors.Color(0.8, 0.8, 0.8),
        "gradient_end": colors.Color(0.95, 0.95, 0.95),
        "border_color": colors.Color(0.6, 0.6, 0.6),
        "pattern_color": colors.Color(0.7, 0.7, 0.7, 0.1),
    },
    "Resin Replicas": {
        "color": colors.Color(0.9, 0.7, 0.4),  # Light orange
        "text_color": colors.black,
        "gradient_start": colors.Color(1.0, 0.8, 0.5),
        "gradient_end": colors.Color(1.0, 0.9, 0.7),
        "border_color": colors.Color(0.8, 0.6, 0.3),
        "pattern_color": colors.Color(1.0, 0.8, 0.5, 0.1),
    },
    "Miscellaneous": {
        "color": colors.Color(0.5, 0.5, 0.5),  # Neutral gray
        "text_color": colors.white,
        "gradient_start": colors.Color(0.6, 0.6, 0.6),
        "gradient_end": colors.Color(0.8, 0.8, 0.8),
        "border_color": colors.Color(0.4, 0.4, 0.4),
        "pattern_color": colors.Color(0.6, 0.6, 0.6, 0.1),
    },
}


def get_category_colors(category):
    """Get color scheme for a category, with fallback to default."""
    if category in CATEGORIES:
        return CATEGORIES[category]

    # Default color scheme
    return {
        "color": colors.Color(0.5, 0.5, 0.5),
        "text_color": colors.white,
        "gradient_start": colors.Color(0.6, 0.6, 0.6),
        "gradient_end": colors.Color(0.8, 0.8, 0.8),
        "border_color": colors.Color(0.4, 0.4, 0.4),
        "pattern_color": colors.Color(0.6, 0.6, 0.6, 0.1),
    }
