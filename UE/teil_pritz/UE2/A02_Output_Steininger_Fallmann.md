# Results assignment 2, HIVE
Project team: Lukas Fallmann, Lukas Steininger

## Querying the movie dataset
### Query 1
Select the first 20 movies
```
select * from movies limit 20;
```

#### Output
| ID  | Title                                   | Genres                                     |
|-----|-----------------------------------------|--------------------------------------------|
| 1   | Toy Story (1995)                        | Adventure, Animation, Children, Comedy, Fantasy |
| 2   | Jumanji (1995)                          | Adventure, Children, Fantasy               |
| 3   | Grumpier Old Men (1995)                 | Comedy, Romance                            |
| 4   | Waiting to Exhale (1995)                | Comedy, Drama, Romance                     |
| 5   | Father of the Bride Part II (1995)      | Comedy                                     |
| 6   | Heat (1995)                             | Action, Crime, Thriller                    |
| 7   | Sabrina (1995)                          | Comedy, Romance                            |
| 8   | Tom and Huck (1995)                     | Adventure, Children                        |
| 9   | Sudden Death (1995)                     | Action                                     |
| 10  | GoldenEye (1995)                        | Action, Adventure, Thriller                |
| 11  | American President, The (1995)          | Comedy, Drama, Romance                     |
| 12  | Dracula: Dead and Loving It (1995)      | Comedy, Horror                             |
| 13  | Balto (1995)                            | Adventure, Animation, Children             |
| 14  | Nixon (1995)                            | Drama                                      |
| 15  | Cutthroat Island (1995)                 | Action, Adventure, Romance                 |
| 16  | Casino (1995)                           | Crime, Drama                               |
| 17  | Sense and Sensibility (1995)            | Drama, Romance                             |
| 18  | Four Rooms (1995)                       | Comedy                                     |
| 19  | Ace Ventura:


### Query 2
How many movies are in the dataset?
```
select count(distinct(title)) from movies;
```
#### Output
9737

### Query 3
How many horror movies do we have in our data?
```
select count(distinct(title)) from movies where genres like 'Horror';
```
#### Output
167

### Query 4
What are the top 10 most frequent tags?
```
select tag, count(tag) from tags group by tag order by count(tag) desc limit 10;
```

#### Output
| Tag            | Count |
|---------------------|-------|
| In Netflix queue    | 131   |
| Atmospheric         | 36    |
| Superhero           | 24    |
| Thought-provoking   | 24    |
| Funny               | 23    |
| Surreal             | 23    |
| Disney              | 23    |
| Religion            | 22    |
| Psychology          | 21    |
| Dark comedy         | 21    |


### Query 5
Which 10 movies were the most controversial in 2015 (e.g., had the highest variance in ratings between 2015/01/01 and 2015/12/31)?
```
select movieId, VARIANCE(rating) from ratings group by movieId, year(from_unixtime(unixTimestamp)) having year(from_unixtime(unixTimestamp)) = 2015 order by VARIANCE(rating) desc Limit 10;
```

#### Output
| ID     | Rating Variance          |
|--------|------------------|
| 2288   | 5.0625          |
| 86320  | 4.0555555555555545 |
| 27611  | 3.7222222222222228 |
| 745    | 3.555555555555556  |
| 56941  | 3.3888888888888893 |
| 4992   | 3.1666666666666665 |
| 317    | 3.1666666666666665 |
| 120635 | 3.0625            |
| 6947   | 3.0625            |
| 4310   | 3.0625            |

### Query 6
Which movies (titles) are the 10 most frequently tagged and how often have they been tagged?
```
select title,counts.c from (select count(tag) as c, movieId as id from tags group by movieId order by count(tag)) as counts join movies on movieId = counts.id order by counts.c desc limit 10;
```
#### Output
| Title                                                    | Count |
|----------------------------------------------------------|-------|
| Pulp Fiction (1994)                                      | 181   |
| Fight Club (1999)                                        | 54    |
| 2001: A Space Odyssey (1968)                             | 41    |
| Léon: The Professional (a.k.a. The Professional) (Léon) (1994) | 35    |
| Eternal Sunshine of the Spotless Mind (2004)             | 34    |
| The Big Lebowski (1998)                                  | 32    |
| Donnie Darko (2001)                                      | 29    |
| Star Wars: Episode IV - A New Hope (1977)                | 26    |
| Inception (2010)                                         | 26    |
| Suicide Squad (2016)                                     | 19    |


### Query 7
Which 15 movies (titles) have been most frequently tagged with the label "funny"?
```
select title,counts.c from (select count(tag) as c, movieId as id from tags where tags.tag like 'funny' group by movieId order by count(tag)) as counts join movies on movieId = counts.id order by counts.c desc limit 15;
```

#### Output
| Title                                    | Count |
|------------------------------------------|-------|
| Step Brothers (2008)                     | 3     |
| Jumanji: Welcome to the Jungle (2017)    | 1     |
| The Big Short (2015)                     | 1     |
| Zombieland (2009)                        | 1     |
| Toy Story 2 (1999)                       | 1     |
| The Brothers Bloom (2008)                | 1     |
| The Croods (2013)                        | 1     |
| Game Night (2018)                        | 1     |
| Inside Llewyn Davis (2013)               | 1     |
| The Hangover (2009)                      | 1     |
| The Interview (2014)                     | 1     |
| Pulp Fiction (1994)                      | 1     |
| Guardians of the Galaxy (2014)           | 1     |
| Clueless (1995)                          | 1     |
| The Big Lebowski (1998)                  | 1     |

### Query 8
Which are the 10 best-rated movies (on average; list titles) with more than 100 ratings?
```
select m.title, ratings_count.rating from (select count(userId) as c ,movieId as id, avg(rating) as rating  from ratings group by movieId having count(userId) > 100) as ratings_count join movies as m on ratings_count.id = m.movieId order by ratings_count.rating desc limit 10;
```

#### Output
| Title                                      | Rating        |
|--------------------------------------------|---------------|
| The Shawshank Redemption (1994)           | 4.429022082018927 |
| The Godfather (1972)                       | 4.2890625     |
| Fight Club (1999)                          | 4.272935779816514 |
| The Godfather: Part II (1974)              | 4.25968992248062  |
| The Departed (2006)                        | 4.252336448598131 |
| Goodfellas (1990)                          | 4.25          |
| The Dark Knight (2008)                     | 4.238255033557047 |
| The Usual Suspects (1995)                  | 4.237745098039215 |
| The Princess Bride (1987)                  | 4.232394366197183 |
| Star Wars: Episode IV - A New Hope (1977)  | 4.231075697211155 |

### Query 9
Which are the highest rated "Horror" movies with more than 10 ratings?
``` 
select m.title, ratings_count.rating from (select count(userId) as c ,movieId as id, avg(rating) as rating  from ratings group by movieId having count(userId) > 10) as ratings_count join movies as m on ratings_count.id = m.movieId where genres like "%Horror5" order by ratings_count.rating desc;
```

#### Output
| Title                                                | Rating            |
|------------------------------------------------------|-------------------|
| The Shining (1980)                                   | 4.08256880733945  |
| Halloween (1978)                                     | 3.7222222222222223 |
| Get Out (2017)                                       | 3.6333333333333333 |
| Nosferatu (Nosferatu eine Symphonie des Grauens) (1922) | 3.53125           |
| Hellraiser (1987)                                    | 3.3666666666666667 |
| The Texas Chainsaw Massacre (1974)                   | 3.269230769230769 |
| Creepshow (1982)                                     | 3.0714285714285716 |
| Hostel (2005)                                        | 2.8636363636363638 |
