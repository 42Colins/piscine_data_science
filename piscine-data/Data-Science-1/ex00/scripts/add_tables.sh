#!/bin/bash
for file in /mnt/data/customer/data*; do
	filename=$(basename $file .csv)
	psql -U cprojean -d piscineds -h localhost -f /mnt/scripts/ex00/data_table.sql -v "file=$filename"
done
for file in /mnt/data/*.csv; do
	filename=$(basename $file .csv)
	psql -U cprojean -d piscineds -h localhost -f /mnt/scripts/ex00/items_table.sql -v "file=$filename"
done