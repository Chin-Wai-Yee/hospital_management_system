import unittest
from datetime import datetime
from Patient import SickRecord

class TestSickRecord(unittest.TestCase):
    def test_constructor(self):
        record = SickRecord()
        self.assertEqual(record.name, "")
        self.assertIsInstance(record.date, datetime)
        self.assertEqual(record.treatment, "")
        self.assertEqual(record.doctor, "")

    def test_setName(self):
        record = SickRecord()
        record.setName("John Doe")
        self.assertEqual(record.name, "John Doe")

    def test_setDate(self):
        record = SickRecord()
        record.setDate("2022-01-01")
        self.assertEqual(record.date, datetime(2022, 1, 1))
        self.assertFalse(record.setDate("2022-13-01"))  # Invalid date format

    def test_setTreatment(self):
        record = SickRecord()
        record.setTreatment("Fever")
        self.assertEqual(record.treatment, "Fever")
        self.assertFalse(record.setTreatment(""))  # Empty treatment

    def test_setDoctor(self):
        record = SickRecord()
        record.setDoctor("Dr. Smith")
        self.assertEqual(record.doctor, "Dr. Smith")
        self.assertFalse(record.setDoctor(""))  # Empty doctor name

    def test_toString(self):
        record = SickRecord("John Doe", datetime(2022, 1, 1), "Fever", "Dr. Smith")
        expected_output = "John Doe (2022-01-01)\nFever by Dr. Dr. Smith"
        self.assertEqual(str(record), expected_output)

if __name__ == "__main__":
    unittest.main()