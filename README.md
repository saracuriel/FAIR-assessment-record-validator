# FAIR-assessment-record-validator

### Embedded SHACL Validator API

A lightweight **FastAPI-based SHACL validation service** for validating RDF data (Turtle or JSON-LD) against predefined SHACL shapes.  

The service embeds SHACL schemas directly in code and delegates validation to an external SHACL engine (`rudof`), returning a structured validation report.

## Endpoints

**Turtle** endpoints, accepted as raw text (`text/plain`):

* POST /validate/test/turtle

* POST /validate/testResult/turtle

* POST /validate/testResultSet/turtle

* POST /validate/metric/turtle

* POST /validate/benchmark/turtle

* POST /validate/scoringAlgorithm/turtle

* POST /validate/benchmarkScore/turtle

**JSON-LD** endpoints, accepted as `application/json`:

* POST /validate/test/jsonld

* POST /validate/testResult/jsonld

* POST /validate/testResultSet/jsonld

* POST /validate/metric/jsonld

* POST /validate/benchmark/jsonld

* POST /validate/scoringAlgorithm/jsonld

* POST /validate/benchmarkScore/jsonld


## Example

```bash
curl -X POST http://localhost:8000/validate/test/turtle \
  -H "Content-Type: text/plain" \
  --data-binary @example.ttl
```

## Execution

Use Docker:


```bash
docker run -p 8000:8000 saracuriel/far-validator:0.0.1
```

Also, you can use Docker Compose:

```bash
version: "3.8"

services:
  api:
    image: saracuriel/far-validator:0.0.1
    ports:
      - "8000:8000"
```

You can access the execution endpoints from FastAPI by entering http://localhost:8000/validate/docs in your browser.
