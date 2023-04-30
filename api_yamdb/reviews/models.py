from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from .validators import validate_username, validate_year

USER = "user"
MODERATOR = "moderator"
ADMIN = "admin"
USER_RU = "юзер"
MODERATOR_RU = "модератор"
ADMIN_RU = "админ"
ROLES = (
    (USER, USER_RU),
    (MODERATOR, MODERATOR_RU),
    (ADMIN, ADMIN_RU),
)


class User(AbstractUser):
    username = models.CharField(
        verbose_name="Пользователь",
        validators=(validate_username,),
        max_length=150,
        unique=True,
        blank=False,
        null=False,
    )
    email = models.EmailField(
        verbose_name="E-Mail",
        unique=True,
        max_length=254,
        blank=False,
        null=False,
    )
    bio = models.TextField(verbose_name="О себе", blank=True, max_length=300)
    first_name = models.CharField(
        verbose_name="имя", max_length=150, blank=True
    )
    last_name = models.CharField(
        verbose_name="фамилия", max_length=150, blank=True
    )
    role = models.CharField(
        verbose_name="Уровень доступа",
        choices=ROLES,
        default=USER,
        blank=True,
        max_length=50,
    )

    @property
    def is_user(self):
        return self.role == USER

    @property
    def is_admin(self):
        return self.role == ADMIN

    @property
    def is_moderator(self):
        return self.role == MODERATOR

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username


class Category(models.Model):
    name = models.TextField(max_length=256, verbose_name="Название категории")
    slug = models.SlugField(unique=True, verbose_name="Слаг категории")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.slug


class Genre(models.Model):
    name = models.TextField(max_length=256, verbose_name="Название жанра")
    slug = models.SlugField(unique=True, verbose_name="Слаг жанра")

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

    def __str__(self):
        return self.slug


class Title(models.Model):
    name = models.TextField(max_length=256, verbose_name="Название")
    year = models.PositiveIntegerField(
        db_index=True, verbose_name="Год", validators=(validate_year,)
    )
    description = models.TextField(blank=True, verbose_name="Описание")
    genre = models.ManyToManyField(
        Genre, through="GenreTitle", verbose_name="Жанр"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Категория",
    )

    class Meta:
        verbose_name = "Произведение"
        verbose_name_plural = "Произведения"

    def __str__(self):
        return self.name


class GenreTitle(models.Model):
    genre = models.ForeignKey(
        Genre, on_delete=models.CASCADE, verbose_name="Жанр"
    )
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE, verbose_name="Название"
    )

    def __str__(self):
        return f"{self.genre} {self.title}"


class Review(models.Model):
    """Класс Отзывы."""

    text = models.TextField(verbose_name="Информация отзыва")
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="reviews",
        verbose_name="Aвтор",
    )
    score = models.PositiveIntegerField(
        verbose_name="Oценка",
        validators=[
            MinValueValidator(1, message="Значение 1 - 10"),
            MaxValueValidator(10, message="Значение 1 - 10"),
        ],
    )
    pub_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата публикации отзыва", db_index=True
    )
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name="reviews",
        verbose_name="произведение",
        null=True,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=(
                    "title",
                    "author",
                ),
                name="unique_review",
            )
        ]

    def __str__(self):
        return self.text


class Comment(models.Model):
    """Класс Коментарии."""

    text = models.TextField(verbose_name="Информация о комментарии")
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="username автора комментария",
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата публикации комментария",
        db_index=True,
    )
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="oтзыв",
    )

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ("-pub_date",)

    def __str__(self):
        return self.text
