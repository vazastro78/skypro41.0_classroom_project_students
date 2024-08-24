# Django проект работы со "студентами"

Ключевые слова:
- django
- skypro_python41.0
- студенты

### Эволюция проекта
- [x] Классная работа "20.1 Работа с ORM (Object-Relational Mapping) в Django"
- [x] Классная работа "20.2 Работа с шаблонами, статическими файлами, шаблоном bootstrap"
- [?] Классная работа "21.1 Работа FBV (function based views) и CBV (class based views)"

### Шаг за шагом

#### 20.1 Работа с ORM (Object-Relational Mapping) в Django

 - Настройка работы с базой данных  СУБД PostgreSQL
 - Создаем модель в Django для класса студент (class Student)
 - Создаем миграцию и применяем миграцию с номером 0001
 - Настраиваем пути в urls.py, MEDIA_URL и MEDIA_ROOT
 - Создаем контроллер index в views.py и страницу templates/students/index.html
 - Настраиваем админку, python manage.py createsuperuser
 - Заполнение базы данных python manage.py dumpdata и loaddata

#### 20.2  Шаблонизация в Django

 - Настройка статических файлов
 - Шаблоны на основе Bootstrap
 - Подшаблоны и базовые шаблоны
 - Новые шаблонные теги и фильтры в templatetags/path_tag_filter.py
 - Ссылки на рисунки и меню

#### 21.1 Работа FBV (function based views) и CBV (class based views)

 - Добавляем для students методы ListView и  DetailView в парадигме CRUD 
> CRUD (create, read, update, delete) — механизм, который реализует простой функционал создания, просмотра, обновления и удаления сущностей.
 - MaterialListView и MaterialCreateView для просмотра всего списка и создания одного элемента
 - 

#### создаем проект django и приложение students

```bash
 export PY_PROJECT=skypro41.0_classroom_project_students #наименование проекта
 mkdir $PY_PROJECT  #создаем директорию проекта
 cd $PY_PROJECT #переходим в рабочую директорию
 django-admin startproject config . #инициализируем проект
 python3 -m venv env #создаем виртуальное окружение
 source env/bin/activate #переходим в виртуальное окружение
 pip3 install django #устанавливаем в виртуальном окружении django
 pip3 freeze > requirements.txt #записываем зависимости
 pip3 install -r requirements.txt 
```

```bash
python3 manage.py startapp students
touch students/urls.py
mkdir -p students/templates/students
mkdir -p static/css static/js static/images
```

#### github

create repository on github and synchronize with offline repository

```bash
git remote add origin git@github.com:vazastro78/skypro41.0_classroom_project_students.git
git branch -M main
git push -u origin main


git checkout -b 20_1_classroom #создаем и переключаемся на новую ветку
git checkout main
git merge 20_1_classroom

git checkout -b 20_2_classroom_templates

git checkout -b 21.1_classroom_FBV_CBV

#git remote remove origin
#git clone  git@github.com:vazastro78/skypro41.0_classroom_project_students.git
```
