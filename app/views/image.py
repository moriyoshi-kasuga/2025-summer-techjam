from flask import Blueprint, Response, request


blueprint = Blueprint(
    "image", __name__, static_folder="images", static_url_path="/images"
)


def save_image(id: str, image_data: bytes):
    with open(f"{blueprint.static_folder}/{id}", "wb") as f:
        f.write(image_data)


@blueprint.route("/", methods=["GET"])
def image():
    image_name = request.args.get("id")
    if not image_name:
        return Response("Image name is required", status=400, mimetype="text/plain")

    return blueprint.send_static_file(image_name)
