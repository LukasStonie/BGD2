select * from movies limit 20;
select count(distinct(movieId)) from movies;
select count(distinct(movieId)) from movies where genres like "Horror";
select tag,count(tag) from tags group by tag order by count(tag) desc limit 10 ;
select variance(rating), movieId from ratings group by movieId,year(from_unixtime(unixtimestamp)) having year(from_unixtime(unixtimestamp)) = 2015 order by variance(rating) desc limit 10;
select title,counts.c from (select count(tag) as c, movieId as id from tags group by movieId) as counts join movies on movieId = counts.id order by counts.c desc limit 10;
select title,counts.c from (select count(tag) as c, movieId as id from tags where tag = "funny" group by movieId) as counts join movies on movieId = counts.id order by counts.c desc limit 15;

select m.title, ratings_count.rating from (select count(userId) as c ,movieId as id, avg(rating) as rating  from ratings group by movieId having count(userId) > 100) as ratings_count join movies as m on ratings_count.id = m.movieId order by ratings_count.rating desc limit 10;

select m.title, ratings_count.rating from (select count(userId) as c ,movieId as id, avg(rating) as rating  from ratings group by movieId having count(userId) > 10) as ratings_count join movies as m on ratings_count.id = m.movieId where genres like "Horror" order by ratings_count.rating desc;