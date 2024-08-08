from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='test@gmail.com')
        self.habit = Habit.objects.create(place='парк', time='2024-08-24T08:00:00', action='приседания',
                                          is_pleasant=False, frequency_number=1, frequency_unit='days',
                                          reward='съесть яблоко', duration='120', is_public=True,
                                          user=self.user)
        self.client.force_authenticate(user=self.user)

    def test_habit_retrieve(self):
        url = reverse("habits:habits-detail", args=(self.habit.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(
            data.get('action'), self.habit.action
        )

    def test_habit_create(self):
        url = reverse("habits:habits-list")
        data = {
            "place": "дом",
            "time": "2024-07-24T20:40:00",
            "action": "протереть пыль",
            "is_pleasant": False,
            "frequency_number": 1,
            "frequency_unit": "days",
            "reward": "посмотреть фильм",
            "duration": "00:02:00",
            "is_public": True,
            "user": 1,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            Habit.objects.all().count(), 2
        )

    def test_habit_list(self):
        url = reverse("habits:habits-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_habit_update(self):
        url = reverse("habits:habits-detail", args=(self.habit.pk,))
        data = {
            'reward': 'посмотреть фильм',
        }
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            data.get('reward'), 'посмотреть фильм'
        )

    def test_habit_delete(self):
        url = reverse("habits:habits-detail", args=(self.habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(
            Habit.objects.all().count(), 0
        )
