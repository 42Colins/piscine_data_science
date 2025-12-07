#!/bin/bash
for file in /mnt/subject/item/*.csv; do
	filename=$(basename $file .csv)
	psql -U cprojean -d piscineds -h localhost -f /mnt/items_table.sql -v "file=$filename"
done