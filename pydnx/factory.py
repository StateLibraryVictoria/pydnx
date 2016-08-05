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