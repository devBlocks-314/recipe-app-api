from unittest.mock import patch

from django.core.management import call_command

from django.db.utils import OperationalError
from django.test import TestCase

class CommandsTestCase(TestCase):

    def test_wait_for_db_ready(self):
        """Test waiting for db when db is available"""
        """This call the handle function defined in wait_for_db.py """
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            gi.return_value = True
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 1)
    

    @patch('time.sleep', return_value=None)
    def test_wait_for_db(self, ts):
        """Test waiting for db"""
        """This call the handle function defined in wait_for_db.py """


        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            gi.side_effect = [OperationalError] * 5 + [True]
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 6)