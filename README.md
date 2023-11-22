# sql_to_mermaid
Scripts to convert compiled SQL into mermaid markdown diagrams

![Alt text](img\sql_to_mermaid.png)

## Installation

Install virtual environment
```
pipenv install
```

Launch virtual environment
```
pipenv shell
```

Generate diagrams
```
python .\src\mermaid_generator.py "<input_sql_path>" "<output_mermaid_markdown_path>"
```

## Example
```
python .\src\mermaid_generator.py ".\src\data\example1.sql" ".\src\output\example1.md"
```
