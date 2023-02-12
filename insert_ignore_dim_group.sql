-- (if new polling group) inserts records into dim_group
-- parameter: group_name
INSERT OR IGNORE INTO dim_group (group_name)
VALUES (?);