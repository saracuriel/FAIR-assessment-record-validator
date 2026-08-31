from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel
import subprocess
import tempfile
import os
from rdflib import Graph, Namespace
from rdflib.namespace import RDF
import json
from .schemas import SHACL_SCHEMAS

app = FastAPI(title="Embedded SHACL Validator",
            docs_url="/validate/docs",
            redoc_url=None,
            openapi_url="/validate/openapi.json",
)

SH = Namespace("http://www.w3.org/ns/shacl#")

# ----------------- Helper -----------------

def validate_rdf(rdf_data: str, data_format: str, schema_name: str):
    if schema_name not in SHACL_SCHEMAS:
        raise HTTPException(status_code=404, detail="Unknown SHACL schema")

    shapes_ttl = SHACL_SCHEMAS[schema_name]

    with tempfile.TemporaryDirectory() as tmpdir:
        data_file = os.path.join(tmpdir, "data.rdf")
        shapes_file = os.path.join(tmpdir, "shapes.ttl")

        with open(data_file, "w") as f:
            f.write(rdf_data)

        with open(shapes_file, "w") as f:
            f.write(shapes_ttl)

        cmd = [
            "rudof", "validate",
            "--mode", "shacl",
            "--data-format", data_format,
            "--schema-format", "turtle",
            "--result-format", "turtle",
            data_file,
            "--schema", shapes_file
        ]

        try:
            result = subprocess.run(
                cmd, capture_output=True, text=True, check=True
            )

            g = Graph()
            g.parse(data=result.stdout, format="turtle")

            report = next(g.subjects(RDF.type, SH.ValidationReport), None)
            conforms = bool(next(g.objects(report, SH.conforms), False))

            results = []
            for res in g.objects(report, SH.result):
                results.append({
                    "focusNode": str(next(g.objects(res, SH.focusNode), None)),
                    "path": str(next(g.objects(res, SH.resultPath), None)),
                    "message": str(next(g.objects(res, SH.resultMessage), None)),
                    "severity": str(next(g.objects(res, SH.resultSeverity), None)),
                    "value": str(next(g.objects(res, SH.value), None)),
                })

            return {"schema": schema_name, "conforms": conforms, "results": results}

        except subprocess.CalledProcessError as e:
            raise HTTPException(status_code=400, detail=e.stderr)


# ----------------- API Endpoints -----------------

@app.get("/validate/", summary="Health check", description="Verify that the API is running correctly.")
async def health_check():
    return {
        "status": "ok",
        "message": "API is running. See /validate/docs for interactive documentation.",
    }
############### Turtle #################

@app.post("/validate/test/turtle",
        summary="Validate your Turtle against SHACL-compliant FTR model")
def validate_test_turtle(data: str = Body(..., media_type="text/plain")):
    return validate_rdf(data, "turtle", "test")

@app.post("/validate/testResult/turtle",
        summary="Validate your Turtle against SHACL-compliant FTR model")
def validate_testResult_turtle(data: str = Body(..., media_type="text/plain")):
    return validate_rdf(data, "turtle", "testResult")

@app.post("/validate/testResultSet/turtle",
        summary="Validate your Turtle against SHACL-compliant FTR model")
def validate_testResultSet_turtle(data: str = Body(..., media_type="text/plain")):
    return validate_rdf(data, "turtle", "testResultSet")

@app.post("/validate/metric/turtle",
        summary="Validate your Turtle against SHACL-compliant FTR model")
def validate_metric_turtle(data: str = Body(..., media_type="text/plain")):
    return validate_rdf(data, "turtle", "metric")

@app.post("/validate/benchmark/turtle",
        summary="Validate your Turtle against SHACL-compliant FTR model")
def validate_benchmark_turtle(data: str = Body(..., media_type="text/plain")):
    return validate_rdf(data, "turtle", "benchmark")

@app.post("/validate/scoringAlgorithm/turtle",
        summary="Validate your Turtle against SHACL-compliant FTR model")
def validate_scoringAlgorithm_turtle(data: str = Body(..., media_type="text/plain")):
    return validate_rdf(data, "turtle", "scoringAlgorithm")

@app.post("/validate/benchmarkScore/turtle",
        summary="Validate your Turtle against SHACL-compliant FTR model")
def validate_benchmarkScore_turtle(data: str = Body(..., media_type="text/plain")):
    return validate_rdf(data, "turtle", "benchmarkScore")

############### JSON-LD #################

@app.post("/validate/test/jsonld",
        summary="Validate your JSON-LD against SHACL-compliant FTR model",
        description="""Remove the described existing example input and paste your JSON-LD metadata""")
def validate_test_jsonld(data: dict):
    return validate_rdf(json.dumps(data), "jsonld", "test")

@app.post("/validate/testResult/jsonld",
        summary="Validate your JSON-LD against SHACL-compliant FTR model",
        description="""Remove the described existing example input and paste your JSON-LD metadata""")
def validate_testResult_jsonld(data: dict):
    return validate_rdf(json.dumps(data), "jsonld", "testResult")

@app.post("/validate/testResultSet/jsonld",
        summary="Validate your JSON-LD against SHACL-compliant FTR model",
        description="""Remove the described existing example input and paste your JSON-LD metadata""")
def validate_testResultSet_jsonld(data: dict):
    return validate_rdf(json.dumps(data), "jsonld", "testResultSet")

@app.post("/validate/metric/jsonld",
        summary="Validate your JSON-LD against SHACL-compliant FTR model",
        description="""Remove the described existing example input and paste your JSON-LD metadata""")
def validate_metric_jsonld(data: dict):
    return validate_rdf(json.dumps(data), "jsonld", "metric")

@app.post("/validate/benchmark/jsonld",
        summary="Validate your JSON-LD against SHACL-compliant FTR model",
        description="""Remove the described existing example input and paste your JSON-LD metadata""")
def validate_benchmark_jsonld(data: dict):
    return validate_rdf(json.dumps(data), "jsonld", "benchmark")

@app.post("/validate/scoringAlgorithm/jsonld",
        summary="Validate your JSON-LD against SHACL-compliant FTR model",
        description="""Remove the described existing example input and paste your JSON-LD metadata""")
def validate_scoringAlgorithm_jsonld(data: dict):
    return validate_rdf(json.dumps(data), "jsonld", "scoringAlgorithm")


@app.post("/validate/benchmarkScore/jsonld",
        summary="Validate your JSON-LD against SHACL-compliant FTR model",
        description="""Remove the described existing example input and paste your JSON-LD metadata""")
def validate_benchmarkScore_jsonld(data: dict):
    return validate_rdf(json.dumps(data), "jsonld", "benchmarkScore")
