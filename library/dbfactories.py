import factory
import factory.django
from factory.fuzzy import FuzzyInteger, FuzzyDate
import datetime
from .models import Books, Author, Publisher

class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Author
    
    firstname = factory.Faker('first_name')
    lastname = factory.Faker('last_name')
    dob = FuzzyDate(datetime.date(2000, 1, 1))
    fullname = factory.LazyAttribute(lambda p: '{} {}'.format(p.firstname, p.lastname))

class PublisherFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Publisher

    name = factory.Faker('company')
    city = factory.Faker('city')
    country = factory.Faker('country')

class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Books

    book_id = factory.Faker('pystr', max_chars=9)
    title = factory.Faker('bs')
    author = factory.SubFactory(AuthorFactory)
    isbn = FuzzyInteger(1000000000, 9999999999)
    publisher = factory.SubFactory(PublisherFactory)
