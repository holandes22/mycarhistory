# About

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

## Setting development environment


### Backend

Run all the actions below in a virtual env.

    cd mycarhistory
    pip install -r requirements.txt
    pip install ansible
    vagrant up

Choose default option for all steps below:

    fab vagrant syncdb
    fab vagrant createsuperuser
    fab vagrant migrate  # in order to apply token migration from DRF
    fab vagrant runserver  # choose the default dev option, runs at localhost:8888 (from VM)


### Frontend

You need to have PhantomJS installed to be able to run the tests from the command line:

    npm install -g phantomjs # you might need sudo for this

Open another window terminal and run:

    cd frontend
    npm install
    grunt server  # serves frontend at localhost:8000
