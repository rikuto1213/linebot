import base64
from pathlib import Path
from bot_app.models import ImageData  # ← your_app を実際のアプリ名に変更してね

def save_image_to_db(image_path, name='default'):
    """
    画像をbase64にエンコードしてDBに保存する
    """
    path = Path(image_path)

    if not path.exists():
        print(f"ファイルが存在しません: {image_path}")
        return

    with path.open('rb') as img_file:
        encoded_str = base64.b64encode(img_file.read()).decode('utf-8')
        print(encoded_str)

    image_data = ImageData(name=name, image_base64=encoded_str)
    image_data.save()
    print(f"保存完了: {name}")
