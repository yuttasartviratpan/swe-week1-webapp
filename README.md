# Vending Machine Tracking Application (Assignment)

[![SonarCloud](https://sonarcloud.io/images/project_badges/sonarcloud-black.svg)](https://sonarcloud.io/summary/new_code?id=yuttasartviratpan_swe-week1-webapp)

Before you clone this repo, please install and make virtualenv and 
install packages in there. Then clone this repo to where you did virtualenv

## Steps to run

**Prerequisites**:

- Python 3 (I used 3.8)
- [Virtualenv](https://gist.github.com/Geoyi/d9fab4f609e9f75941946be45000632b)
    - `sudo apt-get install python3-pip`
    - `sudo pip3 install virtualenv`
    - `virtualenv -p python3 .` 
      - If you want a directory created, then do: `virtualenv -p python3 <dir name>` 

**Django Installation**:

From where you ran `virtualenv -p python3 .`, do `source bin/activate`.

Or if you did `virtualenv -p python3 <dir name>`, then `<dir name>/source bin/activate`

After that, do: 
- `pip install django`

Now you can clone the repo.

**Steps**:

Make sure that your `virtualenv` is activated

- Run the server by
    - ```python3 manage.py runserver```
- Test app by sending request using `Postman`, or any other application
that can do http requests.
