import os
from pathlib import Path

import requests

from app import app

# ----------------------------------------
# launch
# ----------------------------------------

upload_image_dir = "./app/views/images"
if not os.path.exists(upload_image_dir):
    os.mkdir(upload_image_dir)

filename = "./app/static/js/simple-drawing-board.min.js"
if not os.path.exists(filename):
    url = "https://raw.githubusercontent.com/leaysgur/simple-drawing-board.js/refs/heads/main/dist/simple-drawing-board.min.js"

    urlData = requests.get(url).content

    dir = Path(filename).parent
    if not os.path.exists(dir):
        os.mkdir()

    with open(filename, mode="wb") as f:  # wb でバイト型を書き込める
        f.write(urlData)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=port, debug=True)
