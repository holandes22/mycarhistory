About
-----

I started this project mainly to learn three things:

- Ember.js
- ember-data
- Django REST Framework

While also making something that might be useful to someone.
The idea is to give you a place to track the treatments done to your car
both for personal reference and when maybe selling the car publishing the
details to a public profile for potential buyers to look at the info.

It's and open source project based on:

- Django 1.6
- Ember.js - Following Latest
- Ember Data - Following Latest Beta branch
- Django REST Framework - https://github.com/tomchristie/django-rest-framework/
- Ember Data DRF Adapter - https://github.com/toranb/ember-data-django-rest-adapter/

At the beginning I had no idea how to make it work, but thanks to @toranb
who made an example project https://github.com/toranb/complex-ember-data-example/
I was able to start building something

Getting started
---------------

After cloning the repo:

    cd mycarhistory
    pip install -r requirements.txt  # Best in a venv
    librarian-puppet install  # you need librarian-puppet installed: gem install librarian-puppet
    vagrant up
    fab vagrant syncdb
    fab vagrant createsuperuser
    fab vagrant runserver  # choose the default dev option

In another window:
    cd mycarhistory/frontend
    bower install
    npm install
    grunt server  # serves frontend at localhost:8000


