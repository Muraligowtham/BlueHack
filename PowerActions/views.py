from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import requests;

import SoftLayer
import subprocess

def getdetails(request):
    photos = []
    oauth2 = {
        'X-ApiKeys': 'client_secret=wYSIxAY1HPwPcFhLq5QQnw; client_secret=glAxueBFCM2f5e0lScXIv2Gwj2FE4w6HsIdCx95JghfS98CGcXXEagGhZHj3F5na'}
    x = Authentification(
        'https://api.yelp.com/v3/businesses/search?location=United states&term=Burrito', oauth2)
    for b in x["businesses"]:
        a = Authentification('https://api.yelp.com/v3/businesses/%s' % b["id"], oauth2)

        for p in a["photos"]:
          photos.append(p+";")

        return HttpResponse(photos)




def Authentification(url,oauth2):
    try:
        m_request = requests.get(url, headers={
            "Authorization": "Bearer qcp3Z4N4028n237B-6R-IdWi02Sd00-9UWP2iK73zqg6oIgvVn6KFzoeMLMqbvLP1eDbOOR9cLmHCCrcDqX2lsbxZ5h1HHzySoMsIGW5D-C1ADiToS0q0ojl9shwWXYx"})
    except Exception as e:
        print
        e
    else:
        x = m_request.json()
    return x


def index(request):
    return HttpResponse("<h1>Perform the action<h1>")


def indexon(request):
    return HttpResponse("<h1>Perform On action<h1>")

def ConnecttoDevice(request):
    username = 'mbalaji'
    key = '8aad3f6cf9a4a7f189bd1019aea3bf725a425a9bfae4a06309896dcbfcdb8c05'
    client = SoftLayer.Client(username=username, api_key=key)

    try:
        # Getting all virtual guest that the account has:
        virtualGuests = client['SoftLayer_Account'].getVirtualGuests()
    except SoftLayer.SoftLayerAPIError as e:
        """
        If there was an error returned from the SoftLayer API then bomb out with the
        error message.
        """
        print("Unable to retrieve hardware. "
              % (e.faultCode, e.faultString))
    return HttpResponse(virtualGuests)


def PowerOffaDevice(request):
    username = 'mbalaji'
    key = '8aad3f6cf9a4a7f189bd1019aea3bf725a425a9bfae4a06309896dcbfcdb8c05'
    client = SoftLayer.Client(username=username, api_key=key)

    try:
        # Getting all virtual guest that the account has:
        virtualGuests = client['SoftLayer_Account'].getVirtualGuests()
    except SoftLayer.SoftLayerAPIError as e:
        """
        If there was an error returned from the SoftLayer API then bomb out with the
        error message.
        """
        print("Unable to retrieve hardware. "
              % (e.faultCode, e.faultString))



    try:

        virtualGuestName = 'Automate13f06.forest06.fiberlinkqa.local'
        for virtualGuest in virtualGuests:
            if virtualGuest['fullyQualifiedDomainName'] == virtualGuestName:
                virtualGuestId = virtualGuest['id']
        # Power off the virtual guest
        virtualMachines = client['SoftLayer_Virtual_Guest'].powerOff(id=virtualGuestId)
        print("powered off")
    except SoftLayer.SoftLayerAPIError as e:
        """
        If there was an error returned from the SoftLayer API then bomb out with theAA
        error message.
        """
        print("Unable to power off the virtual guest"
              % (e.faultCode, e.faultString))
    return HttpResponse('<h1>PoweredOff<h1>')

def PowerOnADevice(request):
        username = 'mbalaji'
        key = '8aad3f6cf9a4a7f189bd1019aea3bf725a425a9bfae4a06309896dcbfcdb8c05'
        client = SoftLayer.Client(username=username, api_key=key)

        try:
            # Getting all virtual guest that the account has:
            virtualGuests = client['SoftLayer_Account'].getVirtualGuests()
        except SoftLayer.SoftLayerAPIError as e:
            """
            If there was an error returned from the SoftLayer API then bomb out with the
            error message.
            """
            print("Unable to retrieve hardware. "
                  % (e.faultCode, e.faultString))

        try:

            virtualGuestName = 'Automate13f06.forest06.fiberlinkqa.local'
            for virtualGuest in virtualGuests:
                if virtualGuest['fullyQualifiedDomainName'] == virtualGuestName:
                    virtualGuestId = virtualGuest['id']
            # Power off the virtual guest
            virtualMachines = client['SoftLayer_Virtual_Guest'].powerOn(id=virtualGuestId)
            print("powered On")
        except SoftLayer.SoftLayerAPIError as e:
            """
            If there was an error returned from the SoftLayer API then bomb out with the
            error message.
            """
            print("Unable to power off the virtual guest"% (e.faultCode, e.faultString))
        return HttpResponse('<h1>PoweredOn<h1>')


