from hstest.stage_test import *
from hstest.test_case import TestCase
import re


class EasyRiderStage6(StageTest):
    def generate(self) -> List[TestCase]:
        return [

            TestCase(stdin='[{"bus_id" : 128, "stop_id" : 1, "stop_name" : "Prospekt Avenue", "next_stop" : 3, "stop_type" : "S", "a_time" : "08:12"}, '
                           '{"bus_id" : 128, "stop_id" : 3, "stop_name" : "Elm Street", "next_stop" : 5, "stop_type" : "O", "a_time" : "08:19"}, '
                           '{"bus_id" : 128, "stop_id" : 5, "stop_name" : "Fifth Avenue", "next_stop" : 7, "stop_type" : "O", "a_time" : "08:25"}, '
                           '{"bus_id" : 128, "stop_id" : 7, "stop_name" : "Sesame Street", "next_stop" : 0, "stop_type" : "F", "a_time" : "08:37"}, '
                           '{"bus_id" : 256, "stop_id" : 2, "stop_name" : "Pilotow Street", "next_stop" : 3, "stop_type" : "S", "a_time" : "09:20"}, '
                           '{"bus_id" : 256, "stop_id" : 3, "stop_name" : "Elm Street", "next_stop" : 6, "stop_type" : "", "a_time" : "09:45"}, '
                           '{"bus_id" : 256, "stop_id" : 6, "stop_name" : "Abbey Road", "next_stop" : 7, "stop_type" : "O", "a_time" : "09:59"}, '
                           '{"bus_id" : 256, "stop_id" : 7, "stop_name" : "Sesame Street", "next_stop" : 0, "stop_type" : "F", "a_time" : "10:12"}, '
                           '{"bus_id" : 512, "stop_id" : 4, "stop_name" : "Bourbon Street", "next_stop" : 6, "stop_type" : "S", "a_time" : "08:13"}, '
                           '{"bus_id" : 512, "stop_id" : 6, "stop_name" : "Abbey Road", "next_stop" : 0, "stop_type" : "F", "a_time" : "08:16"}]',
                     attach=('Abbey Road', 'Elm Street')),
            TestCase(stdin='[{"bus_id" : 128, "stop_id" : 1, "stop_name" : "Fifth Avenue", "next_stop" : 4, "stop_type" : "S", "a_time" : "08:12"}, '
                           '{"bus_id" : 128, "stop_id" : 4, "stop_name" : "Abbey Road", "next_stop" : 5, "stop_type" : "", "a_time" : "08:19"},  '
                           '{"bus_id" : 128, "stop_id" : 5, "stop_name" : "Santa Monica Boulevard", "next_stop" : 8, "stop_type" : "O", "a_time" : "08:25"},  '
                           '{"bus_id" : 128, "stop_id" : 8, "stop_name" : "Elm Street", "next_stop" : 11, "stop_type" : "", "a_time" : "08:37"},  '
                           '{"bus_id" : 128, "stop_id" : 11, "stop_name" : "Beale Street", "next_stop" : 12, "stop_type" : "", "a_time" : "09:20"},  '
                           '{"bus_id" : 128, "stop_id" : 12, "stop_name" : "Sesame Street", "next_stop" : 14, "stop_type" : "", "a_time" : "09:45"},  '
                           '{"bus_id" : 128, "stop_id" : 14, "stop_name" : "Bourbon Street", "next_stop" : 19, "stop_type" : "O", "a_time" : "09:59"},  '
                           '{"bus_id" : 128, "stop_id" : 19, "stop_name" : "Prospekt Avenue", "next_stop" : 0, "stop_type" : "F", "a_time" : "10:12"},  '
                           '{"bus_id" : 256, "stop_id" : 2, "stop_name" : "Pilotow Street", "next_stop" : 3, "stop_type" : "S", "a_time" : "08:13"},  '
                           '{"bus_id" : 256, "stop_id" : 3, "stop_name" : "Startowa Street", "next_stop" : 8, "stop_type" : "", "a_time" : "08:16"},  '
                           '{"bus_id" : 256, "stop_id" : 8, "stop_name" : "Elm Street", "next_stop" : 10, "stop_type" : "", "a_time" : "08:29"},  '
                           '{"bus_id" : 256, "stop_id" : 10, "stop_name" : "Lombard Street", "next_stop" : 12, "stop_type" : "", "a_time" : "08:44"},  '
                           '{"bus_id" : 256, "stop_id" : 12, "stop_name" : "Sesame Street", "next_stop" : 13, "stop_type" : "O", "a_time" : "08:46"},  '
                           '{"bus_id" : 256, "stop_id" : 13, "stop_name" : "Orchard Road", "next_stop" : 16, "stop_type" : "", "a_time" : "09:13"},  '
                           '{"bus_id" : 256, "stop_id" : 16, "stop_name" : "Sunset Boulevard", "next_stop" : 17, "stop_type" : "O", "a_time" : "09:26"},  '
                           '{"bus_id" : 256, "stop_id" : 17, "stop_name" : "Khao San Road", "next_stop" : 20, "stop_type" : "O", "a_time" : "10:25"},  '
                           '{"bus_id" : 256, "stop_id" : 20, "stop_name" : "Michigan Avenue", "next_stop" : 0, "stop_type" : "F", "a_time" : "11:26"},  '
                           '{"bus_id" : 512, "stop_id" : 6, "stop_name" : "Arlington Road", "next_stop" : 7, "stop_type" : "S", "a_time" : "11:06"},  '
                           '{"bus_id" : 512, "stop_id" : 7, "stop_name" : "Parizska Street", "next_stop" : 8, "stop_type" : "", "a_time" : "11:15"},  '
                           '{"bus_id" : 512, "stop_id" : 8, "stop_name" : "Elm Street", "next_stop" : 9, "stop_type" : "", "a_time" : "11:56"},  '
                           '{"bus_id" : 512, "stop_id" : 9, "stop_name" : "Niebajka Avenue", "next_stop" : 15, "stop_type" : "", "a_time" : "12:20"},  '
                           '{"bus_id" : 512, "stop_id" : 15, "stop_name" : "Jakis Street", "next_stop" : 16, "stop_type" : "", "a_time" : "12:44"},  '
                           '{"bus_id" : 512, "stop_id" : 16, "stop_name" : "Sunset Boulevard", "next_stop" : 18, "stop_type" : "", "a_time" : "13:01"},  '
                           '{"bus_id" : 512, "stop_id" : 18, "stop_name" : "Jakas Avenue", "next_stop" : 19, "stop_type" : "", "a_time" : "14:00"},  '
                           '{"bus_id" : 1024, "stop_id" : 21, "stop_name" : "Karlikowska Avenue", "next_stop" : 12, "stop_type" : "S", "a_time" : "13:01"},  '
                           '{"bus_id" : 1024, "stop_id" : 12, "stop_name" : "Sesame Street", "next_stop" : 0, "stop_type" : "F", "a_time" : "14:00"},  '
                           '{"bus_id" : 512, "stop_id" : 19, "stop_name" : "Prospekt Avenue", "next_stop" : 0, "stop_type" : "F", "a_time" : "14:11"}]',
                     attach=('Sesame Street', 'Sunset Boulevard')),
            TestCase(stdin='[{"bus_id" : 128, "stop_id" : 1, "stop_name" : "Prospekt Avenue", "next_stop" : 3, "stop_type" : "S", "a_time" : "08:12"}, '
                           '{"bus_id" : 128, "stop_id" : 3, "stop_name" : "Elm Street", "next_stop" : 5, "stop_type" : "", "a_time" : "08:19"}, '
                           '{"bus_id" : 128, "stop_id" : 5, "stop_name" : "Fifth Avenue", "next_stop" : 7, "stop_type" : "O", "a_time" : "08:25"}, '
                           '{"bus_id" : 128, "stop_id" : 7, "stop_name" : "Sesame Street", "next_stop" : 0, "stop_type" : "F", "a_time" : "08:37"}, '
                           '{"bus_id" : 256, "stop_id" : 2, "stop_name" : "Pilotow Street", "next_stop" : 3, "stop_type" : "S", "a_time" : "09:20"}, '
                           '{"bus_id" : 256, "stop_id" : 3, "stop_name" : "Elm Street", "next_stop" : 6, "stop_type" : "", "a_time" : "09:45"}, '
                           '{"bus_id" : 256, "stop_id" : 6, "stop_name" : "Sunset Boulevard", "next_stop" : 7, "stop_type" : "", "a_time" : "09:59"}, '
                           '{"bus_id" : 256, "stop_id" : 7, "stop_name" : "Sesame Street", "next_stop" : 0, "stop_type" : "F", "a_time" : "10:12"}, '
                           '{"bus_id" : 512, "stop_id" : 4, "stop_name" : "Bourbon Street", "next_stop" : 6, "stop_type" : "S", "a_time" : "08:13"}, '
                           '{"bus_id" : 512, "stop_id" : 6, "stop_name" : "Sunset Boulevard", "next_stop" : 0, "stop_type" : "F", "a_time" : "08:16"}]',
                     attach="OK"),
        ]

    def check(self, reply: str, result) -> CheckResult:
        if isinstance(result, str):
            if result not in reply:
                return CheckResult.wrong(f"Wrong number of bugs detected or the output format is wrong. "
                                         "Expected output:\n\n"
                                         "On demand stops test:\n"
                                         f"Wrong stop type: {result}")
        else:
            query = rf"['{result[0]}[\W]+{result[1]}']"
            if not re.search(rf'{query}', reply):
                return CheckResult.wrong(f"Wrong number of bugs detected or the output format is wrong. "
                                         "Expected output:\n\n" 
                                         "On demand stops test:\n"
                                         f"Wrong stop type: {list(result)}")
        return CheckResult.correct()


if __name__ == '__main__':
    EasyRiderStage6('easyrider.easyrider').run_tests()
