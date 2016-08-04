from nose.tools import *
from pydnx.factory import build_generalRepCharacteristics
from lxml import etree as ET

def setup():
    print("SETUP!")

def teardown():
    print("TEARDOWN!")

def test_basic():
    print("I RAN!")

def test_generalRepCharacteristics():
	grc = build_generalRepCharacteristics(preservationType='PRESERVATION_MASTER',
		usageType='VIEW',
		DigitalOriginal='True')
	print("printing general Rep Characteristics:")
	print(ET.tostring(grc, pretty_print=True))

def test_generalRepCharacteristics_with_bad_values():
	print("Testing building generalRepCharaceristics with incorrect values")
	try:
		grc = build_generalRepCharacteristics(label="Test Horsey", animalType="Horsey")
	except TypeError:
		grc = None
	assert(grc == None)
