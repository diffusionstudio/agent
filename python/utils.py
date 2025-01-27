import os

def clear_file_path(output: str):
    """Clears the output path if it exists."""
    if os.path.exists(output):
        os.remove(output)
        print(f"Removed existing file: {output}")
