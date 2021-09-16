# Yearbook for ECE Batch of 2024, NITK

This is a project to maintain a yearbook for the students of batch of 2024 of the Department of Electronics and Communication Engineering, National Institute of Technology, Karnataka.

## Installation Guide
- Fork the repository and clone your personal fork.
```
git clone https://github.com/{your_github_username}/yearbook.git
```

- Create a virtual environment, and activate it. For Windows, it is
```
python -m venv venv
venv\Scripts\activate
```
For Linux and MacOS, you can create it using this:
```
python3 -m venv venv
source venv/bin/activate
```
- Run `pip install -r requirements.txt` to install all the necessary requirements.
- Run `python manage.py migrate` to set up the database.
- Run `python manage.py createsuperuser` to make the superuser for all dev purposes.
- You will have to create a `.env` file so that you can store the Django SECRET_KEY. Create one file. In the command prompt, type:
```
python manage.py shell
# Inside the shell
from django.core.management.utils import get_random_secret_key
get_random_secret_key()
```
You will get a secret key generated. Save it in the `.env` file as `SECRET_KEY='{generated_secret_key}'`

- For development purposes, I highly recommend you set `DEBUG=True` in `settings.py`. <b>Make sure you make `DEBUG=False` before any merge request.</b>

- To get the server up and running, use `python manage.py runserver`. A server will start working

## Other Information
This project is made using Django, a popular web framework based on Python. If you want to learn the basics about Django, [this](https://tutorial.djangogirls.org/) is a great resource.

The front end is made using Bootstrap.

## Contributing
All contributors are welcome! If you want to create an issue, [go here](https://github.com/anirudhprabhakaran3/yearbook/issues). If it is a bug, make sure you attach a screenshot so that it becomes easy for the developer to accurately locate and fix it. If it is a feature request, make sure you provide as much information as you can, so that developers can accurately work on it.

If you're a developer looking to contribute, check out the [issues](https://github.com/anirudhprabhakaran3/yearbook/issues) page. For beginners, we have some [good first issues](https://github.com/anirudhprabhakaran3/yearbook/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22). Feel free to drop a comment on issues if you have any questions!

<b>Before you start working on an issue, comment as such on the issue, and wait until it is assigned to you. Pull Requests by people who have not been assigned issues will not be accepted.</b>