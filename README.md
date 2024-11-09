"# Todo-list"

Set Up for `Windows` 

> Install modules via `VENV` (windows) 

```
$ virtualenv env
$ .\env\Scripts\activate
$ pip install -r requirements.txt
```

<br />

> Set Up Database

```bash
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py loaddata dump.json
```

<br />

> Start the app

```bash
$ python manage.py runserver
```

At this point, the app runs at `http://127.0.0.1:8000/`. 

<br />

Task List page:
![img_2.png](imgs/img_2.png)

Task Delete page:
![img.png](imgs/img.png)

Task Update/Create page:
![img_1.png](imgs/img_1.png)

Tag list page:
![img_3.png](imgs/img_3.png)

Tag update page:
![img_4.png](imgs/img_4.png)

Tag delete page:
![img_5.png](imgs/img_5.png)