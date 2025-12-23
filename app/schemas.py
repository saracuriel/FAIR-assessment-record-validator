# schemas.py

TEST_SHACL = """
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix ftr: <https://w3id.org/ftr#> .
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix sio: <http://semanticscience.org/resource/> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix adms: <http://www.w3.org/ns/adms#> .
@prefix vivo: <http://vivoweb.org/ontology/core#> .
@prefix doap: <http://usefulinc.com/ns/doap#> .
@prefix dqv: <http://www.w3.org/ns/dqv#> .
@prefix vcard: <http://www.w3.org/2006/vcard/ns#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix : <http://www.example.org/me#> .
@prefix dpv: <https://w3id.org/dpv#> .

:OrganizationShape
    a sh:NodeShape ;
    sh:nodeKind sh:IRI ;
    sh:targetClass vcard:Organization ;

    sh:property [
        sh:path vcard:organization-name ;
        sh:or (
            [ sh:datatype xsd:string ]
            [ sh:datatype rdf:langString ]
        ) ;
    ] .

:IndividualShape
    a sh:NodeShape ;
    sh:nodeKind sh:IRI ;
    sh:targetClass vcard:Individual ;

    sh:property [
        sh:path vcard:fn ;
        sh:or (
            [ sh:datatype xsd:string ]
            [ sh:datatype rdf:langString ]
        ) ;
    ] ;

    sh:property [
        sh:path vcard:hasEmail ;
        sh:nodeKind sh:IRI ;
    ] .

:MetricShape
    a sh:NodeShape ;
    sh:nodeKind sh:IRI ;
    sh:targetClass ftr:Metric .

:TestShape
    a sh:NodeShape ;
    sh:nodeKind sh:IRI ;
    sh:targetClass ftr:Test ;

    sh:property [
        sh:path rdf:type ;
        sh:hasValue ftr:Test ;
        sh:minCount 1 ;
    ] ;

    sh:property [
        sh:path dcterms:identifier ;
        sh:or (
            [ sh:datatype xsd:string ]
            [ sh:datatype rdf:langString ]
        ) ;
        sh:minCount 1 ;
    ] ;

    sh:property [
        sh:path dcterms:title ;
        sh:or (
            [ sh:datatype xsd:string ]
            [ sh:datatype rdf:langString ]
        ) ;
        sh:minCount 1 ;
    ] ;

    sh:property [
        sh:path dcterms:description ;
        sh:or (
            [ sh:datatype xsd:string ]
            [ sh:datatype rdf:langString ]
        ) ;
        sh:minCount 1 ;
    ] ;

    sh:property [
        sh:path dcat:keyword ;
        sh:or (
            [ sh:datatype xsd:string ]
            [ sh:datatype rdf:langString ]
        ) ;
    ] ;

    sh:property [
        sh:path vivo:abbreviation ;
        sh:or (
            [ sh:datatype xsd:string ]
            [ sh:datatype rdf:langString ]
        ) ;
    ] ;

    sh:property [
        sh:path dcat:endpointDescription ;
        sh:nodeKind sh:IRI ;
    ] ;

    sh:property [
        sh:path dcat:endpointURL ;
        sh:nodeKind sh:IRI ;
    ] ;

    sh:property [
        sh:path doap:repository ;
        sh:nodeKind sh:IRI ;
    ] ;

    sh:property [
        sh:path dcterms:type ;
        sh:nodeKind sh:IRI ;
    ] ;

    sh:property [
        sh:path dcterms:license ;
        sh:nodeKind sh:IRI ;
        sh:minCount 1 ;
        sh:maxCount 1 ;
    ] ;

    sh:property [
        sh:path ftr:applicationArea ;
        sh:nodeKind sh:IRI ;
    ] ;

    sh:property [
        sh:path dcat:version ;
        sh:or (
            [ sh:datatype xsd:string ]
            [ sh:datatype rdf:langString ]
        ) ;
        sh:minCount 1 ;
        sh:maxCount 1 ;
    ] ;

    sh:property [
        sh:path adms:versionNotes ;
        sh:or (
            [ sh:datatype xsd:string ]
            [ sh:datatype rdf:langString ]
        ) ;
    ] ;

    sh:property [
        sh:path ftr:status ;
        sh:or (
            [ sh:datatype xsd:string ]
            [ sh:datatype rdf:langString ]
        ) ;
        sh:maxCount 1 ;
    ] ;

    sh:property [
        sh:path dcat:contactPoint ;
        sh:minCount 1 ;
        sh:or (
        [
            sh:nodeKind sh:IRI ;
            sh:node :OrganizationShape
        ]
        [
            sh:nodeKind sh:IRI ;
            sh:node :IndividualShape
        ]
        ) ;
    ] ;

    sh:property [
        sh:path dcterms:creator ;
        sh:or (
        [
            sh:nodeKind sh:IRI ;
            sh:node :OrganizationShape
        ]
        [
            sh:nodeKind sh:IRI ;
            sh:node :IndividualShape
        ]
        ) ;
    ] ;

    sh:property [
        sh:path dcat:publisher ;
        sh:or (
        [
            sh:nodeKind sh:IRI ;
            sh:node :OrganizationShape
        ]
        [
            sh:nodeKind sh:IRI ;
            sh:node :IndividualShape
        ]
        ) ;
    ] ;

    sh:property [
        sh:path sio:SIO_000233 ;
        sh:node :MetricShape ;
        sh:minCount 1 ;
    ] ;

    sh:property [
        sh:path ftr:supportedBy ;
        sh:nodeKind sh:IRI ;
    ] ;

    sh:property [
        sh:path dpv:isApplicableFor ;
        sh:nodeKind sh:IRI ;
    ] .
"""

TESTRESULT_SHACL = """
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix ftr: <https://w3id.org/ftr#> .
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix sio: <http://semanticscience.org/resource/> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix adms: <http://www.w3.org/ns/adms#> .
@prefix vivo: <http://vivoweb.org/ontology/core#> .
@prefix doap: <http://usefulinc.com/ns/doap#> .
@prefix dqv: <http://www.w3.org/ns/dqv#> .
@prefix vcard: <http://www.w3.org/2006/vcard/ns#> .
@prefix dpv: <https://w3id.org/dpv#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix : <http://www.example.org/me#> .

:TestShape
    a sh:NodeShape ;
    sh:nodeKind sh:IRI ;
    sh:targetClass ftr:Test .

:EntityShape
    a sh:NodeShape ;
    sh:nodeKind sh:IRI ;
    sh:targetClass prov:Entity ;
    sh:property [
        sh:path dcterms:identifier ;
        sh:or (
            [ sh:datatype xsd:string ]
            [ sh:datatype rdf:langString ]
        ) ;
    ] .

:TestResultShape
    a sh:NodeShape ;
    sh:nodeKind sh:IRI ;
    sh:targetClass ftr:TestResult ;
    sh:property [
        sh:path dcterms:identifier ;
        sh:or (
            [ sh:datatype xsd:string ]
            [ sh:datatype rdf:langString ]
        ) ;
        sh:minCount 1 ;
    ] ;
    sh:property [
        sh:path dcterms:title ;
        sh:or (
            [ sh:datatype xsd:string ]
            [ sh:datatype rdf:langString ]
        ) ;
        sh:minCount 1 ;
    ] ;
    sh:property [
        sh:path dcterms:description ;
        sh:or (
            [ sh:datatype xsd:string ]
            [ sh:datatype rdf:langString ]
        ) ;
        sh:minCount 1 ;
    ] ;
    sh:property [
        sh:path dcterms:license ;
        sh:nodeKind sh:IRI ;
        sh:minCount 1 ;
    ] ;
    sh:property [
        sh:path prov:value ;
        sh:or (
            [ sh:datatype xsd:string ]
            [ sh:datatype rdf:langString ]
        ) ;
        sh:minCount 1 ;
    ] ;
    sh:property [
        sh:path ftr:log ;
        sh:or (
            [ sh:datatype xsd:string ]
            [ sh:datatype rdf:langString ]
        ) ;
        sh:minCount 1 ;
    ] ;
    sh:property [
        sh:path ftr:completion ;
        sh:datatype xsd:integer ;
    ] ;
    sh:property [
        sh:path ftr:affectedElements ;
        sh:nodeKind sh:IRI ;
    ] ;
    sh:property [
        sh:path ftr:outputFromTest ;
        sh:node :TestShape ;
        sh:minCount 1 ;
    ] ;
    sh:property [
        sh:path ftr:assessmentTarget ;
        sh:node :EntityShape ;
        sh:minCount 1 ;
    ] ;
    sh:property [
        sh:path prov:wasGeneratedBy ;
        sh:node :TestExecutionActivityShape ;
    ] ;
    sh:property [
        sh:path ftr:suggestion ;
        sh:node :GuidanceShape ;
        sh:minCount 1 ;
    ] .

:TestExecutionActivityShape
    a sh:NodeShape ;
    sh:nodeKind sh:IRI ;
    sh:targetClass ftr:TestExecutionActivity ;
    sh:property [
        sh:path prov:used ;
        sh:node :EntityShape ;
        sh:maxCount 1 ;
    ] ;
    sh:property [
        sh:path prov:wasAssociatedWith ;
        sh:node :TestShape ;
    ] ;
    sh:property [
        sh:path prov:endedAtTime ;
        sh:datatype xsd:dateTime ;
        sh:minCount 1 ;
    ] .

:GuidanceShape
    a sh:NodeShape ;
    sh:nodeKind sh:IRI ;
    sh:targetClass ftr:GuidanceContext ;
    sh:property [
        sh:path dcterms:title ;
        sh:or (
            [ sh:datatype xsd:string ]
            [ sh:datatype rdf:langString ]
        ) ;
        sh:minCount 1 ;
    ] ;
    sh:property [
        sh:path dcterms:description ;
        sh:or (
            [ sh:datatype xsd:string ]
            [ sh:datatype rdf:langString ]
        ) ;
        sh:minCount 1 ;
    ] ;
    sh:property [
        sh:path sio:SIO_000339 ;
        sh:nodeKind sh:IRI ;
    ] .

"""

TESTRESULTSET_SHACL = """
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix ftr: <https://w3id.org/ftr#> .
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix sio: <http://semanticscience.org/resource/> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix adms: <http://www.w3.org/ns/adms#> .
@prefix vivo: <http://vivoweb.org/ontology/core#> .
@prefix doap: <http://usefulinc.com/ns/doap#> .
@prefix dqv: <http://www.w3.org/ns/dqv#> .
@prefix vcard: <http://www.w3.org/2006/vcard/ns#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix : <http://www.example.org/me#> .
@prefix dpv: <https://w3id.org/dpv#> .

:TestResultSetShape
    a sh:NodeShape ;
    sh:nodeKind sh:IRI ;
    sh:targetClass ftr:TestResultSet ;

    sh:property [
        sh:path dcterms:identifier ;
        sh:or (
            [ sh:datatype xsd:string ]
            [ sh:datatype rdf:langString ]
        ) ;
        sh:minCount 1 ;
    ] ;

    sh:property [
        sh:path dcterms:title ;
        sh:or (
            [ sh:datatype xsd:string ]
            [ sh:datatype rdf:langString ]
        ) ;
        sh:minCount 1 ;
    ] ;

    sh:property [
        sh:path dcterms:license ;
        sh:nodeKind sh:IRI ;
        sh:minCount 1 ;
    ] ;

    sh:property [
        sh:path prov:wasGeneratedBy ;
        sh:node :TestExecutionActivityShape ;
        sh:minCount 1 ;
    ] ;

    sh:property [
        sh:path ftr:assessmentTarget ;
        sh:node :EntityShape ;
        sh:minCount 1 ;
    ] ;

    sh:property [
        sh:path prov:hadMember ;
        sh:node :TestResultShape ;
        sh:minCount 1 ;
    ] .

:TestShape
    a sh:NodeShape ;
    sh:nodeKind sh:IRI ;

    sh:property [
        sh:path rdf:type ;
        sh:hasValue ftr:Test ;
        sh:minCount 1 ;
    ] .

:EntityShape
    a sh:NodeShape ;
    sh:nodeKind sh:IRI ;
    sh:targetClass prov:Entity ;

    sh:property [
        sh:path dcterms:identifier ;
        sh:or (
            [ sh:datatype xsd:string ]
            [ sh:datatype rdf:langString ]
        ) ;
    ] .

:TestResultShape
    a sh:NodeShape ;
    sh:nodeKind sh:IRI ;
    sh:targetClass ftr:TestResult ;

    sh:property [
        sh:path dcterms:identifier ;
        sh:or (
            [ sh:datatype xsd:string ]
            [ sh:datatype rdf:langString ]
        ) ;
        sh:minCount 1 ;
    ] ;

    sh:property [
        sh:path dcterms:title ;
        sh:or (
            [ sh:datatype xsd:string ]
            [ sh:datatype rdf:langString ]
        ) ;
        sh:minCount 1 ;
    ] ;

    sh:property [
        sh:path dcterms:description ;
        sh:or (
            [ sh:datatype xsd:string ]
            [ sh:datatype rdf:langString ]
        ) ;
        sh:minCount 1 ;
    ] ;

    sh:property [
        sh:path dcterms:license ;
        sh:nodeKind sh:IRI ;
        sh:minCount 1 ;
    ] ;

    sh:property [
        sh:path prov:value ;
        sh:or (
            [ sh:datatype xsd:string ]
            [ sh:datatype rdf:langString ]
        ) ;
        sh:minCount 1 ;
        sh:maxCount 1 ;
    ] ;

    sh:property [
        sh:path ftr:log ;
        sh:or (
            [ sh:datatype xsd:string ]
            [ sh:datatype rdf:langString ]
        ) ;
        sh:minCount 1 ;
        sh:maxCount 1 ;
    ] ;

    sh:property [
        sh:path ftr:completion ;
        sh:datatype xsd:integer ;
    ] ;

    sh:property [
        sh:path ftr:affectedElements ;
        sh:nodeKind sh:IRI ;
    ] ;

    sh:property [
        sh:path ftr:outputFromTest ;
        sh:node :TestShape ;
        sh:minCount 1 ;
    ] ;

    sh:property [
        sh:path ftr:assessmentTarget ;
        sh:node :EntityShape ;
        sh:minCount 1 ;
    ] ;

    sh:property [
        sh:path prov:wasGeneratedBy ;
        sh:node :TestExecutionActivityShape ;
    ] ;

    sh:property [
        sh:path ftr:suggestion ;
        sh:node :GuidanceShape ;
        sh:minCount 1 ;
    ] .

:TestExecutionActivityShape
    a sh:NodeShape ;
    sh:nodeKind sh:IRI ;
    sh:targetClass ftr:TestExecutionActivity ;

    sh:property [
        sh:path prov:used ;
        sh:node :EntityShape ;
    ] ;

    sh:property [
        sh:path prov:wasAssociatedWith ;
        sh:node :TestShape ;
    ] ;

    sh:property [
        sh:path prov:endedAtTime ;
        sh:datatype xsd:dateTime ;
        sh:minCount 1 ;
        sh:maxCount 1 ;
    ] .

:GuidanceShape
    a sh:NodeShape ;
    sh:nodeKind sh:IRI ;
    sh:targetClass ftr:GuidanceContext ;

    sh:property [
        sh:path dcterms:title ;
        sh:or (
            [ sh:datatype xsd:string ]
            [ sh:datatype rdf:langString ]
        ) ;
        sh:minCount 1 ;
    ] ;

    sh:property [
        sh:path dcterms:description ;
        sh:or (
            [ sh:datatype xsd:string ]
            [ sh:datatype rdf:langString ]
        ) ;
        sh:minCount 1 ;
    ] .

"""

METRIC_SHACL = """
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix ftr: <https://w3id.org/ftr#> .
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix sio: <http://semanticscience.org/resource/> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix vivo: <http://vivoweb.org/ontology/core#> .
@prefix dqv: <http://www.w3.org/ns/dqv#> .
@prefix vcard: <http://www.w3.org/2006/vcard/ns#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix dpv: <https://w3id.org/dpv#> .
@prefix : <http://www.example.org/me#> .

:OrganizationShape
    a sh:NodeShape ;
    sh:targetClass vcard:Organization ;
    sh:nodeKind sh:IRI ;

    sh:property [
        sh:path vcard:organization-name ;
        sh:nodeKind xsd:string ;
    ] .

:IndividualShape
    a sh:NodeShape ;
    sh:targetClass vcard:Individual ;
    sh:nodeKind sh:IRI ;

    sh:property [
        sh:path vcard:fn ;
        sh:or (
            [ sh:datatype xsd:string ]
            [ sh:datatype rdf:langString ]
        ) ;
    ] ;

    sh:property [
        sh:path vcard:hasEmail ;
        sh:nodeKind sh:IRI ;
    ] .

:BenchmarkShape
    a sh:NodeShape ;
    sh:targetClass ftr:Benchmark ;
    sh:nodeKind sh:IRI .

:DimensionShape
    a sh:NodeShape ;
    sh:targetClass dqv:Dimension ;
    sh:nodeKind sh:IRI .

:TestShape
    a sh:NodeShape ;
    sh:targetClass ftr:Test ;
    sh:nodeKind sh:IRI .

:MetricShape
    a sh:NodeShape ;
    sh:targetClass ftr:Metric ;
    sh:nodeKind sh:IRI ;

    sh:property [
        sh:path dcterms:identifier ;
        sh:or (
            [ sh:datatype xsd:string ]
            [ sh:datatype rdf:langString ]
        ) ;
        sh:minCount 1 ;
    ] ;

    sh:property [
        sh:path dcterms:title ;
        sh:nodeKind xsd:string ;
        sh:minCount 1 ;
    ] ;

    sh:property [
        sh:path dcterms:description ;
        sh:nodeKind xsd:string ;
        sh:minCount 1 ;
    ] ;

    sh:property [
        sh:path dcat:keyword ;
        sh:nodeKind xsd:string ;
    ] ;

    sh:property [
        sh:path dqv:inDimension ;
        sh:node :DimensionShape ;
    ] ;

    sh:property [
        sh:path vivo:abbreviation ;
        sh:nodeKind xsd:string ;
    ] ;

    sh:property [
        sh:path dcat:landingPage ;
        sh:nodeKind sh:IRI ;
    ] ;

    sh:property [
        sh:path dcat:version ;
        sh:nodeKind xsd:string ;
        sh:minCount 1 ;
        sh:maxCount 1 ;
    ] ;

    sh:property [
        sh:path ftr:applicationArea ;
        sh:nodeKind sh:IRI ;
    ] ;

    sh:property [
        sh:path ftr:status ;
        sh:nodeKind xsd:string ;
    ] ;

    sh:property [
        sh:path ftr:hasBenchmark ;
        sh:node :BenchmarkShape ;
    ] ;

    sh:property [
        sh:path dcat:contactPoint ;
        sh:minCount 1 ;
        sh:or (
        [
            sh:nodeKind sh:IRI ;
            sh:node :OrganizationShape
        ]
        [
            sh:nodeKind sh:IRI ;
            sh:node :IndividualShape
        ]
        ) ;
    ] ;

    sh:property [
        sh:path dcterms:creator ;
        sh:or (
        [
            sh:nodeKind sh:IRI ;
            sh:node :OrganizationShape
        ]
        [
            sh:nodeKind sh:IRI ;
            sh:node :IndividualShape
        ]
        ) ;
    ] ;

    sh:property [
        sh:path dcat:publisher ;
        sh:or (
        [
            sh:nodeKind sh:IRI ;
            sh:node :OrganizationShape
        ]
        [
            sh:nodeKind sh:IRI ;
            sh:node :IndividualShape
        ]
        ) ;
    ] ;

    sh:property [
        sh:path ftr:hasPositiveValidation ;
        sh:nodeKind sh:IRI ;
    ] ;

    sh:property [
        sh:path ftr:hasNegativeValidation ;
        sh:nodeKind sh:IRI ;
    ] ;

    sh:property [
        sh:path ftr:supportedBy ;
        sh:nodeKind sh:IRI ;
    ] ;

    sh:property [
        sh:path dpv:isApplicableFor ;
        sh:nodeKind sh:IRI ;
    ] ;

    sh:property [
        sh:path sio:SIO_000234 ;
        sh:node :TestShape ;
    ] .

"""

BENCHMARK_SHACL = """
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix ftr: <https://w3id.org/ftr#> .
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix sio: <http://semanticscience.org/resource/> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix vivo: <http://vivoweb.org/ontology/core#> .
@prefix dqv: <http://www.w3.org/ns/dqv#> .
@prefix vcard: <http://www.w3.org/2006/vcard/ns#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix : <http://www.example.org/me#> .

:OrganizationShape
    a sh:NodeShape ;
    sh:nodeKind sh:IRI ;
    sh:targetClass vcard:Organization ;

    sh:property [
        sh:path vcard:organization-name ;
        sh:or (
            [ sh:datatype xsd:string ]
            [ sh:datatype rdf:langString ]
        ) ;
        sh:minCount 1 ;
    ] .

:IndividualShape
    a sh:NodeShape ;
    sh:nodeKind sh:IRI ;
    sh:targetClass vcard:Individual ;

    sh:property [
        sh:path vcard:fn ;
        sh:or (
            [ sh:datatype xsd:string ]
            [ sh:datatype rdf:langString ]
        ) ;
        sh:minCount 1 ;
    ] ;

    sh:property [
        sh:path vcard:hasEmail ;
        sh:nodeKind sh:IRI ;
        sh:minCount 1 ;
    ] .

:MetricShape
    a sh:NodeShape ;
    sh:nodeKind sh:IRI ;
    sh:targetClass ftr:Metric .

:ScoringAlgorithmShape
    a sh:NodeShape ;
    sh:nodeKind sh:IRI ;

    sh:property [
        sh:path rdf:type ;
        sh:hasValue ftr:ScoringAlgorithm ;
        sh:minCount 1 ;
    ] .

:BenchmarkShape
    a sh:NodeShape ;
    sh:nodeKind sh:IRI ;
    sh:targetClass ftr:Benchmark ;

    sh:property [
        sh:path dcterms:identifier ;
        sh:or (
            [ sh:datatype xsd:string ]
            [ sh:datatype rdf:langString ]
        ) ;
        sh:minCount 1 ;
    ] ;

    sh:property [
        sh:path dcterms:title ;
        sh:or (
            [ sh:datatype xsd:string ]
            [ sh:datatype rdf:langString ]
        ) ;
        sh:minCount 1 ;
    ] ;

    sh:property [
        sh:path dcterms:description ;
        sh:or (
            [ sh:datatype xsd:string ]
            [ sh:datatype rdf:langString ]
        ) ;
        sh:minCount 1 ;
    ] ;

    sh:property [
        sh:path dcat:keyword ;
        sh:or (
            [ sh:datatype xsd:string ]
            [ sh:datatype rdf:langString ]
        ) ;
    ] ;

    sh:property [
        sh:path vivo:abbreviation ;
        sh:or (
            [ sh:datatype xsd:string ]
            [ sh:datatype rdf:langString ]
        ) ;
    ] ;

    sh:property [
        sh:path dcat:landingPage ;
        sh:nodeKind sh:IRI ;
    ] ;

    sh:property [
        sh:path dcat:version ;
        sh:or (
            [ sh:datatype xsd:string ]
            [ sh:datatype rdf:langString ]
        ) ;
        sh:minCount 1 ;
        sh:maxCount 1 ;
    ] ;

    sh:property [
        sh:path ftr:applicationArea ;
        sh:nodeKind sh:IRI ;
    ] ;

    sh:property [
        sh:path ftr:status ;
        sh:or (
            [ sh:datatype xsd:string ]
            [ sh:datatype rdf:langString ]
        ) ;
    ] ;

    sh:property [
        sh:path ftr:hasAssociatedMetric ;
        sh:node :MetricShape ;
        sh:minCount 1 ;
    ] ;

    sh:property [
        sh:path dcat:contactPoint ;
        sh:minCount 1 ;
        sh:or (
        [
            sh:nodeKind sh:IRI ;
            sh:node :OrganizationShape
        ]
        [
            sh:nodeKind sh:IRI ;
            sh:node :IndividualShape
        ]
        ) ;
    ] ;

    sh:property [
        sh:path dcterms:creator ;
        sh:or (
        [
            sh:nodeKind sh:IRI ;
            sh:node :OrganizationShape
        ]
        [
            sh:nodeKind sh:IRI ;
            sh:node :IndividualShape
        ]
        ) ;
    ] ;

    sh:property [
        sh:path dcat:publisher ;
        sh:or (
        [
            sh:nodeKind sh:IRI ;
            sh:node :OrganizationShape
        ]
        [
            sh:nodeKind sh:IRI ;
            sh:node :IndividualShape
        ]
        ) ;
    ] ;

    sh:property [
        sh:path sio:SIO_000234 ;
        sh:node :ScoringAlgorithmShape ;
    ] .

"""

SHACL_SCHEMAS = {
    "test": TEST_SHACL,
    "testResult": TESTRESULT_SHACL,
    "testResultSet": TESTRESULTSET_SHACL,
    "metric": METRIC_SHACL,
    "benchmark": BENCHMARK_SHACL
}
