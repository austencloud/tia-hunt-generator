"""
src/generate_scavenger_hunt.py
Main entry point for the specimen scavenger hunt generator
"""
from scavenger_hunt.hunt_generator import ScavengerHuntGenerator

def main():
    """Run the scavenger hunt generator."""
    print("📝 Starting Specimen Scavenger Hunt Generator")
    generator = ScavengerHuntGenerator()
    generator.generate_hunt_pdf()
    print("✅ Done!")

if __name__ == "__main__":
    main()
