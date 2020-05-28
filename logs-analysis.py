#!/usr/bin/env python
"""Analysis of Newspaper website logs."""

import psycopg2


def main():
    """Display the results of each of the methods."""
    print('Newspaper Analysis')
    most_popular_articles()
    most_popular_authors()
    days_with_more_than_1_percent_error()
    print('End of Analysis')


def most_popular_articles():
    """Most popular three articles of all times."""
    db = psycopg2.connect(database="news")
    c = db.cursor()
    query = '''select articles.title, count(log.path) as views
    from articles, log
    where '/article/' || articles.slug = log.path
    group by articles.title
    order by views DESC
    limit 3;'''
    c.execute(query)
    rows = c.fetchall()
    print("Most popular three articles of all time:")
    for row in rows:
        print(' {} - {:,} views'.format(row[0],row[1]))
    print("")
    db.close()
    c.close()


def most_popular_authors():
    """Most popular article authors of all time."""
    db = psycopg2.connect(database="news")
    c = db.cursor()
    query = '''select authors.name, count(log.path) as views
    from authors, articles, log
    where '/article/' || articles.slug = log.path
    and authors.id = articles.author
    group by authors.name
    order by views DESC;'''
    c.execute(query)
    rows = c.fetchall()
    print("Most popular three authors of all time:")
    for row in rows:
        print(' {} - {:,} views'.format(row[0],row[1]))
    print("")
    db.close()
    c.close()


def days_with_more_than_1_percent_error():
    """Day(s) with more than 1% of requests that lead to errors."""
    db = psycopg2.connect(database="news")
    c = db.cursor()
    query = '''select to_char(date, 'DD FMMonth, YYYY') as date,
    ROUND(error_percent, 2) as error_percent
    from (
    select to_char(time, 'DD FMMonth, YYYY')::date as date,
    100* (count(path) filter (where status = '404 NOT FOUND')/
    count(path)::numeric) as error_percent
    from log
    group by to_char(time, 'DD FMMonth, YYYY')
    ) a
    where error_percent > 1;'''
    c.execute(query)
    rows = c.fetchall()
    print("Day(s) with more than 1% of requests that lead to errors:")
    for row in rows:
        print(' {} - {:.2f}% errors'.format(row[0],row[1]))
    print("")
    db.close()
    c.close()


if __name__ == '__main__':
    main()
