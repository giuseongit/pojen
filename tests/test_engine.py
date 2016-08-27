from unittest import TestCase
from pojen import engine

class EngineTestCase(TestCase):
    def test_can_parse_int(self):
        self.assertEquals(engine.can_parse_int("1"), True)
        self.assertEquals(engine.can_parse_int("no"), False)

    def test_can_parse_float(self):
        self.assertEquals(engine.can_parse_float("1.0"), True)
        self.assertEquals(engine.can_parse_float("no"), False)

    def test_can_infer_type(self):
        self.assertEquals(engine.infer_type("true"), bool)
        self.assertEquals(engine.infer_type("1"), int)
        self.assertEquals(engine.infer_type(1), int)
        self.assertEquals(engine.infer_type("1.0"), float)
        self.assertEquals(engine.infer_type(1.0), float)
        self.assertEquals(engine.infer_type("hello"), str)

    def test_prepare_structure(self):
        example = {
            "keyone": [2,3,1],
            "keytwo": "valone",
            "keythree": 4,
            "keyfour": {
                "subkeyone": "subvalone",
                "subkeytwo": {
                    "nested": "0.3"
                }
            }
        }

        example2 = {
            "keyone": {
                "subkeyone": "subvalone",
                "subkeytwo": {
                    "nested": "0.3"
                }
            }
        }

        dt = engine.prepare_structure(example, "top")
        dt2 = engine.prepare_structure(example2)

        expected_result = [
            ('top', {'keyone': 'ArrayList<Integer>', 'keytwo': 'String', 'keyfour': 'Keyfour', 'keythree': 'int'}, ["java.util.ArrayList"]),
            ('keyfour', {'subkeyone': 'String', 'subkeytwo': 'Subkeytwo'}, []),
            ('subkeytwo', {'nested': 'float'}, [])
        ]

        expected_result2 = [
            ('keyone', {'subkeyone': 'String', 'subkeytwo': 'Subkeytwo'}, []),
            ('subkeytwo', {'nested': 'float'}, [])
        ]

        self.assertEquals(dt2, expected_result2)
        self.assertEquals(dt, expected_result)
