import math
import requests
import time

# K-samsök supports JSON if given the following Accept header
headers = {
    'Accept': 'application/json'
}

# We will work with two of K-samsöks methods search/fields for getting data
# and statisticSearch for automatic statistics
endpoint = 'http://www.kulturarvsdata.se/ksamsok/api'
endpoint_fields = '{}?&x-api=test&method=search&hitsPerPage=500&recordSchema=xml'.format(
    endpoint)
endpoint_facet = '{}?&x-api=test&method=statisticSearch&removeBelow=1'.format(
    endpoint)


# K-samsök uses the query language CQL
# it allows you to create very advanced queries
# https://www.loc.gov/standards/sru/cql/

# K-samsök has a lot of fields that you can query:
# https://www.raa.se/hitta-information/k-samsok/att-anvanda-k-samsok/index-for-statistic-facet/
# https://www.raa.se/hitta-information/k-samsok/att-anvanda-k-samsok/ytterligare-index-for-sok/

# Lets ask K-samsök for photos with images (thumbnails) which were taken before 1890
query = 'itemType=foto AND thumbnailExists=j AND create_fromTime<=1890'

# Lets also specify which fields we want to recive
fields = 'itemLabel,create_fromTime,thumbnail'

# the following is a generator
# a generator is similar to a function
# but insead of returning something once
# it returns mulityply things which you can loop over
# this particular generator uses K-samsöks methods search/fields to recive data
# you can resuse this generator in you own projects


def search_field_generator(query, fields):
    # initial query to know how many results we get
    query_url = '{}&query={}&fields={}&startRecord='.format(
        endpoint_fields, query, fields)
    r = requests.get(query_url, headers=headers)
    json = r.json()

    # K-samsök only returns 500 results in a single request
    # therefor we need to use the total number of results
    # to calculate the number of request we could potentially need to do
    total_results = json['result']['totalHits']
    required_n_requests = math.ceil(total_results / 500)

    # now we can start querying while keeping track of where in the results we are
    count = 0
    while required_n_requests > count:
        start_record = count * 500
        count += 1

        r = requests.get(query_url + str(start_record), headers=headers)
        response_data = r.json()

        for record in response_data['result']['records']['record']:
            # sometimes there are empty records and those has no fields :-(
            if not len(record) == 2:
                continue

            item_to_yield = {}

            # some fields can appear multiply times
            # therefor we need to merge those to lists if needed
            for field in record['field']:
                # if the field is already a list
                if isinstance(item_to_yield.get(field['name'], False), list):
                    item_to_yield[field['name']].append(field['content'])
                # if it's not yet a list but we found the same field name/key again
                elif item_to_yield.get(field['name'], False):
                    item_to_yield[field['name']] = list(
                        [item_to_yield[field['name']], field['content']])
                # default to just a regular value
                else:
                    item_to_yield[field['name']] = field['content']

            yield item_to_yield


def getrecords():

    # now we can loop our generator and print all the results
    for record in search_field_generator(query, fields):
        print(record)
    # you can change the values of query and fields get the data you need


# Lets move on to K-samsöks statisticSearch
# statisticSearch allows you get statistics fo the values
# in an index/field for a specified query

# As an example let us ask K-samsök which data providers
# provides the records for the query we just tested

# the provider is found in the following index
index = 'serviceOrganization'

# again we create something reusable, in this case a regular function


def statistic_search(query, index):
    query_url = '{}&query={}&index={}=*'.format(endpoint_facet, query, index)
    r = requests.get(query_url, headers=headers)
    json = r.json()

    result = list()
    for value in json['result']['term']:
        value_to_append = {}
        value_to_append['count'] = value['records']
        value_to_append['value'] = value['indexFields']['value']

        result.append(value_to_append)
    return result


def stats():
    """
    providers_statistics = statistic_search(query, index)
    print(providers_statistics)
    """
    # Now lets reuse it and ask the same question
    # but for the field "dataQuality" and for all K-samsök records
    print(statistic_search('*', 'itemLicense'))
    # again you can change both the query and index
    # to get other statistics


stats()