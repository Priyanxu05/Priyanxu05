import sys
from pathlib import Path

import cv2
from PIL import Image


def remove_background(input_path, output_path):

    try:
        from rembg import remove

        print("Removing background...")

        image = Image.open(input_path).convert("RGBA")

        result = remove(image)

        # Create white background
        background = Image.new(
            "RGBA",
            result.size,
            "white"
        )

        background.alpha_composite(result)

        background.convert("RGB").save(
            output_path
        )

        print("Background removed successfully.")

    except Exception as e:

        print("Background removal failed.")
        print("Using original image instead.")
        print(e)

        image = Image.open(
            input_path
        ).convert("RGB")

        image.save(
            output_path
        )


def enhance_image(input_path, output_path):

    print("Improving contrast...")

    image = cv2.imread(
        str(input_path)
    )

    if image is None:
        raise FileNotFoundError(
            f"Could not read {input_path}"
        )

    # Convert to grayscale
    gray = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

    # Improve local contrast
    clahe = cv2.createCLAHE(
        clipLimit=2.0,
        tileGridSize=(8, 8)
    )

    enhanced = clahe.apply(gray)

    # Slight smoothing
    enhanced = cv2.GaussianBlur(
        enhanced,
        (3, 3),
        0
    )

    cv2.imwrite(
        str(output_path),
        enhanced
    )

    print("Contrast enhancement complete.")


def main():

    if len(sys.argv) < 2:

        print(
            "Usage:"
        )

        print(
            "python scripts/prep_photo.py source-photo.jpg"
        )

        return

    input_path = Path(
        sys.argv[1]
    )

    if not input_path.exists():

        print(
            f"ERROR: File not found: {input_path}"
        )

        return

    # Make sure data folder exists
    data_folder = Path("data")

    data_folder.mkdir(
        parents=True,
        exist_ok=True
    )

    temp_path = (
        data_folder /
        "temp-white.png"
    )

    output_path = (
        data_folder /
        "source-prepped.png"
    )

    # Step 1
    remove_background(
        input_path,
        temp_path
    )

    # Step 2
    enhance_image(
        temp_path,
        output_path
    )

    # Remove temporary file
    if temp_path.exists():

        temp_path.unlink()

    print()
    print("==============================")
    print("Photo preparation complete!")
    print("==============================")
    print()
    print(
        f"Output: {output_path}"
    )


if __name__ == "__main__":
    main()