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

## Docker

To run Pear with Docker.

```sh
docker run -p 5000:5000 -e APP_ROOT=/myapp -v /path/to/data:/data nikstar/pear:latest
```

### Build from source

Clone the repository and navigate to the project directory.

```sh
git clone https://github.com/nikstar/pear.git
cd pear
```

Build the Docker image.

```sh
docker build -t pear .
```

Start the container.

```sh
docker run -p 5000:5000 -e APP_ROOT=/myapp -v /path/to/data:/data pear
```

### Using docker-compose

Use `docker-compose.yml` from this repository or create your own::

```yaml
version: "3.9"
services:
  pear:
    image: nikstar/pear 
    environment:
      APP_ROOT: /myapp
    volumes:
      - /path/to/data:/data
    ports:
      - "5001:5000"
```

Start the container with docker-compose.

```sh
docker-compose up
```

This will start Pear on port 5001 and you can access it by going to http://localhost:5001/myapp in your web browser.

Note that you can customize the environment variables, volumes, and external port to fit your needs.

## License

Pear is released under the MIT License.
