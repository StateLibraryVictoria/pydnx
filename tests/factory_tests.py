from nose.tools import *
from pydnx.factory import build_generalRepCharacteristics, build_generalIECharacteristics, build_generalFileCharacteristics
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

def test_generalFileCharacteristics():
	gfc = build_generalFileCharacteristics(label="Test File",
		FileEntityType="TestFile", fileSizeBytes="10092")
	print("printing general File Characteristics:")
	print(ET.tostring(gfc, pretty_print=True))


def test_generalFileCharacteristics_with_bad_values():
	print("Testing building generalFileCharacteristics with incorrect values")
	try:
		gfc = build_generalIECharacteristics(label="Dodgy_test", 
			animalType="Horsey")
	except TypeError:
		gfc = None
	assert(gfc == None)