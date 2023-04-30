import csv
import os

from django.core.management import BaseCommand
from reviews.models import (Category, Comment, Genre, GenreTitle, Review,
                            Title, User)

from api_yamdb.settings import CSV_FILE_PATH

FILE_MODEL = {
    "category.csv": (Category, " "),
    "genre.csv": (Genre, ""),
    "users.csv": (User, ""),
    "titles.csv": (Title, {"category": Category}),
    "genre_title.csv": (GenreTitle, ""),
    "review.csv": (Review, {"author": User}),
    "comments.csv": (Comment, {"author": User}),
}


class Command(BaseCommand):
    help = "Load from csv file into the database"

    def handle(self, *args, **kwargs):
        # delete data from model
        print("-" * 80)
        print("### delete data from models")
        print("-" * 80)
        for _, model_args in reversed(FILE_MODEL.items()):
            if model_args[0].objects.all().exists():
                print(
                    f"Delete all objects from "
                    f"model {model_args[0].__name__}"
                )
                deleted = model_args[0].objects.all().delete()
                print(f"Deleted {deleted[0]} row(s)")

        # load data to models
        print("")
        print("-" * 80)
        print("### load data to models")
        print("-" * 80)
        for csv_file, model_args in FILE_MODEL.items():
            print(f"Model: {model_args[0].__name__}")
            file = os.path.join(CSV_FILE_PATH, csv_file)
            if os.path.exists(file):
                with open(file, "r", encoding="utf-8") as f:
                    reader = csv.reader(f, delimiter=",")
                    header = next(reader)
                    print(
                        f"Load data from {csv_file} to "
                        f"model {model_args[0].__name__}"
                    )
                    records = []
                    for row in reader:
                        # model without foreign keys
                        if not model_args[1]:
                            # print('# model without foreign keys')
                            object_dict = {
                                key: value for key, value in zip(header, row)
                            }
                            record = model_args[0](**object_dict)
                            records.append(record)

                        # model with foreign keys
                        else:
                            object_dict = {
                                key: value for key, value in zip(header, row)
                            }
                            data_args = dict(**object_dict)
                            for key, value in model_args[1].items():
                                # print(key, value)
                                data_args[key] = value.objects.get(
                                    pk=data_args[key]
                                )
                            # print(data_args)
                            record = model_args[0](**data_args)
                            records.append(record)
                        if len(records) > 5000:
                            model_args[0].objects.bulk_create(records)
                            records = []
                    if records:
                        model_args[0].objects.bulk_create(records)

                    cnt = model_args[0].objects.count()
                    print(f"Loaded: {cnt} row(s)")
                    print("-" * 40)

            else:
                print(f'File "{file}" does not exist')
