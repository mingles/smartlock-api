import unittest
import json

from Project.tests.base_test import BaseTest

__author__ = 'Sam Davies'


class LockListTestCase(BaseTest):
    def test_filter_by_lock_id(self):
        """ Ensure that a list of users can be filtered by the lock id """
        # Given
        self.register_user(username="tester@mail.com", password="python")
        self.register_user(username="user1@mail.com", password="python")
        self.app.post(
            '/lock',
            headers=self.auth_header("tester@mail.com", "python"),
            data=dict(lock_id=123, lock_name="123")
        )

        # When
        response = self.app.get(
            '/user',
            headers=self.auth_header("tester@mail.com", "python"),
            query_string={"lock_id": 123}
        )

        # Then
        self.assertEqual(200, response.status_code)
        users = json.loads(response.data)
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0]["email"], "tester@mail.com")


if __name__ == '__main__':
    unittest.main()
