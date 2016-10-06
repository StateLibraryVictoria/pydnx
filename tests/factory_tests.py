from nose.tools import *
from lxml import etree as ET

import pydnx.factory as f


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
    generic_good_values(f.build_objectIdentifier, 
        objectIdentifierType='RecordID',
        objectIdentifierValue='P8881')

def test_objectIdentifier_with_bad_values():
    generic_bad_values(f.build_objectIdentifier, 
        objectIdentifierType='RecordID',
        favouriteVehicle='Tractor')

def test_preservationLevel():
    generic_good_values(f.build_preservationLevel, 
        preservationLevelValue='Preservation Master', 
        preservationLevelRationale='' +
            'Born Digital record to be retained as National Archives',
        preservationLevelDateAssigned='2016-08-01')

def test_preservationLevel_with_bad_values():
    generic_bad_values(f.build_preservationLevel, 
        preservationLevelValue='Preservation Master', 
        preservationLevelRationale='' +
            'Born Digital record to be retained as National Archives',
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

def test_objectCharacteristicsExtension():
    generic_good_values(f.build_objectCharacteristicsExtension,
        objectCharacteristicsExtension="<test>Test XML</test>")

def test_objectCharacteristicsExtension_bad_values():
    generic_bad_values(f.build_objectCharacteristicsExtension,
        animal='horsey!')


def test_environment():
    generic_multi_record_good_values(f.build_environment,
        {'environmentCharacteristic': 'recommended',
         'environmentPurpose': 'edit',
         'environmentNote': 'Microsoft Office Suite 6.0 on Windows 8 OS,' + 
            ' 64-bit Intel processor'})

def test_environment_bad_values():
    generic_multi_record_bad_values(f.build_environment,
        {'environmentCharacteristic': 'recommended',
         'environmentPurpose': 'edit',
         'animal': 'Horsey!'})

def test_environmentDependencies():
    generic_multi_record_good_values(f.build_environmentDependencies,
        {'dependencyName': 'TransformationProfile',
         'dependencyIdentifierValue1': 'URL',
         'dependencyIdentifierValue1': '' + 
            'http://transform.org/9988142/transform.xsl'})


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
        esr = generic_multi_record_good_values(
            f.build_environmentSoftwareRegistry,
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
        {'environmentExtension': '' + 
            '<xml><stub id="test">Stub XML</stub></xml>'})

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

def test_signatureInformationExtension():
    generic_good_values(f.build_signatureInformationExtension, 
        signatureInformationExtension='<ext>Test Value</ext>')

def test_signatureInformationExtension_bad_values():
    generic_bad_values(f.build_signatureInformationExtension,
        animal='horsey!')


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
        evt = generic_multi_record_bad_values(f.build_event,
            {'animal': 'horsey!'})
    except ValueError:
        evt = None
    assert(evt == None)


def test_linkingRightsStatementIdentifier():
    generic_multi_record_good_values(f.build_linkingRightsStatementIdentifier,
        {'linkingRightsStatementIdentifierType': 'CMSRightsID',
         'linkingRightsStatementIdentifierValue': '0001'})

def test_linkingRightsStatementIdentifier_bad_values():
    try:
        lrsi = generic_multi_record_bad_values(
            f.build_linkingRightsStatementIdentifier,
                {'animal': 'horsey!'})
    except ValueError:
        lrsi = None
    assert(lrsi == None)

def test_accessRightsPolicy():
    generic_good_values(f.build_accessRightsPolicy, policyId='100',
        policyDescription='Open Access')

def test_accessRightsPolicy_bad_values():
    generic_bad_values(f.build_accessRightsPolicy, policyId='400',
        policyDescription='restricted access',
        animal='horsey-worsey!')

def test_retentionPeriodPolicy():
    generic_good_values(f.build_retentionPeriodPolicy, policyId='99YEARS',
        policyDescription="" + 
        "I got 99 problems but a retention policy ain't one")

def test_retentionPeriodPolicy_bad_values():
    generic_bad_values(f.build_retentionPeriodPolicy, policyId='5YEARS',
        animal='horsey!')

def test_grantedRightsStatement():
    generic_multi_record_good_values(f.build_grantedRightsStatement, 
        {'grantedRightsStatementIdentifier': 'grsID',
        'grantedRightsStatementValue': '000001'})

def test_grantedRightsStatement_bad_values():
    try:
        grs = generic_multi_record_bad_values(
            f.build_linkingRightsStatementIdentifier,
                {'animal': 'horsey!'})
    except ValueError:
        grs = None
    assert(grs == None)

def test_collection():
    generic_multi_record_good_values(f.build_collection,
        {'collectionID': 'coll99',
         'collectionName': 'Primary Collection'})

def test_collection_bad_values():
    try:
        c = generic_multi_record_bad_values(f.build_collection,
            {'animal': 'horsey!'})
    except ValueError:
        c = None
    assert(c == None)


def test_build_ie_amdTech():
    gic = [{'submissionReason': 'bornDigital', 'IEEntityType': 'periodicIE'}]
    ieamdtech = f.build_ie_amdTech(generalIECharacteristics=gic)
    print(ET.tostring(ieamdtech))


def test_build_ie_amdTech_bad_values():
    gic = [{'animal': 'horsey', 'IEEntityType': 'periodicIE'}]
    oc = [{'objectType': 'INTELLECTUAL_ENTITY'}]
    try:
        ieamdtech = f.build_ie_amdTech(generalIECharacteristics=gic,
            objectCharacteristics=oc)
    except TypeError:
        ieamdtech = None
    assert(ieamdtech == None)

def test_build_rep_amdTech():
    grc = [{'label': 'Digital Original',
        'preservationType': 'Preservation Master',
        'usageType': 'VIEW',
        'DigitalOriginal': 'true',
        'RevisionNumber': '1'}]
    repamdtech = f.build_rep_amdTech(generalRepCharacteristics=grc)
    print(ET.tostring(repamdtech))


def test_build_rep_amdTech_bad_values():
    grc = [{'animal': 'horsey!'}]
    try:
        repamdtech = f.build_rep_amdTech(generalRepCharacteristics=grc)
    except TypeError:
        repamdtech = None
    assert(repamdtech == None)

def test_build_file_amdTech():
    gfc = [{'label': 'good file', 'note': 'the very finest of files',
        'fileOriginalName': 'awesome.tif',
        'fileOriginalPath': '/home/employee/awesome.tif', 
        'fileMIMEType': 'image/tiff'}]
    obj_chars = [{'objectType': 'FILE'}]
    creating_app = [{'creatingApplicationName': 'GIMP', 
        'creatingApplicationVersion': 'v1.0.9'}]
    fileamdtech = f.build_file_amdTech(generalFileCharacteristics=gfc,
        objectCharacteristics=obj_chars, creatingApplication=creating_app)
    print(ET.tostring(fileamdtech))


def test_build_ie_amdTech_with_cms():
    gic = [{'submissionReason': 'bornDigital', 'IEEntityType': 'periodicIE'}]
    oc = [{'objectType': 'INTELLECTUAL_ENTITY'}]
    cms = [{'system': 'emu', "recordId": "88838"}]
    ieamdtech = f.build_ie_amdTech(generalIECharacteristics=gic,
        objectCharacteristics=oc, CMS=cms)
    print(ET.tostring(ieamdtech))


def test_build_ie_amdTech_with_cms_and_objectIdentifier():
    gic = [{'submissionReason': 'bornDigital', 'IEEntityType': 'periodicIE'}]
    oc = [{'objectType': 'INTELLECTUAL_ENTITY'}]
    cms = [{'system': 'emu', "recordId": "88838"}]
    oid = [{'objectIdentifierType': 'AlmaID',
            'objectIdentifierValue': 'AAA90'}]
    ieamdtech = f.build_ie_amdTech(generalIECharacteristics=gic,
        objectCharacteristics=oc, CMS=cms, objectIdentifier=oid)
    print(ET.tostring(ieamdtech))


def test_build_ie_amdTech_with_webharvesting():
    gic = [{'submissionReason': 'bornDigital', 'IEEntityType': 'periodicIE'}]
    oc = [{'objectType': 'INTELLECTUAL_ENTITY'}]
    cms = [{'system': 'emu', "recordId": "88838"}]
    oid = [{'objectIdentifierType': 'AlmaID',
            'objectIdentifierValue': 'AAA90'}]
    web = [{'harvestDate': '2016-09-23 15:11:21.0', 
        'primarySeedURL': 'http://www.thegoogles.com',
        'targetName': 'The almighty Googles'}]
    ieamdtech = f.build_ie_amdTech(
            generalIECharacteristics=gic,
            objectCharacteristics=oc,
            CMS=cms,
            objectIdentifier=oid,
            webHarvesting=web)
    print(ET.tostring(ieamdtech))


def test_build_ie_amdRights():
    rights = [{'policyId': '100', 'policyDescription': 'Open Access'}]
    ieamdrights = f.build_ie_amdRights(accessRightsPolicy=rights)
    print(ET.tostring(ieamdrights))


def test_build_ie_amdDigiprov():
    events = [{'eventType': 'PRE_INGEST',
             'eventDescription': 'preconditioning',
             'eventDateTime': '2016-08-21T09:17:22NZST',
             'eventOutcome1': 'File extension changed from ".tx" to ".txt"'},
             {'eventType': 'PRE_INGEST',
             'eventDescription': 'preconditioning',
             'eventDateTime': '2016-09-13T13:21:45NZST',
             'eventOutcome1': 'File extension changed from' +
                ' ".txt" back to ".tx"'}]
    ieamddigiprov = f.build_ie_amdDigiprov(event=events)
    print(ET.tostring(ieamddigiprov))