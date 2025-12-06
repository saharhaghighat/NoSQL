from neo4j import GraphDatabase


def get_filtered_paginated_movies(page_number, page_size):
    query = """
    MATCH (m:Movie)-[:HAS_GENRE]->(g:Genre)
    WITH g.name as genre_name , avg(m.score) AS average_rating
    ORDER BY average_rating DESC
    SKIP $skip
    LIMIT $limit
    RETURN genre_name, average_rating
    """

    uri = "bolt://localhost:7687"
    user = "neo4j"
    password = "password"

    skip = (page_number - 1) * page_size
    limit = page_size

    with GraphDatabase.driver(uri, auth=(user, password)) as driver:
        with driver.session() as session:
            result = session.run(query, skip=skip, limit=limit)
            return [{"Genre": record[0], "AverageRating": record[0]} for record in result.values()]