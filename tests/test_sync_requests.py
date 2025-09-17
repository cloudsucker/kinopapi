import unittest

# SEARCH
from kinopapi.requests.search import suggest_search

# FILM
from kinopapi.requests.film import (
    film_base_info,
    film_similar_movies,
    film_trivias,
    film_media_posts,
    film_soundtracks,
    film_movie_lists_relations,
)

# MOVIE
from kinopapi.requests.movie import (
    movie_preview_card,
    movie_trailers_with_order,
    movies_in_cinema_with_featuring,
    movie_users_reviews,
    original_movies,
)

# PERSON
from kinopapi.requests.person import person_preview_card

# TVSERIES
from kinopapi.requests.tvseries import (
    tvseries_base_info,
    tvseries_similar_movies,
    tvseries_episodes,
    tvseries_trivias,
    tvseries_soundtracks,
    tvseries_media_posts,
    tvseries_movie_lists_relations,
    tvseries_critic_reviews,
)


class TestKinopapiSync(unittest.TestCase):

    def test_suggest_search(self):
        response = suggest_search("во все тяжкие")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)

    def test_film_base_info(self):
        response = film_base_info(1209193)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)

    def test_film_similar_movies(self):
        response = film_similar_movies(1209193)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)

    def test_film_trivias(self):
        response = film_trivias(1209193)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)

    def test_film_media_posts(self):
        response = film_media_posts(1209193)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)

    def test_film_soundtracks(self):
        response = film_soundtracks(1209193)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)

    def test_film_movie_lists_relations(self):
        response = film_movie_lists_relations(1209193)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)

    def test_movie_preview_card(self):
        response = movie_preview_card(404900)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)

    def test_movie_trailers_with_order(self):
        response = movie_trailers_with_order(404900)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)

    def test_movies_in_cinema_with_featuring(self):
        response = movies_in_cinema_with_featuring(1)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)

    def test_movie_users_reviews(self):
        response = movie_users_reviews(404900)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)

    def test_original_movies(self):
        response = original_movies(404900)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)

    def test_person_preview_card(self):
        response = person_preview_card(3556)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)

    def test_tvseries_base_info(self):
        response = tvseries_base_info(404900)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)

    def test_tvseries_similar_movies(self):
        response = tvseries_similar_movies(404900)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)

    def test_tvseries_episodes(self):
        response = tvseries_episodes(404900)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)

    def test_tvseries_trivias(self):
        response = tvseries_trivias(404900)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)

    def test_tvseries_soundtracks(self):
        response = tvseries_soundtracks(404900)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)

    def test_tvseries_media_posts(self):
        response = tvseries_media_posts(404900)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)

    def test_tvseries_movie_lists_relations(self):
        response = tvseries_movie_lists_relations(404900)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)

    def test_tvseries_critic_reviews(self):
        response = tvseries_critic_reviews(404900)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)
