from rest_framework import serializers

from reviews.models import Category, Comment, Genre, Review, Title, User
from reviews.validators import validate_username


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "bio",
            "first_name",
            "last_name",
            "email",
            "role",
        )


class NotAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "bio",
            "role",
        )
        read_only_fields = ("role",)


class GetTokenSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    confirmation_code = serializers.CharField(required=True)


class SignUpSerializer(serializers.Serializer):
    email = serializers.EmailField(
        required=True,
        max_length=254,
    )
    username = serializers.CharField(
        required=True, validators=[validate_username], max_length=150
    )


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("name", "slug")
        lookup_field = "slug"


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("name", "slug")
        lookup_field = "slug"


class TitlesWriteSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        queryset=Genre.objects.all(), slug_field="slug", many=True
    )
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(), slug_field="slug"
    )

    class Meta:
        model = Title
        fields = ("id", "name", "year", "description", "genre", "category")


class TitlesReadSerializer(serializers.ModelSerializer):
    rating = serializers.IntegerField(read_only=True)
    genre = GenreSerializer(many=True, read_only=True)
    category = CategoriesSerializer(read_only=True)

    class Meta:
        model = Title
        fields = (
            "id",
            "name",
            "year",
            "rating",
            "description",
            "genre",
            "category",
        )


class ReviewSerializer(serializers.ModelSerializer):
    """Сериализатор отзывов"""

    author = serializers.SlugRelatedField(
        slug_field="username", read_only=True
    )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["author"] = UsersSerializer(instance.author).data[
            "username"
        ]
        return representation

    class Meta:
        model = Review
        fields = ("id", "title", "author", "text", "score", "pub_date")
        read_only_fields = ("title", "author", "pub_date")

    def validate(self, attrs):
        review_obj_exists = Review.objects.filter(
            author=self.context.get("request").user,
            title=self.context.get("view").kwargs.get("title_id"),
        ).exists()
        if review_obj_exists and self.context.get("request").method == "POST":
            raise serializers.ValidationError("Вы уже оставляли отзыв")
        return attrs


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор комментариев"""

    author = serializers.SlugRelatedField(
        slug_field="username", read_only=True
    )
    review = serializers.SlugRelatedField(slug_field="text", read_only=True)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["author"] = UsersSerializer(instance.author).data[
            "username"
        ]
        return representation

    class Meta:
        model = Comment
        fields = ("id", "review", "author", "text", "pub_date")
        read_only_fields = ("review", "author", "pub_date")
