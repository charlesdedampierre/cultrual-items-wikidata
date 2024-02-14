"""from models import WikidataEntity, ComplexityObject

# load json

# insert in the entities

# create instances of WikidataEntity for each entity in the JSON
entity1 = WikidataEntity(id="http://www.wikidata.org/entity/Q220659", label="archaeological artifact")
entity2 = WikidataEntity(id="http://www.wikidata.org/entity/Q860861", label="sculpture")
entity3 = WikidataEntity(id="http://www.wikidata.org/entity/Q220659", label="archaeological artifact")
time_period = WikidataEntity(id="http://www.wikidata.org/entity/Q11772", label="Ancient Greece")
culture = WikidataEntity(id="http://www.wikidata.org/entity/Q11772", label="Ancient Greece")
creator = WikidataEntity(id="http://www.wikidata.org/.well-known/genid/e6025332e49d116c7e0e17eb8412d211", label="http://www.wikidata.org/.well-known/genid/e6025332e49d116c7e0e17eb8412d211")

# create a ComplexityObject instance and add the entities to its fields
complexity_object = ComplexityObject(
    instance=entity1,
    inception="-0129-01-01T00:00:00Z",
    time_period=time_period,
    culture=culture,
    creator=creator

    import sqlite3

    conn = sqlite3.connect("../cultura.db")

    region = pd.read_sql_query("SELECT * FROM birthcity_information", conn)
    region = region[["countryLabel", "country_id"]].drop_duplicates()

"""
