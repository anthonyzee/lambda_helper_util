def getRequestContext(oEventObject):

    oRequestContext = {
        "HttpMethod": "",
        "UrlPath": "",
        "UsingFunctionUrl": False
    }
    if 'requestContext' in oEventObject:
        if 'http' in oEventObject['requestContext']:
            oRequestContext["HttpMethod"] = oEventObject['requestContext']['http']['method']
            oRequestContext["UsingFunctionUrl"] = True

    if 'httpMethod' in oEventObject:
        oRequestContext["HttpMethod"] = oEventObject['httpMethod']
    
    if 'rawPath' in oEventObject:
        oRequestContext["UrlPath"] = oEventObject['rawPath']
        oRequestContext["UsingFunctionUrl"] = True
    elif 'path' in oEventObject:
        oRequestContext["UrlPath"] = oEventObject['path']
            
    return oRequestContext

def getPathValue(sRawPath, nPathIndex):
    sRawPathList = sRawPath.split('?')
    sRawPathList = sRawPathList[0].split('/')
    return sRawPathList[nPathIndex]

def getLastPathValue(sRawPath):
    
    # initialize variable
    sLastPathValue = ""

    sRawPathList = sRawPath.split('?')
    sRawPathList = sRawPathList[0].split('/')

    sLastPathValue = sRawPathList[len(sRawPathList) - 1]

    return sLastPathValue

def getHeaderObject(oEventObject):

    # initialize variable
    oNewHeaderObject = {}

    if 'headers' in oEventObject:
        if oEventObject['headers'] != None:
            for sHeaderName in oEventObject['headers']:
                oNewHeaderObject[sHeaderName.lower()] = oEventObject['headers'][sHeaderName]

    return oNewHeaderObject

def createResponseObject(nStatusCode, sResponseBody, bCORS):

    oResponseObject = {
        'statusCode': nStatusCode,
        'body': sResponseBody
    }

    if bCORS == True:
        oResponseObject['headers'] = {
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Methods': '*',
            'Access-Control-Allow-Origin': '*'
        }
    
    return oResponseObject 
