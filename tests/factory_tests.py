from nose.tools import *
from pydnx.factory import build_generalRepCharacteristics, build_generalIECharacteristics
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


def test_generalIECharacteristics():
	grc = build_generalIECharacteristics(submissionReason='Unpublished Donation',
		status='ACTIVE',
		IEEntityType='UnpublishedBornDigital')
	print("printing general IE Characteristics:")
	print(ET.tostring(grc, pretty_print=True))


def test_generalIECharacteristics_with_bad_values():
	print("Testing building generalIECharaceristics with incorrect values")
	try:
		grc = build_generalIECharacteristics(submissionReason="Dodgy_test", animalType="Horsey")
	except TypeError:
		grc = None
	assert(grc == None)