import flask
from app.image_processing import process_image


main = flask.Blueprint("main", __name__)
UPLOAD_FOLDER = "uploads/"
ALLOWED_EXTENSIONS = ["png", "jpeg", "jpg"]


@main.route("/")
def index():
    return flask.render_template("index.html")


@main.route("/uploading", methods=["POST"])
def upload_photo():
    photo = flask.request.files.get("photo")
    photo.filename = photo.filename.replace(" ", "_")
    if photo and allowed_file(photo.filename):
        photo.save(UPLOAD_FOLDER + photo.filename)
        return flask.redirect(flask.url_for("main.checkout", file=photo.filename))
    flask.abort(400)


@main.route("/osu")
def osu():
    return flask.redirect("https://osu.ppy.sh/users/28569393")


@main.route("/checkout")
def checkout():
    """На этой странице будет отображаться загруженный файл и прочитанный текст
    В случае неправильного распознования текста пользователь может его исправить"""
    image_name = flask.request.args.get("file")
    if image_name and allowed_file(image_name):
        return flask.render_template("checkout.html",
               data=process_image(image_name), image=image_name)


@main.route("/uploads/<filename>")
def uploaded_file(filename):
    uploads_path = flask.current_app.root_path + "/../uploads"
    return flask.send_from_directory(uploads_path, filename)


def allowed_file(filename:str):
    return filename.split(".")[-1] in ALLOWED_EXTENSIONS
