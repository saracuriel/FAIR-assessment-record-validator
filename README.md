# FAIR-assessment-record-validator

### Embedded SHACL Validator API

A lightweight **FastAPI-based SHACL validation service** for validating RDF data (Turtle) against predefined SHACL shapes.  

The service embeds SHACL schemas directly in code and delegates validation to an external SHACL engine (`rudof`), returning a structured validation report.

## Endpoints

All endpoints accept RDF as raw text (text/plain):

POST /validate/test/turtle

POST /validate/testResult/turtle

POST /validate/testResultSet/turtle

POST /validate/metric/turtle

POST /validate/benchmark/turtle


## Example

```bash
curl -X POST http://localhost:8000/validate/test/turtle \
  -H "Content-Type: text/plain" \
  --data-binary @example.ttl
```

## Execution

Use Docker:


```bash
docker run -p 8000:8000 pabloalarconm/fair-assessment-record-validator:0.2.1
```

Also, you can use Docker Compose:

```bash
version: "3.8"

services:
  api:
    image: pabloalarconm/fair-assessment-record-validator:0.2.1
    ports:
      - "8000:8000"
```