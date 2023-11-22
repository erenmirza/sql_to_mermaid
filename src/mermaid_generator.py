import sys
from sqlglot import parse_one, exp

def generate_mermaid_code(sql_file_path, output_file_path):
    with open(sql_file_path, "r") as sql_file:
        query = sql_file.read()
        # print(query)

    dependencies = {}

    for cte in parse_one(query).find_all(exp.CTE):
        dependencies[cte.alias_or_name] = []

        cte_query = cte.this.sql()
        for table in parse_one(cte_query).find_all(exp.Table):
            dependencies[cte.alias_or_name].append(table.name)

    # Generate Mermaid code
    nodes = "\n".join([f'{cte}["{cte}"]' for cte in dependencies])
    edges = "\n".join([f'{target} --> {source}' for source, targets in dependencies.items() for target in targets])

    mermaid_code = f"""```mermaid
graph LR;

{nodes}

{edges}
```"""

    # Write to a Markdown file
    with open(output_file_path, "w") as output_file:
        output_file.write(mermaid_code)

    print(f"Mermaid code written to {output_file_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <sql_file_path>")
        sys.exit(1)

    sql_file_path = sys.argv[1]
    output_file_path = sys.argv[2]
    generate_mermaid_code(sql_file_path, output_file_path)