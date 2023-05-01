# Проект **Yamdb_final**
![example workflow](https://github.com/Rishat-Ver/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

### **Описание проекта:**
*Проект Yamdb_final собирает отзывы пользователей на произведения. Сами произведения в Yamdb_final не хранятся, здесь нельзя посмотреть фильм или послушать музыку.*
*Произведения делятся на категории, такие как «Книги», «Фильмы», «Музыка». Например, в категории «Книги» могут быть произведения «Винни-Пух и все-все-все» и «Марсианские хроники», а в категории «Музыка» — песня «Давеча» группы «Жуки» и вторая сюита Баха. Список категорий может быть расширен (например, можно добавить категорию «Изобразительное искусство» или «Ювелирка»).* 
*Произведению может быть присвоен жанр из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»).* 
*Добавлять произведения, категории и жанры может только администратор.*
*Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы и ставят произведению оценку в диапазоне от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка произведения — рейтинг (целое число). На одно произведение пользователь может оставить только один отзыв.*
*Пользователи могут оставлять комментарии к отзывам.*
*Добавлять отзывы, комментарии и ставить оценки могут только аутентифицированные пользователи.*

---

### **Технологии:**
Python 3.7 <br>
Django 3.2 <br>
DRF 3.12.4 <br>
JWT <br>
Docker Desktop <br>
Docker Hub <br>
Github Actions <br>
Yandex cloud 

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
sudo systemctl stop nginx
sudo apt install docker.io

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
SECRET_KEY

```

---

### **Документация API YaMDb**
Документация: http://localhost/redoc/

---

[example branch parameter](https://github.com/Rishat-Ver/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg) <br>
Данный проект , является совместной работой трех начинающих разроботчиков (Ришат , Даша , Сергей) <br>
Он сделан в рамках обучения на курсе Python-рфзроботчик Яндекс-Практикума <br>
На данный момент по работе с настройкой сервера , докера и т п работал Ришат Вергасов <br>
https://github.com/Rishat-Ver/backend_test_homework