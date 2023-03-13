from flask import Flask, render_template, send_file, request, abort, url_for
import io
import os
import zipfile

FILE_ROOT = os.environ.get("FILE_ROOT", default="/data")
APP_ROOT = os.environ.get("APP_ROOT", default="/")
if APP_ROOT == "" or APP_ROOT[-1] != "/":
    APP_ROOT = APP_ROOT + "/"

app = Flask(__name__, static_url_path=APP_ROOT+"static")

@app.route(APP_ROOT)
@app.route(APP_ROOT+'<path:path>')
def index(path=''):
    print(path)
    os_path = os.path.join(FILE_ROOT, path)
    if not (os.path.isdir(os_path) or os.path.isfile(os_path)):
        abort(404)
    
    wants_download = bool(request.args.get("dl", default=0, type=int))
    
    if os.path.isfile(os_path):
        return send_file(os_path, as_attachment=wants_download)
    
    if wants_download:
        return _zip_and_download(path, os_path)
    else:
        return _render_listing(path, os_path)

def _render_listing(dir, os_dir):
    dir_contents = []
    for file_name in os.listdir(os_dir):
        size = _get_size(os.path.join(os_dir, file_name))
        size_str = _sizeof_fmt(size)
        dir_contents.append({
            'name': file_name + ("/" if os.path.isdir(os.path.join(os_dir, file_name)) else ""),
            'url': url_for("index", path=os.path.join(dir, file_name)), 
            'size': size_str,
        })
    dir_contents.sort(key=lambda x: x["name"])
    return render_template('index.html', folder="./" + dir, files=dir_contents)

def _zip_and_download(dir: str, os_dir: str):
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for root, _, files in os.walk(os_dir):
            for file in files:
                file_path = os.path.join(root, file)
                zip_file.write(file_path, os.path.relpath(file_path, os_dir))
    return send_file(
        io.BytesIO(buffer.getvalue()),
        mimetype='application/zip',
        as_attachment=True,
        download_name=f'{dir.split("/")[-1]}.zip'
    )

def _get_size(path):
    if os.path.isfile(path):
        return os.path.getsize(path)
    else:
        total = 0
        for dirpath, _, filenames in os.walk(path): 
            for file in filenames:
                try:
                    total += os.path.getsize(os.path.join(dirpath, file)) 
                except:
                    pass
        return total

def _sizeof_fmt(num):
    for unit in ['B', 'KB', 'MB', 'GB']:
        if abs(num) < 1024.0 or unit == 'GB':
            if abs(num) < 10:
                return f"{num:.1f} {unit}"
            else:
                return f"{num:.0f} {unit}"
        num /= 1024.0

if __name__ == '__main__':
    app.run(host="0.0.0.0")
