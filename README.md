# Super cute place holder images

Super simple way to add [placekitten](http://placekitten.com) images to your Django templates.

## Installation

1. Download the place_kitten app and place it somewhere on your Python path
2. Add `place_kitten` to your `INSTALLED_APPS`
3. Load the tag in your templates `{% load placekitten %}`

*requires [Django classy tags](https://github.com/ojii/django-classy-tags)*

## Usage

Just load the tag and pass in the required image width & height and it prints an image tag for you.
    
    {% placekitten 200 150 %}
    # <img src="http://placekitten.com/200/150" width="200" height="150" alt="I can haz placeholder?" />

By default it outputs a colour image, if you would like a Black & White image you can add an optional 3rd paramater.

    {% placekitten 200 150 "b&w" %}
    # <img src="http://placekitten.com/g/200/150" width="200" height="150" alt="I can haz placeholder?" />
