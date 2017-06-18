from django.test import TestCase
import mock
from .models import *
import unittest

# Create your tests here.

def myfilter(*k, **args):
    class Temp():
        def all(self):
            x1 = Collectpoint_type(typename=0, remark='haha')
            x2 = Collectpoint_type(typename=1, remark='tttt')
            return [x1, x2]
    return Temp()

    
class SampleTests(unittest.TestCase):

    #@mock.patch('cloub.models.Collectpoint_type.objects.filter', myfilter)
    @mock.patch('cloub.tests.Collectpoint_type.objects.filter', myfilter)
    def test(self):
        x = Collectpoint_type.objects.filter().all()
        self.assertEquals(len(x), 2)
        


