from PIL import Image
from io import BytesIO


def load_cover(cover_data):

    if cover_data is None:
        return None

    try:
        image = Image.open(
            BytesIO(cover_data)
        )

        image = image.convert("RGB")

        image = image.resize(
            (120, 120)
        )

        return image

    except Exception as e:
        print("Cover fout:", e)
        return None