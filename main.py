import pyarrow as pa
import pyarrow.csv as pcsv




def tokenize(query: str) -> list[str]:
    return   query.split(" ")


def execute_plan(plan: list[str]) -> pa.Table:
    
    
    return pcsv.read_csv("vgchartz-2024.csv", pcsv.Read)


if __name__ == "__main__":
    # print(execute_plan(tokenize(QUERY)))

    print(query_to_pb(QUERY))