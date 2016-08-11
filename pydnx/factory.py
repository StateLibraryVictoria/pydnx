from lxml import etree as ET
# import model as m

DNX_NS = "http://www.exlibrisgroup.com/dps/dnx"
dnx_nsmap = {
    'dnx': DNX_NS
}

ET.register_namespace('dnx', DNX_NS)

GENERAL_REP_CHARACTERISTICS = ['label', 'preservationType', 'usageType',
    'representationEntityType', 'contentType', 'contextType', 'hardwareUsed',
    'physicalCarrierMedia', 'derivedFromId', 'deliveryPriority',
    'orderingSequence', 'DigitalOriginal', 'RevisionNumber',
    'RepresentationCode', 'TaskID', 'RepresentationOriginalName', 'UserDefinedA',
    'UserDefinedB', 'UserDefinedC']

GRC = {'label': None, 'preservationType': None, 'usageType': None}


def _build_generic_section(section_name, keynames=None):
    section = ET.Element('{http://www.exlibrisgroup.com/dps/dnx}section', id=section_name)
    record = ET.SubElement(section, '{http://www.exlibrisgroup.com/dps/dnx}record')
    for key in keynames:
        if keynames[key] != None:
            record_key = ET.SubElement(record, '{http://www.exlibrisgroup.com/dps/dnx}key', id=key)
            record_key.text = keynames[key]
    return section

def _build_generic_repeatable_section(section_name, allowed_keys, *args):
    section = ET.Element('{http://www.exlibrisgroup.com/dps/dnx}section',
        id=section_name)
    for arg in args:
        record = ET.SubElement(section, '{http://www.exlibrisgroup.com/dps/dnx}record')
        for key in arg.keys():
            if key in allowed_keys:
                record_key = ET.SubElement(record, '{http://www.exlibrisgroup.com/dps/dnx}key')
                record_key.attrib['ID'] = key
                record_key.text = arg[key]
            else:
                raise ValueError("\"{}\" is not a permitted key in {} record dictionary ( acceptable values are {} )".format(
                    key, section_name, allowed_keys))
    return section

def build_generalIECharacteristics(submissionReason=None, status=None, statusDate=None,
        IEEntityType=None, UserDefinedA=None, UserDefinedB=None, UserDefinedC=None):
        # Note: statusDate is used by the system - not really for pre-ingest use
        
    return _build_generic_section('generalIECharacteristics', locals())


def build_generalRepCharacteristics(label=None, preservationType=None, usageType=None,
        representationEntityType=None, contentType=None, contextType=None, hardwareUsed=None,
        physicalCarrierMedia=None, derivedFromId=None, deliveryPriority=None,
        orderingSequence=None, DigitalOriginal=None, RevisionNumber=None,
        RepresentationCode=None, TaskID=None, RepresentationOriginalName=None, UserDefinedA=None,
        UserDefinedB=None, UserDefinedC=None):
        # Mandatory: preservationType, usageType(only "VIEW" supported)
    return _build_generic_section('generalRepCharacteristics', locals())



def build_generalFileCharacteristics(label=None, note=None,
        FileEntityType=None, compositionLevel=None, fileLocationType=None, 
        fileLocation=None, fileOriginalName=None,
        fileOriginalPath=None, fileOriginalID=None, fileExtension=None,
        fileMIMEType=None, fileSizeBytes=None, storageID=None, streamRefId=None,
        formatLibraryId=None, riskLibraryIdentifiers=None):
        # Note: fileLocationType is used by the system - not really for pre-ingest use
        # Note: fileOriginalID is used by the system - not really for pre-ingest use
        # Note: fileExtension is used by the system - not really for pre-ingest use
        # Note: formatLibraryId is used by the system - not really for pre-ingest use
        # Note: riskLibraryIdentifiers is used by the system - not really for pre-ingest use
        # fileMIMEType can be submitted by user, or it will be set by system on ingest
        # fileSizeBytes can be submitted by user, or it will be set by system on ingest
        # Note: storageID and streamRefId currently not in use
    return _build_generic_section('generalFileCharacteristics', locals())


def build_objectCharacteristics(objectType=None, groupID=None):
    # parentID - set during loading stage
    # creationDate - set during loading stage
    # createdBy - set during loading stage
    # modificationDate - set in system, on committing new version
    # modifiedBy - set in system, on committing new version
    # owner - set in system during loading stage
    return _build_generic_section('objectCharacteristics', locals())

def build_cms(system=None, recordId=None):
    # mId = system-generated
    return _build_generic_section('CMS', locals())

def build_webHarvesting(primarySeedURL=None, WCTIdentifier=None,
        targetName=None, group=None, harvestDate=None, harvestTime=None):
    return _build_generic_section('webHarvesting', locals())

# internalIdentifier -- Not used for pre-ingest

def build_objectIdentifier(objectIdentifierType=None, objectIdentifierValue=None):
    return _build_generic_section('objectIdentifier', locals())


def build_preservationLevel(preservationLevelValue=None, 
        preservationLevelRole=None, preservationLevelRationale=None,
        preservationLevelDateAssigned=None):
    return _build_generic_section('preservationLevel', locals())


# def build_significantProperties(*args):
#     section = ET.Element('{http://www.exlibrisgroup.com/dps/dnx}section',
#         id='significantProperties')
#     for arg in args:
#         record = ET.SubElement(section, '{http://www.exlibrisgroup.com/dps/dnx}record')
#         for key in arg.keys():
#             record_key = ET.SubElement(record, '{http://www.exlibrisgroup.com/dps/dnx}key')
#             record_key.attrib['ID'] = key
#             record_key.text = arg[key]
#     return section

def build_significantProperties(*args):
    allowed_keys = ['significantPropertiesType', 'significantPropertiesValue',
                    'significantProperiesExtension']
    return _build_generic_repeatable_section('significantProperties', 
        allowed_keys, *args)

def build_fileFixity(*args):
    allowed_keys = ['agent', 'fixityType', 'fixityValue']
    return _build_generic_repeatable_section('fileFixity', allowed_keys,
        *args)

def build_creatingApplication(creatingApplicationName=None,
        creatingApplicationVersion=None,
        dateCreatedByApplication=None,
        creatingApplicationExtension=None):
    return _build_generic_section('creatingApplication', locals())


def build_inhibitors(*args):
    allowed_keys = ['inhibitorType', 'inhibitorTarget', 'inhibitorKey']
    return _build_generic_repeatable_section('inhibitors', allowed_keys,
        *args)


def build_environment(*args):
    allowed_keys = ['environmentCharacteristic', 'environmentPurpose',
        'environmentNote']
    return _build_generic_repeatable_section('environment', allowed_keys,
        *args)


def build_environmentDependencies(*args):
    allowed_keys = ['dependencyName', 'dependencyIdentifierValue1',
        'dependencyIdentifierValue1', 'dependencyIdentifierType2',
        'dependencyIdentifierType2', 'dependencyIdentifierValue3',
        'dependencyIdentifierType3']
    return _build_generic_repeatable_section('environmentDependencies', 
            allowed_keys, *args)

def build_environmentSoftware(*args):
    allowed_keys = ['softwareName', 'softwareVersion', 'softwareType',
        'softwareOtherInformation', 'softwareOtherInformation',
        'softwareDependancy']
    return _build_generic_repeatable_section('environmentSoftware',
            allowed_keys, *args)

def build_environmentSoftwareRegistry(*args):
    return _build_generic_repeatable_section('environmentSoftwareRegistry',
        ['registryId'], *args)

def build_environmentHardware(*args):
    allowed_keys = ['hardwareName', 'hardwareType', 'hardwareOtherInformation']
    return _build_generic_repeatable_section('environmentHardware',
        allowed_keys, *args)

def build_envHardwareRegistry(*args):
    return _build_generic_repeatable_section('environmentSoftwareRegistry',
        ['registryId'], *args)

def build_environmentExtension(*args):
    return _build_generic_repeatable_section('environmentExtension',
        ['environmentExtension'], *args)

def build_signatureInformation(*args):
    allowed_keys = ['signatureInformationEncoding', 'signer', 'signatureMethod',
        'signatureValue', 'signatureValidationRules', 'signatureProperties',
        'keyInformation']
    return _build_generic_repeatable_section('signatureInformation',
        allowed_keys, *args)


def build_relationship(*args):
    allowed_keys = ['relationshipType', 'relationshipSubType',
        'relatedObjectIdentifierType1', 'relatedObjectIdentifierValue1',
        'relatedObjectSequence1', 'relatedObjectIdentfierType2',
        'relatedObjectIdentifierValue2', 'relatedObjectSequence2',
        'relatedObjectIdentifierType3', 'relatedObjectIdentifierValue3',
        'relatedObjectSequence3']
    return _build_generic_repeatable_section('relationship', allowed_keys,
        *args)


def build_linkingIEIdentifier(*args):
    allowed_keys = ['linkingIEIdentifierType', 'linkingIEIdentifierValue']
    return _build_generic_repeatable_section('linkingIEIdentifier',
        allowed_keys, *args)
