import os
import sys
import unittest
from day12_navigation_state import NavigationState, Point, Direction
from day12_instruction_library import build_instructions_from_file, execute_instructions
from day12_part02 import part02_instruction_factory


class TestDay12Part02(unittest.TestCase):
    def test_part01(self):
        # Arrange
        file_path = os.path.join(sys.path[0], "input_sample01.txt")
        initial_waypoint_offset = Point(10, -1)
        instructions = build_instructions_from_file(file_path, part02_instruction_factory)
        initial_nav_state = NavigationState(Point(0, 0), Direction.East, initial_waypoint_offset)

        # Act
        final_nav_state = execute_instructions(initial_nav_state, instructions)
        total_distance = final_nav_state.location.manhatten_distance_from(initial_nav_state.location)

        # Assert
        self.assertEqual(total_distance, 286)


if __name__ == '__main__':
    unittest.main()
