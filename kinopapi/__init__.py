# FILM
from kinopapi.requests.film import (
    film_base_info,
    film_base_info_async,
    film_similar_movies,
    film_similar_movies_async,
    film_trivias,
    film_trivias_async,
    film_media_posts,
    film_media_posts_async,
    film_soundtracks,
    film_soundtracks_async,
    film_movie_lists_relations,
    film_movie_lists_relations_async,
)

# MOVIES
from kinopapi.requests.movie import (
    movie_preview_card,
    movie_preview_card_async,
    movie_trailers_with_order,
    movie_trailers_with_order_async,
    movies_in_cinema_with_featuring,
    movies_in_cinema_with_featuring_async,
    movie_users_reviews,
    movie_users_reviews_async,
    original_movies,
    original_movies_async,
)

# PERSON
from kinopapi.requests.person import person_preview_card, person_preview_card_async

# SEARCH
from kinopapi.requests.search import suggest_search, suggest_search_async

# TVSERIES
from kinopapi.requests.tvseries import (
    tvseries_trivias,
    tvseries_trivias_async,
    tvseries_similar_movies,
    tvseries_similar_movies_async,
    tvseries_episodes,
    tvseries_episodes_async,
    tvseries_base_info,
    tvseries_base_info_async,
    tvseries_soundtracks,
    tvseries_soundtracks_async,
    tvseries_media_posts,
    tvseries_media_posts_async,
    tvseries_movie_lists_relations,
    tvseries_movie_lists_relations_async,
)
