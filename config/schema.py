import strawberry
import typing


@strawberry.type
class Movie:
    pk: int
    title: str
    year: int
    rating: int


movies_db = [
    Movie(pk=1, title="Godfather", year=1990, rating=10),
    Movie(pk=2, title="ToyStory", year=2000, rating=10),
]


def movies():
    return movies_db


def movie(movie_pk: int):
    return movies_db[movie_pk - 1]


@strawberry.type
class Query:
    # @strawberry.field
    # def movies(self) -> typing.List[Movie]:
    #     return movies_db

    # @strawberry.field
    # def movie(self, movie_pk: int) -> Movie:
    #     return movies_db[movie_pk - 1]
    movies: typing.List[Movie] = strawberry.field(resolver=movies)
    movie: Movie = strawberry.field(resolver=movie)


def add_movie(title: str, year: int, rating: int):
    movies_db.append(
        Movie(
            pk=len(movies_db) + 1,
            title=title,
            year=year,
            rating=rating,
        )
    )
    return movies_db[-1]


@strawberry.type
class Mutation:
    # @strawberry.mutation
    # def add_movie(self, title: str, year: int, rating: int) -> Movie:
    #     movies_db.append(
    #         Movie(
    #             pk=len(movies_db) + 1,
    #             title=title,
    #             year=year,
    #             rating=rating,
    #         )
    #     )
    #     return movies_db[-1]
    add_movie: Movie = strawberry.mutation(resolver=add_movie)


schema = strawberry.Schema(
    query=Query,
    mutation=Mutation,
)
