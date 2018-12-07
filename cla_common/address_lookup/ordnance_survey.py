# coding=utf-8
import logging

import requests

log = logging.getLogger(__name__)


class OsAddressLookup(object):
    def __init__(self, key, url=None):
        if not key:
            raise Exception("OS Places API key required")
        self.key = key
        if not url:
            url = "https://api.ordnancesurvey.co.uk/places/v1/addresses/postcode"
        self.url = url

    def lookup_postcode(self, postcode):
        params = {'postcode': postcode,
                  'key': self.key,
                  'output_srs': 'WGS84',
                  'dataset': 'DPA',
                  # 'maxresults': 100,  # TODO Consider postcodeinfo default maxresults
                  # 'dataset': 'DPA,LPI'  # Only request DPA results by default. TODO Confirm exclusion of LPI results.
                  #  See https://apidocs.os.uk/docs/os-places-lpi-output
                  }
        try:
            os_places_response = requests.get(self.url, params, timeout=3)  # TODO lookup SLA, adjust timeout
            os_places_response.raise_for_status()
        except requests.exceptions.RequestException as e:
            log.error('Requests error: {}'.format(e))
        else:
            try:
                return os_places_response.json().get('results', [])
            except ValueError as e:
                log.warning('os_places_response JSON parse error: {}'.format(e))
        return []


class OsAddressLookupFormatted(OsAddressLookup):
    def format_address_from_result(self, raw_result):
        dpa_result = raw_result.get('DPA')
        if dpa_result:
            return self.format_address_from_dpa_result(dpa_result)
        # lpi_result = raw_result.get('LPI')
        # if lpi_result:
        #     return format_address_from_lpi_result(lpi_result)

    @staticmethod
    def format_address_from_dpa_result(raw_result):
        formatted_components = []
        # TODO Merge lines for "BUILDING_NUMBER" and "THOROUGHFARE_NAME"
        # TODO Bother with special title casing?  https://stackoverflow.com/a/3729957
        for key in ["BUILDING_NAME", "BUILDING_NUMBER", "THOROUGHFARE_NAME", "DEPENDENT_LOCALITY", "POST_TOWN"]:
            formatted_components.append(raw_result.get(key, '').title())
        formatted_components.append(raw_result.get("POSTCODE", '').upper())
        return '\n'.join([c for c in formatted_components if c])

    # def format_address_from_lpi_result(raw_result):
    #     formatted_components = []
    #     for key in ["PAO_START_NUMBER", "STREET_DESCRIPTION", "TOWN_NAME", "LOCAL_CUSTODIAN_CODE_DESCRIPTION"]:
    #         formatted_components.append(raw_result.get(key, '').title())
    #     formatted_components.append(raw_result.get("POSTCODE_LOCATOR", '').upper())
    #     return '\n'.join([c for c in formatted_components if c])

    def lookup_postcode(self, postcode):
        os_places_results = super(OsAddressLookupFormatted, self).lookup_postcode(postcode)
        return [self.format_address_from_result(result) for result in os_places_results]
