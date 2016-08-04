from lxml import etree as ET

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


def build_generic_section(section_name, keynames=None):
	section = ET.Element('{http://www.exlibrisgroup.com/dps/dnx}section', id=section_name)
	record = ET.SubElement(section, '{http://www.exlibrisgroup.com/dps/dnx}record')
	for key in keynames:
		if keynames[key] != None:
			record_key = ET.SubElement(record, '{http://www.exlibrisgroup.com/dps/dnx}key', id=key)
			record_key.text = keynames[key]
	return section


def build_generalRepCharacteristics(label=None, preservationType=None, usageType=None,
		representationEntityType=None, contentType=None, contextType=None, hardwareUsed=None,
		physicalCarrierMedia=None, derivedFromId=None, deliveryPriority=None,
		orderingSequence=None, DigitalOriginal=None, RevisionNumber=None,
		RepresentationCode=None, TaskID=None, RepresentationOriginalName=None, UserDefinedA=None,
		UserDefinedB=None, UserDefinedC=None):
	return build_generic_section('generalRepCharacteristics', locals())


def build_generalIECharacteristics(submissionReason=None, status=None, statusDate=None,
		IEEntityType=None, UserDefinedA=None, UserDefinedB=None, UserDefinedC=None):
		# Note: statusDate is supposed to be used by the system only - consider removing
	return build_generic_section('generalIECharacteristics', locals())


def build_generalFileCharacteristics(label=None, note=None,
	FileEntityType=None, compositionLevel=None, fileLocationType=None, 
	fileLocation=None, fileOriginalName=None,
	fileOriginalPath=None, fileOriginalID=None, fileExtension=None,
	fileMIMEType=None, fileSizeBytes=None, storageID=None, streamRefId=None,
	formatLibraryId=None, riskLibraryIdentifiers=None):
	return build_generic_section('generalFileCharacteristics', locals())