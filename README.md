# Django проект работы со "студентами"

Ключевые слова:
- django
- skypro_python41.0
- студенты

### Эволюция проекта
- [x] Классная работа "20.1 Работа с ORM (Object-Relational Mapping) в Django"

### Шаг за шагом

#### 20.1 Работа с ORM (Object-Relational Mapping) в Django

 - Настройка работы с базой данных  СУБД PostgreSQL

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


git checkout -b 20_1_classroom


#git remote remove origin
#git clone  git@github.com:vazastro78/skypro41.0_classroom_project_students.git
```
