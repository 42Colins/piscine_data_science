#!/bin/bash
for file in /mnt/subject/customer/*.csv; do
	filename=$(basename $file .csv)
	psql -U cprojean -d piscineds -h localhost -f /mnt/db.sql -v "file=$filename"
done