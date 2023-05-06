# Проект **Yamdb_final**
![example workflow](https://github.com/Rishat-Ver/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

### **URL проекта Yamdb_final:**
http://84.252.143.251/admin <br>
http://84.252.143.251/api/v1/ <br>
http://84.252.143.251/redoc/ <br>

---

### **Описание проекта:**
*Проект Yamdb_final собирает отзывы пользователей на произведения. Сами произведения в Yamdb_final не хранятся, здесь нельзя посмотреть фильм или послушать музыку.*
*Произведения делятся на категории, такие как «Книги», «Фильмы», «Музыка». Например, в категории «Книги» могут быть произведения «Винни-Пух и все-все-все» и «Марсианские хроники», а в категории «Музыка» — песня «Давеча» группы «Жуки» и вторая сюита Баха. Список категорий может быть расширен (например, можно добавить категорию «Изобразительное искусство» или «Ювелирка»).* 
*Произведению  может быть присвоен жанр из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»).* 
*Добавлять произведения, категории и жанры может только администратор.*
*Благодарные или возмущённые пользователи оставляютк произведениям  текстовые отзывы и ставят произведению оценку в диапазоне от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка произведения — рейтинг (целое число). На одно произведение пользователь может оставить только один отзыв.*
*Пользователи могут оставлять комментарии к отзывам.*
*Добавлять отзывы, комментарии и ставить оценки могут только аутентифицированные пользователи...*

---

### **Технологии:**
Python 3.7 <br>
Django 3.2 <br>
DRF 3.12.4 <br>
JWT <br>
Docker Hub <br>
Github Actions <br>
Yandex cloud <br>

---

### **Команда разработчиков:**
- Менеджер Ольга Рогачева
- Ришат https://github.com/Rishat-Ver
- Даша https://github.com/striki23
- Сергей https://github.com/code-nf

---

### **Запуск проекта:**
```
git clone git@github.com:Rishat-Ver/yamdb_final.git
python3 -m venv venv
source /venv/Scripts/activate 
python -m pip install --upgrade pip
pip install -r requirements.txt
docker build -t rishat1991/yamdb_final:latest .
docker login -u rishat1991 
# вводим пароль от Docker Hub
docker push rishat1991/yamdb_final:latest
apt install docker.io
sudo curl -L "https://github.com/docker/compose/releases/download/1.26.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo systemctl stop nginx
git add .
git commit -m ""
git push

```

---

### **шаблон наполнения env-файла**

```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=rishik
DB_HOST=db
DB_PORT=5432
SECRET_KEY='++s4p8%m9_hylnw*(+$f4+n46)^01_)ibpqt3-j_-!@srfg63)'

```
---
### **Actions secrets**

```
DB_ENGINE - django.db.backends.postgresql
DB_HOST - db
DB_NAME - postgres 
DB_PORT - 5432
DOCKER_PASSWORD - пароль пользователя в DockerHub
DOCKER_USERNAME - имя пользователя в DockerHub
HOST - ip-адрес сервера
POSTGRES_PASSWORD - rishik
POSTGRES_USER - postgres
SECRET_KEY - секретный ключ приложения django
SSH_KEY - SSH ключ (cat ~/.ssh/id_rsa.pub)
TELEGRAM_TO - id своего телеграм-аккаунта
TELEGRAM_TOKEN - токен бота
USER - пользователь

```

---

### **Документация API YaMDb**
Документация: http://84.252.143.251/redoc/

---

Данный проект , является совместной работой трех начинающих разроботчиков (Ришат , Даша , Сергей) <br>
Он сделан в рамках обучения на курсе Python-рфзроботчик Яндекс-Практикума <br>
На данный момент по работе с настройкой сервера , докера и т п работал Ришат Вергасов <br>
https://github.com/Rishat-Ver/backend_test_homework
