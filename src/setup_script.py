#!/usr/bin/env python3
"""
Setup script for Insect Asylum Scavenger Hunt Generator

This script creates all the necessary directories and files for the
scavenger hunt generator system that integrates with the existing
display card generator.
"""

import os
import sys

# Define the directory structure
DIRECTORIES = [
    "src/scavenger_hunt",
    "src/scavenger_hunt/renderers",
]

def create_directories():
    """Create the necessary directories."""
    for directory in DIRECTORIES:
        try:
            os.makedirs(directory, exist_ok=True)
            print(f"✅ Created directory: {directory}")
        except Exception as e:
            print(f"❌ Error creating directory {directory}: {e}")

def main():
    """Main function to set up the scavenger hunt system."""
    print("🔧 Setting up Insect Asylum Scavenger Hunt Generator")
    
    create_directories()
    print("\n✨ Directory setup complete!")
    print("\nNow create each Python file in the appropriate directory.")
    print("\nTo generate a scavenger hunt PDF, run:")
    print("  python src/generate_scavenger_hunt.py")

if __name__ == "__main__":
    main()
