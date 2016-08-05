from nose.tools import *
import pydnx.factory as f
from lxml import etree as ET

def setup():
    print("SETUP!")

def teardown():
    print("TEARDOWN!")

def test_basic():
    print("I RAN!")

def test_generalRepCharacteristics():
    grc = f.build_generalRepCharacteristics(preservationType='PRESERVATION_MASTER',
        usageType='VIEW',
        DigitalOriginal='True')
    print("printing general Rep Characteristics:")
    print(ET.tostring(grc, pretty_print=True))

def test_generalRepCharacteristics_with_bad_values():
    print("Testing building generalRepCharaceristics with incorrect values")
    try:
        grc = f.build_generalRepCharacteristics(label="Test Horsey", animalType="Horsey")
    except TypeError:
        grc = None
    assert(grc == None)


def test_generalIECharacteristics():
    grc = f.build_generalIECharacteristics(submissionReason='Unpublished Donation',
        status='ACTIVE',
        IEEntityType='UnpublishedBornDigital')
    print("printing general IE Characteristics:")
    print(ET.tostring(grc, pretty_print=True))


def test_generalIECharacteristics_with_bad_values():
    print("Testing building generalIECharaceristics with incorrect values")
    try:
        grc = f.build_generalIECharacteristics(submissionReason="Dodgy_test", animalType="Horsey")
    except TypeError:
        grc = None
    assert(grc == None)

def test_generalFileCharacteristics():
    gfc = f.build_generalFileCharacteristics(label="Test File",
        FileEntityType="TestFile", fileSizeBytes="10092")
    print("printing general File Characteristics:")
    print(ET.tostring(gfc, pretty_print=True))


def test_generalFileCharacteristics_with_bad_values():
    print("Testing building generalFileCharacteristics with incorrect values")
    try:
        gfc = f.build_generalIECharacteristics(label="Dodgy_test", 
            animalType="Horsey")
    except TypeError:
        gfc = None
    assert(gfc == None)


def test_objectCharacteristics():
    oc = f.build_objectCharacteristics(objectType='INTELLECTUAL_ENTITY', groupID='IEGROUP1')
    print("printing object Characteristics:")
    print(ET.tostring(oc, pretty_print=True))


def test_objectCharacteristics_with_bad_values():
    print("Testing building objectCharacteristics with incorrect values")
    try:
        oc = f.build_generalIECharacteristics(objectType="INTELLECTUAL_ENTITY", 
            animalType="Horsey")
    except TypeError:
        oc = None
    assert(oc == None)

def test_CMS():
    cms = f.build_CMS(system='ALMA', recordId='aaa1234')
    print("printing CMS details")
    print(ET.tostring(cms, pretty_print=True))

def test_CMS_with_bad_values():
    print("Testing building objectCharacteristics with incorrect values")
    try:
        cms = f.build_CMS(system='ALMA', 
            animalType="Horsey")
    except TypeError:
        cms = None
    assert(cms == None)