# coding=utf-8
import logging

import requests

log = logging.getLogger(__name__)


class AddressLookup(object):
    def __init__(self, key, url=None):
        if not key:
            raise Exception("OS Places API key required")
        self.key = key
        if not url:
            url = "https://api.ordnancesurvey.co.uk/places/v1/addresses/postcode"
        self.url = url

    def by_postcode(self, postcode):
        params = {'postcode': postcode,
                  'key': self.key,
                  'output_srs': 'WGS84',
                  'dataset': 'DPA',
                  }
        try:
            os_places_response = requests.get(self.url, params, timeout=3)
            os_places_response.raise_for_status()
        except requests.exceptions.RequestException as e:
            log.error('OS Places request error: {}'.format(e))
        else:
            try:
                return os_places_response.json().get('results', [])
            except ValueError as e:
                log.warning('OS Places response JSON parse error: {}'.format(e))
        return []


class FormattedAddressLookup(AddressLookup):
    def format_address_from_result(self, raw_result):
        dpa_result = raw_result.get('DPA')
        if dpa_result:
            return self.format_address_from_dpa_result(dpa_result)

    @staticmethod
    def format_address_from_dpa_result(raw_result):
        formatted_components = []
        for key in ["BUILDING_NAME", "BUILDING_NUMBER", "THOROUGHFARE_NAME", "DEPENDENT_LOCALITY", "POST_TOWN"]:
            formatted_components.append(raw_result.get(key, '').title())
        formatted_components.append(raw_result.get("POSTCODE", '').upper())
        return '\n'.join([c for c in formatted_components if c])

    def by_postcode(self, postcode):
        os_places_results = super(FormattedAddressLookup, self).by_postcode(postcode)
        return [self.format_address_from_result(result) for result in os_places_results]
