from nose.tools import *
import pydnx.factory as f
from lxml import etree as ET


def generic_good_values(builder_function, **kwargs):
    print("testing correct values for {}".format(builder_function.__name__))
    item = builder_function(**kwargs)
    print("printing details for {}".format(item.tag))
    print(ET.tostring(item, pretty_print=True))

def generic_bad_values(builder_function, **kwargs):
    print("Testing incorrect values for {}".format(builder_function.__name__))
    try:
        item = builder_function(**kwargs)
    except TypeError:
        item = None
    assert(item == None)

def generic_multi_record_good_values(builder_function, *args):
    print("testing correct values for {}".format(builder_function.__name__))
    item = builder_function(*args)
    print("printing details for {}".format(item.tag))
    print(ET.tostring(item, pretty_print=True))

def generic_multi_record_bad_values(builder_function, *args):
    print("testing incorrect values for {}".format(builder_function.__name__))
    try:
        item = builder_function(*args)
    except ValueError:
        item = None
    assert(item == None)

def setup():
    print("SETUP!")

def teardown():
    print("TEARDOWN!")

def test_basic():
    print("I RAN!")

def test_generalRepCharacteristics():
    generic_good_values(f.build_generalRepCharacteristics,
        preservationType='PRESERVATION_MASTER',
        usageType='VIEW',
        DigitalOriginal='True')

def test_generalRepCharacteristics_with_bad_values():
    generic_bad_values(f.build_generalRepCharacteristics,label="Test Horsey",
        animalType="Horsey")

def test_generalIECharacteristics():
    generic_good_values(f.build_generalIECharacteristics,
        submissionReason='Unpublished Donation',
        status='ACTIVE',
        IEEntityType='UnpublishedBornDigital')

def test_generalIECharacteristics_with_bad_values():
    generic_bad_values(f.build_generalIECharacteristics,
        submissionReason="Dodgy_test", animalType="Horsey")

def test_generalFileCharacteristics():
    generic_good_values(f.build_generalFileCharacteristics, label="Test File",
        FileEntityType="TestFile", fileSizeBytes="10092")

def test_generalFileCharacteristics_with_bad_values():
    generic_bad_values(f.build_generalFileCharacteristics, label="Dodgy_test",
            animalType="Horsey")

def test_objectCharacteristics():
    generic_good_values(f.build_objectCharacteristics, 
        objectType='INTELLECTUAL_ENTITY', groupID='IEGROUP1') 

def test_objectCharacteristics_with_bad_values():
    generic_bad_values(f.build_generalIECharacteristics, 
        objectType="INTELLECTUAL_ENTITY", 
        animalType="Horsey")

def test_cms():
    generic_good_values(f.build_cms, system='EMu', recordId='11121')

def test_cms_with_bad_values():
    generic_bad_values(f.build_cms, system='EMu', animal='Horsey!')

def test_webHarvesting():
    generic_good_values(f.build_webHarvesting, 
        primarySeedURL='http://www.cheese.co.nz/index.html', 
        targetName='http://www.cheese.com',
        harvestDate='2016-08-01', harvestTime='15:44:02')

def test_webHarvesting_with_bad_values():
    generic_bad_values(f.build_webHarvesting,
        primarySeedURL='http://www.cheese.co.nz/index.html',
        animal='Horsey!')

def test_objectIdentifier():
    generic_good_values(f.build_objectIdentifier, objectIdentifierType='RecordID',
        objectIdentifierValue='P8881')

def test_objectIdentifier_with_bad_values():
    generic_bad_values(f.build_objectIdentifier, objectIdentifierType='RecordID',
        favouriteVehicle='Tractor')

def test_preservationLevel():
    generic_good_values(f.build_preservationLevel, 
        preservationLevelValue='Preservation Master', 
        preservationLevelRationale='Born Digital record to be retained as National Archives',
        preservationLevelDateAssigned='2016-08-01')

def test_preservationLevel_with_bad_values():
    generic_bad_values(f.build_preservationLevel, 
        preservationLevelValue='Preservation Master', 
        preservationLevelRationale='Born Digital record to be retained as National Archives',
        preservationLevelDateAssigned='2016-08-01',
        animal="Horsey-worsey")

def test_significantProperties():
    generic_multi_record_good_values(f.build_significantProperties,
        {'significantPropertiesType': 'image.maxSampleValue',
         'significantPropertiesValue': '[1]'},
        {'significantPropertiesType': 'image.minSampleValue',
         'significantPropertiesValue': '[0]'})

def test_significantProperties_with_bad_values():
    generic_multi_record_bad_values(f.build_significantProperties, 
        {'significantPropertiesType': 'image.maxSampleValue',
             'significantPropertiesValue': '[1]'},
            {'significantPropertiesType': 'image.minSampleValue',
             'animal': 'Horsey!'})

def test_fixity():
    generic_multi_record_good_values(f.build_fileFixity,
        {'fixityType': 'MD5',
         'fixityValue': 'eu8eu43riui26263e663td6t393d'},
        {'fixityType': 'SHA1',
         'fixityValue': '37yre783hdjioejdp98'})

def test_fixity_with_bad_values():
    generic_multi_record_bad_values(f.build_fileFixity,
        {'fixityType': 'MD5',
         'fixityValue': 'eu8eu43riui26263e663td6t393d'},
        {'fixityType': 'SHA1',
         'animal': 'horsey!'})

def test_creatingApplication():
    generic_good_values(f.build_creatingApplication,
        creatingApplicationName='Microsoft Word',
        creatingApplicationVersion='8.1',
        dateCreatedByApplication='2011-03-01')

def test_creatingApplication_bad_values():
    generic_bad_values(f.build_creatingApplication,
        creatingApplicationName='Microsoft Word',
        creatingApplicationVersion='8.1',
        dateCreatedByApplication='2011-03-01',
        animal='Horsey-worsey')

def test_inhibitors():
    generic_multi_record_good_values(f.build_inhibitors,
        {'inhibitorType': 'password',
         'inhibitorTarget': 'render',
         'inhibitorKey': 'P455W0rd!'},
        {'inhibitorType': 'password',
         'inhibitorTarget': 'render',
         'inhibitorKey': '53cR3t!'})

def test_inhibitors_bad_values():
    generic_multi_record_bad_values(f.build_inhibitors,
        {'inhibitorType': 'password',
         'inhibitorTarget': 'render',
         'inhibitorKey': 'P455W0rd!'},
        {'inhibitorType': 'password',
         'inhibitorTarget': 'render',
         'animal': 'Horsey!'})


def test_environment():
    generic_multi_record_good_values(f.build_environment,
        {'environmentCharacteristic': 'recommended',
         'environmentPurpose': 'edit',
         'environmentNote': 'Microsoft Office Suite 6.0 on Windows 8 OS, 64-bit Intel processor'})

def test_environment_bad_values():
    generic_multi_record_bad_values(f.build_environment,
        {'environmentCharacteristic': 'recommended',
         'environmentPurpose': 'edit',
         'animal': 'Horsey!'})

def test_environmentDependencies():
    generic_multi_record_good_values(f.build_environmentDependencies,
        {'dependencyName': 'TransformationProfile',
         'dependencyIdentifierValue1': 'URL',
         'dependencyIdentifierValue1': 'http://transform.org/9988142/transform.xsl'})


def test_environmentDependencies_bad_values():
    generic_multi_record_bad_values(f.build_environmentDependencies,
        {'dependencyName': 'TransformationProfile',
         'dependencyIdentifierValue1': 'URL',
         'animal': 'Horsey!'})

def test_environmentSoftware():
    generic_multi_record_good_values(f.build_environmentSoftware,
        {'softwareName': 'Adobe Illustrator',
         'softwareVersion': '6.0',
         'softwareType': 'edit, render'})

def test_environmentSoftware_bad_values():
    generic_multi_record_bad_values(f.build_environmentSoftware,
        {'softwareName': 'Adobe Illustrator',
         'softwareVersion': '6.0',
         'animal': 'Horsey!'})

def test_environmentSoftwareRegistry():
    generic_multi_record_good_values(f.build_environmentSoftwareRegistry,
        {'registryId': 'env01-soft9918'})

def test_environmentSoftwareRegistry_bad_values():
    try:
        esr = generic_multi_record_good_values(f.build_environmentSoftwareRegistry,
            {'animal': 'Horsey!'})
    except ValueError:
        esr = None
    assert(esr == None)


def test_environmentHardware():
    generic_multi_record_good_values(f.build_environmentHardware,
        {'hardwareName': 'Intel Pentium III',
         'hardwareType': 'processor',
         'hardwareOtherInformation': '266MHz or faster is required'})

def test_environmentHardware_bad_values():
    try:
        esr = generic_multi_record_good_values(f.build_environmentHardware,
            {'animal': 'Little piggies!'})
    except ValueError:
        esr = None
    assert(esr == None)


def test_envHardwareRegistry():
    generic_multi_record_good_values(f.build_envHardwareRegistry,
        {'registryId': 'env01-hw99282'})

def test_envHardwareRegistry_bad_values():
    try:
        esr = generic_multi_record_good_values(f.build_envHardwareRegistry,
            {'animal': 'Horsey!'})
    except ValueError:
        esr = None
    assert(esr == None)


def test_environmentExtension():
    generic_multi_record_good_values(f.build_environmentExtension,
        {'environmentExtension': '<xml><stub id="test">Stub XML</stub></xml>'})

def test_environmentExtension_bad_values():
    try:
        esr = generic_multi_record_good_values(f.build_environmentExtension,
            {'animal': 'Horsey!'})
    except ValueError:
        esr = None
    assert(esr == None)


def test_signatureInformation():
    generic_multi_record_good_values(f.build_signatureInformation,
        {'signatureInformationEncoding': 'Base64',
         'signer': 'National Archives of Sweden',
         'signatureValue': 'j84884tfedfdy29'})

def test_signatureInformation_bad_values():
    try:
        esr = generic_multi_record_good_values(f.build_signatureInformation,
            {'animal': 'Horsey!'})
    except ValueError:
        esr = None
    assert(esr == None)


def test_relationship():
    generic_multi_record_good_values(f.build_relationship,
        {'relationshipType': 'Sidecar File',
         'relationshipSubType': 'SAMMA metadata',
         'relatedObjectIdentifierType1': 'Preservica IE PID',
         'relatedObjectIdentifierValue1': 'PrIE1001'})

def test_relationship_bad_values():
    try:
        rel = generic_multi_record_good_values(f.build_relationship,
        {'relationshipType': 'Sidecar File',
         'relationshipSubType': 'SAMMA metadata',
         'relatedObjectIdentifierType1': 'Preservica IE PID',
         'relatedObjectIdentifierValue1': 'PrIE1001',
         'animal': 'Horsey!'})
    except ValueError:
        rel = None
    assert(rel == None)


def test_linkingIEIdentifier():
    generic_multi_record_good_values(f.build_linkingIEIdentifier,
        {'linkingIEIdentifierType': 'Appendix',
         'linkingIEIdentifierValue': 'IE1001',})

def test_linkingIEIdentifier_bad_values():
    try:
        esr = generic_multi_record_good_values(f.build_linkingIEIdentifier,
            {'animal': 'Horsey!'})
    except ValueError:
        esr = None
    assert(esr == None)


def test_event():
    generic_multi_record_good_values(f.build_event,
        {'eventType': 'PRE_INGEST',
         'eventDescription': 'preconditioning',
         'eventDateTime': '2016-08-21T09:17:22NZST',
         'eventOutcome1': 'File extension changed from ".tx" to ".txt"'})

def test_event_bad_values():
    try:
        gsr = generic_multi_record_bad_values(f.build_event,
            {'animal': 'horsey!'})
    except ValueError:
        gsr = None
    assert(gsr == None)