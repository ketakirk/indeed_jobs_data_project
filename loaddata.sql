drop database if exists indeed_jobs;

create database indeed_jobs;
use indeed_jobs;

drop table if exists analyst_by_state_and_industry;

create table analyst_by_state_and_industry (
    statename varchar(2),
    industry varchar(100),
    total_jobs int
);

load data 
infile '/Users/rohan/Documents/code/data_analysis/projects/jobs_data/data/csv/jobs_by_state_and_industry.csv'
into table analyst_by_state_and_industry
fields terminated by ',';