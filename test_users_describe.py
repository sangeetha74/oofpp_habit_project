from unittest import TestCase

class Test(TestCase):
    def test_users_table_description(self):
        from users_describe import users_table_description
        self.assertEqual(users_table_description("test.db"),1)

    def test_habit_table_description(self):
        from describe_habit_table import habit_table_description
        self.assertEqual(habit_table_description("test.db"), 1)

    def test_habit_completion_table_description(self):
        from describe_habit_completion_table import habit_completion_table_description
        self.assertEqual(habit_completion_table_description("test.db"), 1)