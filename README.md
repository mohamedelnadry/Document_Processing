# Document Processing

An API that allows users to upload images and PDF files, perform operations on them, and retrieve the results.

## Features

1. Image upload in base64 format
2. Image rotation
3. PDF to image conversion
4. 
## Installation

### local installation

1. Install the required packages:
```bash
pip install -r requirements.txt
```

2. Add a .env file with the following content:

```
DATABASE_NAME = <DATABASE_NAME>
DATABASE_USER = <DATABASE_USER>
DATABASE_PASSWORD = <DATABASE_PASSWORD>
DATABASE_HOST = <DATABASE_HOST>
DATABASE_PORT = <DATABASE_PORT>

# If using docker compose
DATABASE_HOST = 'db'
```

3. Run the server:

```bash
python manage.py runserver
```

### Docker installation
To set up using Docker:
```bash
docker-compose up
```

## Api End Points

* ### Upload Document:

#### Endpoint :` /api/upload`

#### Method: `POST`

#### Request Payload:

`upload`: Base64 encoded content of the image or PDF.

```
 {"upload":"data:application/pdf;base64,JVBERi0xLjQKJdPr6eEKMSAwIG9iag"}
```

#### Response:

```
{
    "detail": "File uploaded successfully.",
    "id": 2,
    "file_type": "pdf"
}
```

* ### List All Images:

#### Endpoint :`/api/images`

#### Method: `GET`

#### Response:

```
[
    {
        "id": 1,
        "image_path": "http://127.0.0.1:8000/media/images/temp-7050.png",
        "width": 818,
        "height": 363,
        "channels": 4
    },
    {
        "id": 2,
        "image_path": "http://127.0.0.1:8000/media/images/temp-8194.png",
        "width": 600,
        "height": 419,
        "channels": 4
    }
]
```

* ### List All PDFs:

#### Endpoint :`/api/pdfs`

#### Method: `GET`

#### Response:

```
[
    {
        "id": 2,
        "pdf_path": "http://127.0.0.1:8000/media/pdfs/temp-8047.pdf",
        "width": "594.96",
        "height": "841.92",
        "num_pages": 2
    },
    {
        "id": 1,
        "pdf_path": "http://127.0.0.1:8000/media/pdfs/temp-1557.pdf",
        "width": "594.96",
        "height": "841.92",
        "num_pages": 2
    }
]
```

* ### Retrieve or Delete an Image:

#### Endpoint :`/api/images/<image_id>`

#### Method:

`GET`: Retrieves the specified image's details.
`DELETE`: Deletes the specified image.

#### Response:

```
{
    "id": 2,
    "image_path": "http://127.0.0.1:8000/media/images/temp-8194.png",
    "width": 600,
    "height": 419,
    "channels": 4
}
```

On Delete

```
{
    "detail": "Image deleted successfully."
}
```

* ### Retrieve or Delete an PDF:

#### Endpoint :`/api/images/<pdf_id>`

#### Method:

`GET`: Retrieves the specified PDF's details.
`DELETE`: Deletes the specified PDF.

#### Response:

```
{
    "id": 1,
    "pdf_path": "http://127.0.0.1:8000/media/pdfs/temp-1557.pdf",
    "width": "594.96",
    "height": "841.92",
    "num_pages": 2
}
```

On Delete

```
{
    "detail": "Image deleted successfully."
}
```

* ### Rotate Image:

#### Endpoint :`/api/rotate`

#### Method: `POST`

#### Request Payload:

`image_id`: ID of the image you want to rotate.
`angle`: Angle to rotate the image (e.g., 45, 90, 180).

```
{
    "image_id":1,
    "angle":30
}
```

#### Response:

```
{
    "detail": "Image updated.",
    "image_id": 1
}
```

* ### Convert PDF to Image:

#### Endpoint :`/api/convert-pdf-to-image`

#### Method: `POST`

#### Request Payload:

`pdf_id`: ID of the PDF you want to convert.

```
{
    "pdf_id":2
}
```

#### Response:

```
{
    "detail": "Converted successfully.",
    "data": [
        {
            "id": 115,
            "image_path": "/media/images/temp-2621(0).jpg",
            "width": 1656,
            "height": 2339,
            "channels": 3
        },
        {
            "id": 116,
            "image_path": "/media/images/temp-2621(1).jpg",
            "width": 1656,
            "height": 2339,
            "channels": 3
        }
    ]
}
```

## Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

### Running tests with pytest

    $ pytest

## License

The MIT License (MIT)
Copyright (c) 2023, elnadry

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following 