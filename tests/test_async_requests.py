import unittest

# SEARCH:
from kinopapi.requests.search import suggest_search_async

# FILM:
from kinopapi.requests.film import (
    film_base_info_async,
    film_similar_movies_async,
    film_trivias_async,
    film_media_posts_async,
    film_soundtracks_async,
    film_movie_lists_relations_async,
)

# MOVIE:
from kinopapi.requests.movie import (
    movie_preview_card_async,
    movie_trailers_with_order_async,
    movies_in_cinema_with_featuring_async,
    movie_users_reviews_async,
    original_movies_async,
)

# PERSON:
from kinopapi.requests.person import person_preview_card_async

# TVSERIES:
from kinopapi.requests.tvseries import (
    tvseries_base_info_async,
    tvseries_similar_movies_async,
    tvseries_episodes_async,
    tvseries_trivias_async,
    tvseries_soundtracks_async,
    tvseries_media_posts_async,
    tvseries_movie_lists_relations_async,
    tvseries_critic_reviews_async,
)


class TestKinopapiAsync(unittest.IsolatedAsyncioTestCase):

    async def test_suggest_search_async(self):
        response = await suggest_search_async("во все тяжкие")
        self.assertEqual(response.status, 200)
        json_data = await response.json()
        self.assertIsInstance(json_data, dict)

    async def test_film_base_info_async(self):
        response = await film_base_info_async(1209193)
        self.assertEqual(response.status, 200)
        json_data = await response.json()
        self.assertIsInstance(json_data, dict)

    async def test_film_similar_movies_async(self):
        response = await film_similar_movies_async(1209193)
        self.assertEqual(response.status, 200)
        json_data = await response.json()
        self.assertIsInstance(json_data, dict)

    async def test_film_trivias_async(self):
        response = await film_trivias_async(1209193)
        self.assertEqual(response.status, 200)
        json_data = await response.json()
        self.assertIsInstance(json_data, dict)

    async def test_film_media_posts_async(self):
        response = await film_media_posts_async(1209193)
        self.assertEqual(response.status, 200)
        json_data = await response.json()
        self.assertIsInstance(json_data, dict)

    async def test_film_soundtracks_async(self):
        response = await film_soundtracks_async(1209193)
        self.assertEqual(response.status, 200)
        json_data = await response.json()
        self.assertIsInstance(json_data, dict)

    async def test_film_movie_lists_relations_async(self):
        response = await film_movie_lists_relations_async(1209193)
        self.assertEqual(response.status, 200)
        json_data = await response.json()
        self.assertIsInstance(json_data, dict)

    async def test_movie_preview_card_async(self):
        response = await movie_preview_card_async(404900)
        self.assertEqual(response.status, 200)
        json_data = await response.json()
        self.assertIsInstance(json_data, dict)

    async def test_movie_trailers_with_order_async(self):
        response = await movie_trailers_with_order_async(404900)
        self.assertEqual(response.status, 200)
        json_data = await response.json()
        self.assertIsInstance(json_data, dict)

    async def test_movies_in_cinema_with_featuring_async(self):
        response = await movies_in_cinema_with_featuring_async(1)
        self.assertEqual(response.status, 200)
        json_data = await response.json()
        self.assertIsInstance(json_data, dict)

    async def test_movie_users_reviews_async(self):
        response = await movie_users_reviews_async(404900)
        self.assertEqual(response.status, 200)
        json_data = await response.json()
        self.assertIsInstance(json_data, dict)

    async def test_original_movies_async(self):
        response = await original_movies_async(404900)
        self.assertEqual(response.status, 200)
        json_data = await response.json()
        self.assertIsInstance(json_data, dict)

    async def test_person_preview_card_async(self):
        response = await person_preview_card_async(3556)
        self.assertEqual(response.status, 200)
        json_data = await response.json()
        self.assertIsInstance(json_data, dict)

    async def test_tvseries_base_info_async(self):
        response = await tvseries_base_info_async(404900)
        self.assertEqual(response.status, 200)
        json_data = await response.json()
        self.assertIsInstance(json_data, dict)

    async def test_tvseries_similar_movies_async(self):
        response = await tvseries_similar_movies_async(404900)
        self.assertEqual(response.status, 200)
        json_data = await response.json()
        self.assertIsInstance(json_data, dict)

    async def test_tvseries_episodes_async(self):
        response = await tvseries_episodes_async(404900)
        self.assertEqual(response.status, 200)
        json_data = await response.json()
        self.assertIsInstance(json_data, dict)

    async def test_tvseries_trivias_async(self):
        response = await tvseries_trivias_async(404900)
        self.assertEqual(response.status, 200)
        json_data = await response.json()
        self.assertIsInstance(json_data, dict)

    async def test_tvseries_soundtracks_async(self):
        response = await tvseries_soundtracks_async(404900)
        self.assertEqual(response.status, 200)
        json_data = await response.json()
        self.assertIsInstance(json_data, dict)

    async def test_tvseries_media_posts_async(self):
        response = await tvseries_media_posts_async(404900)
        self.assertEqual(response.status, 200)
        json_data = await response.json()
        self.assertIsInstance(json_data, dict)

    async def test_tvseries_movie_lists_relations_async(self):
        response = await tvseries_movie_lists_relations_async(404900)
        self.assertEqual(response.status, 200)
        json_data = await response.json()
        self.assertIsInstance(json_data, dict)

    async def test_tvseries_critic_reviews_async(self):
        response = await tvseries_critic_reviews_async(404900)
        self.assertEqual(response.status, 200)
        json_data = await response.json()
        self.assertIsInstance(json_data, dict)
