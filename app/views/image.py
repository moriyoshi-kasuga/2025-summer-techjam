from flask import Blueprint, Response, request

blueprint = Blueprint(
    "image", __name__, static_folder="images", static_url_path="/images"
)


def save_image(id: str, image: str):
    with open(f"app/views/images/{id}", "wb") as f:
        f.write(image.encode("utf-8"))


@blueprint.route("/")
def image():
    image_name = request.args.get("id")
    if not image_name:
        # If no image name is provided, return error response
        return Response("Image name is required", status=400, mimetype="text/plain")

    return blueprint.send_static_file(f"{image_name}")
