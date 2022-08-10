import csv
import os
from pprint import pprint

from django.conf import settings
from django.core.management.base import BaseCommand
from django.shortcuts import get_object_or_404
from reviews.models import Category, Comment, Genre, Review, Title, TitleGenre
from users.models import User


class Command(BaseCommand):
    help = 'Upload sample data'

    def handle(self, *args, **options):
        path = os.path.join(settings.BASE_DIR, 'static', 'data',
                            'users.csv')
        pprint(path)
        with open(path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader, None)
            for row in reader:
                pprint(row)
                _, created = User.objects.get_or_create(
                    id=row[0],
                    username=row[1],
                    email=row[2],
                    role=row[3],
                    bio=row[4],
                    first_name=row[5],
                    last_name=row[6],
                )

        path = os.path.join(settings.BASE_DIR, 'static', 'data',
                            'genre.csv')
        pprint(path)
        with open(path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader, None)
            for row in reader:
                pprint(row)
                _, created = Genre.objects.get_or_create(
                    id=row[0],
                    name=row[1],
                    slug=row[2],
                )

        path = os.path.join(settings.BASE_DIR, 'static', 'data',
                            'category.csv')
        pprint(path)
        with open(path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader, None)
            for row in reader:
                pprint(row)
                _, created = Category.objects.get_or_create(
                    id=row[0],
                    name=row[1],
                    slug=row[2],
                )

        path = os.path.join(settings.BASE_DIR, 'static', 'data',
                            'titles.csv')
        pprint(path)
        with open(path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader, None)
            for row in reader:
                pprint(row)
                _, created = Title.objects.get_or_create(
                    id=row[0],
                    name=row[1],
                    year=row[2],
                    category=get_object_or_404(Category, id=row[3]),
                )

        path = os.path.join(settings.BASE_DIR, 'static', 'data',
                            'review.csv')
        pprint(path)
        with open(path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader, None)
            for row in reader:
                pprint(row)
                _, created = Review.objects.get_or_create(
                    id=row[0],
                    title_id=row[1],
                    text=row[2],
                    author=get_object_or_404(User, id=row[3]),  # row[3],
                    score=row[4],
                    pub_date=row[5],
                )

        path = os.path.join(settings.BASE_DIR, 'static', 'data',
                            'comments.csv')
        pprint(path)
        with open(path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader, None)
            for row in reader:
                pprint(row)
                _, created = Comment.objects.get_or_create(
                    id=row[0],
                    review=get_object_or_404(Review, id=row[1]),
                    text=row[2],
                    author=get_object_or_404(User, id=row[3]),
                    pub_date=row[4],
                )

        path = os.path.join(settings.BASE_DIR, 'static', 'data',
                            'genre_title.csv')
        pprint(path)
        with open(path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader, None)
            for row in reader:
                pprint(row)
                _, created = TitleGenre.objects.get_or_create(
                    id=row[0],
                    title=get_object_or_404(Title, id=row[1]),
                    genre=get_object_or_404(Genre, id=row[2]),
                )
