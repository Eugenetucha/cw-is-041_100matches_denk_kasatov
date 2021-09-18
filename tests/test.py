import unittest
from importlib import reload
import src.game_starting
import pygame
import src.main


class PygameMainWindowTest(unittest.TestCase):
    def setUp(self):
        reload(src.game_starting)
        pygame.init()

    def tearDown(self):
        pygame.quit()

    def test_switch_to_next_player_one(self):
        src.game_starting.switch_to_next_player()
        self.assertEqual(src.game_starting.current_player, "2")

    def test_switch_to_next_player_two(self):
        src.game_starting.switch_to_next_player()
        self.assertNotEqual(src.game_starting.current_player, "1")

    def test_switch_to_next_player_three(self):
        src.game_starting.switch_to_next_player()
        self.assertNotEqual(src.game_starting.current_player, "3")

    def test_quit(self):
        pygame.quit()
        self.assertFalse(pygame.display.get_init())


class PygameTopWindowTest(unittest.TestCase):
    def setUp(self):
        reload(src.main)
        pygame.init()

    def tearDown(self):
        pygame.quit()

    def test_quit(self):
        pygame.quit()
        self.assertFalse(pygame.display.get_init())

    def test_list_crnt_one(self):
        src.main.list_crnt()
        self.assertEqual(src.main.list_crnt(), None)

    def test_list_crnt_two(self):
        src.main.list_crnt()
        self.assertNotEqual(src.main.list_crnt(), 1)

    def test_list_crnt_three(self):
        src.main.list_crnt()
        self.assertNotEqual(src.main.list_crnt(), 2)


if __name__ == '__main__':
    unittest.main()
