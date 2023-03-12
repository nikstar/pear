# Pear 🍐

Pear is a simple file server web app built with Flask that allows downloading files and zipped directories.

## Getting Started

To get started with Pear, you can clone the repository and run the following command:

```sh
git clone https://github.com/nikstar/pear.git
cd pear
pip install -r requirements.txt
flask run # or python app.py
```

This will start the server and you can access it by going to http://localhost:5000/ in your web browser.

## Usage

By default, Pear serves files from the /data directory. You can change this by setting the FILE_ROOT environment variable.

```sh
export FILE_ROOT=/path/to/your/files
flask run
```

You can also specify a custom app root by setting the APP_ROOT environment variable. This allows you to serve Pear under a subpath on your domain.

```sh
export APP_ROOT=/pear
flask run
```

## License

Pear is released under the MIT License.