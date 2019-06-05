# Hack Oregon Data APIs v1 Style Guide

## Overview

The intent of this document is to provide some guidance for API developers when building APIs under Hack Oregon Projects. Our aim is to follow general RESTful API best practices, and work with solutions/standards that are built into our technology stack.

We aim to also provide the highest level of interoperability between our APIs. By adopting standards between teams, we can better support users connecting to multiple APIs.

### API Technologies
* **HTTPS:** All API requests must be made over HTTPS.
* **JSON:** All API request and response bodies will be JSON.

## Requests

Requests and endpoints should follow a common REST-based structure.

### URL Structure

* URLs will use the Hack Oregon team name as the root:  
  Pattern: `:team_name/v1/:resource name`   
  Example: `transportation_systems/v1/stops`  


* URLs will be prefixed by the major version number:  
  Pattern: `/v1/:resource name`  
  Example: `/v1/stops`  

* Collections of resources are referenced by their resource name (plural):  
  Pattern: `/v1/:resource name`  
  Example: `/v1/stops`

* Individual resources are referenced by their resource name (plural) followed by the guid:  
  Pattern: `/v1/:resource name/:guid`  
  Example: `/v1/stops/25fe21b8-8de2-40d0-93b0-c819101d1a11`


### GET

Request a single resource or collection of Resources

* GET requests may include query parameters
* GET requests **Should Avoid** including a request body
    - Request Bodies may be used to avoid extreme URL length

#### Single Resource

```
GET /v1/stops/25fe21b8-8de2-40d0-93b0-c819101d1a11
```

##### Responses (Resource)

|Scenario|Code|Body|
|---|---|---|
| Valid Resource/Request | 200 | Resource |
| Bad Request | 400 | Error |
| Not Authorized | 403 | Error |
| Not Found | 404 | Error |
| Internal Server Error | 500 | Error |

#### Collection

```
GET /v1/stops
```

##### Responses (Resource)

|Scenario|Code|Body|
|---|---|---|
| Valid Resource/Request | 200 | List of Resources (All or Paginated) |
| Valid Resource, No Results | 200 | JSON response with empty array for Resource ex: `{"data": []}`|
| Bad Request | 400 | Error |
| Not Authorized | 403 | Error |
| Internal Server Error | 500 | Error |

#### Recommended Supporting Technologies

* Django Rest Framework [Viewsets](https://www.django-rest-framework.org/api-guide/viewsets/) and [Mixins](https://www.django-rest-framework.org/api-guide/generic-views/#mixins) should generally handle this behavior. If you are writing custom views, use built-in status codes.

* Users will have to correctly provide routing

* Django Rest Framework allows [versioning](https://www.django-rest-framework.org/api-guide/versioning/) to be handled through a few methods.

## Response Codes

### Successful Requests

|Status Code|Description|Verbs|
|---|---|---|
|200 OK|This status **MUST** be returned for synchronous requests that complete successfully and have a response body. This **MUST** only be used if there is not a more appropriate 2XX response code. |GET, PATCH|

### Client Errors

|Status Code|Description|Verbs|
|---|---|---|
|400 Bad Request|This status **MUST** be returned for requests that provide malformed or invalid data. Examples: malformed request body or invalid request fields.|GET, PATCH, POST, DELETE|
|403 Forbidden|This status **MUST** be returned if the request cannot be performed by the user due to lack of permissions. Example: User with read-only permissions to a resource tries to update it. |POST, PATCH, DELETE|
|404 Not Found|This status **MUST** be returned if the requested resource does not exist or if the user requesting the resource has insufficient permissions to view the resource.|GET, POST, PATCH, DELETE|

### Server Errors

|Status Code|Description|
|---|---|
|500 Internal Server Error|This status **MUST** be returned when a server error occurs.

## Resources

A resource represents an individual object within the system.  It is represented as a JSON object.  

## Field Names

Resource Fields will be camelCase.

Resource Fields MUST include ONLY the following characters:

* `a-z` (lowercase alpha)
* `A-Z` (uppercase alpha)

Resource fields that accept multiple values MUST be pluralized.

#### Recommended Supporting Technologies

* https://github.com/vbabiy/djangorestframework-camel-case

## Collections

A collection is a list of multiple Resources.

A collection is represented as a JSON object.

A collection object **MUST** contain:

* `count` - Total count of all Resources
* `results` - Array of individual resources returned

If a collection is paginated, then it **MUST** contain pagination links, `next` and `previous`, with appropriate `null` values (See [Pagination](#Pagination)).

```JSON

{
  "count": 49759,
  "next": "http://service.civicpdx.org/housing-affordability/api/harvardjchs/?limit=10&offset=10",
  "previous": null,
  "results": [
    {
      "id": 848,
      "date": "1996-01-01",
      "dataPoint": "Total",
      "dataType": "All Households by Nativity",
      "source": "W-2",
      "valueType": "count",
      "value": "98574707.36667",
      "rank": 5,
      "total": 5
    },
    {
      "id": 844,
      "date": "1996-01-01",
      "dataPoint": "Native Born, White Non-Hispanic",
      "dataType": "All Households by Nativity",
      "source": "W-2",
      "valueType": "count",
      "value": "73497839.33333",
      "rank": 4,
      "total": 5
    },
    {
      "id": 845,
      "date": "1996-01-01",
      "dataPoint": "Native Born, Minority",
      "dataType": "All Households by Nativity",
      "source": "W-2",
      "valueType": "count",
      "value": "15688421.00000",
      "rank": 3,
      "total": 5
    },
    {
      "id": 847,
      "date": "1996-01-01",
      "dataPoint": "Foreign-Born Non Citizen",
      "dataType": "All Households by Nativity",
      "source": "W-2",
      "valueType": "count",
      "value": "5647456.86667",
      "rank": 2,
      "total": 5
    },
    {
      "id": 846,
      "date": "1996-01-01",
      "dataPoint": "Foreign-Born Citizen",
      "dataType": "All Households by Nativity",
      "source": "W-2",
      "valueType": "count",
      "value": "3740990.16667",
      "rank": 1,
      "total": 5
    },
    {
      "id": 853,
      "date": "2016-01-01",
      "dataPoint": "Total",
      "dataType": "All Households by Nativity",
      "source": "W-2",
      "valueType": "count",
      "value": "124574774.16667",
      "rank": 5,
      "total": 5
    },
    {
      "id": 849,
      "date": "2016-01-01",
      "dataPoint": "Native Born, White Non-Hispanic",
      "dataType": "All Households by Nativity",
      "source": "W-2",
      "valueType": "count",
      "value": "80347957.66667",
      "rank": 4,
      "total": 5
    },
    {
      "id": 850,
      "date": "2016-01-01",
      "dataPoint": "Native Born, Minority",
      "dataType": "All Households by Nativity",
      "source": "W-2",
      "valueType": "count",
      "value": "25923476.00000",
      "rank": 3,
      "total": 5
    },
    {
      "id": 851,
      "date": "2016-01-01",
      "dataPoint": "Foreign-Born Citizen",
      "dataType": "All Households by Nativity",
      "source": "W-2",
      "valueType": "count",
      "value": "9693821.73333",
      "rank": 2,
      "total": 5
    },
    {
      "id": 852,
      "date": "2016-01-01",
      "dataPoint": "Foreign-Born Non Citizen",
      "dataType": "All Households by Nativity",
      "source": "W-2",
      "valueType": "count",
      "value": "8609518.76667",
      "rank": 1,
      "total": 5
    }
  ]
}

```

## Pagination

Pagination **SHOULD** be used by Collections to limit the number of resources returned at a time.

Pagination is requested by a client through the use of query parameters.

Requests will accept the following query parameters:

- limit: maximum number of items to return
- offset: starting position of the query in relation to the complete set of unpaginated items

A paginated response would look as follows:

```json
{
    "count": 1023,
    "next": "https://api.example.org/accounts/?limit=100&offset=500",
    "previous": "https://api.example.org/accounts/?limit=100&offset=300",
    "results": [
       …
    ]
}
```
#### Recommended Supporting Technologies

To achieve this, register a `DEFAULT_PAGINATION_CLASS` in your `local_settings/settings.py` to apply to all apps:

```python
REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 50
}
```

PAGE_SIZE is recommended to be between 50-100, depending on the size of resource object.

## Query Parameters

Query Parameters **MUST** include **ONLY** the following characters:

* `a-z` (lowercase only)
* `_` (underscore)

Query parameters that accept multiple values **MUST** be pluralized.

All query parameters **MUST** be properly [url-encoded](https://en.wikipedia.org/wiki/Percent-encoding#Current_standard). If a single query parameter value includes the comma (`,`) character, the comma **MUST** be double encoded.

> **Note:** For readability purposes, the examples throughout this document do not show encoded query strings.

#### Examples
Single value:
`GET /v1/apps?names=firstname`

Multiple values:
 `GET /v1/apps?names=firstname,secondname`

Single value with comma:
 `GET /v1/apps?names=comma%2Cname`

## Filtering

Filtering is the use of query parameters to return a subset of resources within a [Collection](#collections).

Filter query parameters **MUST** have names that conform to the acceptable [query parameter](#query-parameters) names.
Filter parameters **MUST** be able to be combined with other filters on the same collection.

When multiple filters are provided, the results **MUST** match all specified filters.

* All filters, including pagination filters should be available to the schema autogeneration

#### Examples

**Single value request**:
`GET /v1/apps?names=the_name`

This will return all apps with name `the_name`.

**Multiple value request**:
`GET /v1/apps?names=first_name,second_name`

This will return all apps with name `the_name` OR `second_name`.

**Combined filters**:
`GET /v1/apps?names=the_name&state=STARTED`

This will return all apps with name `the_name` AND state `STARTED`.

#### Recommended Supporting Technologies

* [django-filter](https://www.django-rest-framework.org/api-guide/filtering/#djangofilterbackend) and the DjangoFilterBackend is encouraged to be used.

* Create a [`get_schema_fields(self, view)`](https://www.django-rest-framework.org/api-guide/filtering/#pagination-schemas) method on a view in which you need to add fields to schema autogeneration (uses [CoreAPI](https://www.django-rest-framework.org/api-guide/schemas/#core-api)). May need to do this to add [pagination](#pagination) filters.


## Errors

### Status Codes

The HTTP status code returned for errors **MUST** be included in the documented [status codes](#response-codes).

## Aggregation

-- TODO

## GeoJSON

APIs will return valid GeoJSON as per [GeoJSON spec](https://geojson.org/)

Proper Field Types should be used for each Feature
  * Use points for individual Point Objects
  * Generally MultiPolygons should be avoided
    - https://gis.stackexchange.com/questions/225368/understanding-difference-between-polygon-and-multipolygon-for-shapefiles-in-qgis

Other related fields/data will be returned as Properties:

  ```json
  "properties": {
                 "firstProp": "value0",
                 "secondProp": {
                     "this": "that"
                 }
             }
  ```

Lists should be returned via "FeatureCollections":  

  ```json
    {
         "type": "FeatureCollection",
         "features": [{
             "type": "Feature",
             "geometry": {
                 "type": "Point",
                 "coordinates": [102.0, 0.5]
             },
             "properties": {
                 "firstProp": "value0"
             }
         }, {
             "type": "Feature",
             "geometry": {
                 "type": "LineString",
                 "coordinates": [
                     [102.0, 0.0],
                     [103.0, 1.0],
                     [104.0, 0.0],
                     [105.0, 1.0]
                 ]
             },
             "properties": {
                 "firstProp": "value0",
                 "secondProp": 0.0
             }
         }, {
             "type": "Feature",
             "geometry": {
                 "type": "Polygon",
                 "coordinates": [
                     [
                         [100.0, 0.0],
                         [101.0, 0.0],
                         [101.0, 1.0],
                         [100.0, 1.0],
                         [100.0, 0.0]
                     ]
                 ]
             },
             "properties": {
                 "firstProp": "value0",
                 "secondProp": {
                     "this": "that"
                 }
             }
         }]
     }
  ```
  * Standard Projection should be [EPSG:4326](https://spatialreference.org/ref/epsg/wgs-84/)

#### Recommended Supporting Technologies

* [djangorestframework-gis](https://github.com/djangonauts/django-rest-framework-gis) provides support for DRF for models, views, serializers, returning valid GeoJSON
* Use with [POSTGIS](https://postgis.net/) database and [Django PostGIS engine](https://docs.djangoproject.com/en/2.2/ref/contrib/gis/tutorial/#configure-settings-py)

## Documentation

Projects should include the following documentation:

* Basic README providing project summary, Hack Oregon intro, quickstart, installation, and contribution guidelines
* Formatted [docstrings](https://www.django-rest-framework.org/api-guide/schemas/#schemas-as-documentation) on classes and methods
* Swagger UI frontend
* Published OpenAPI schema
