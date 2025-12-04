import dlt

rules = {
    "rule1": "orderid is not null",
    "rule2": "Quantity > 0"
}

@dlt.table(
    name='my_table'
)
@dlt.expect_all(rules)
def read_orders_stream():
    return (
        spark.readStream.format("cloudFiles")
        .option("cloudFiles.format", "csv")
        .load("/Volumes/project_kankan/orders/orders_volume/data/")
    )