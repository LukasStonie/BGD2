# Docker Setup
Starting the docker container

`docker run --name mongo mongo:8 `

Connect to the container

`docker exec -it mongo /bin/bash`

Start the mongo shell

`mongosh`

# Insert data

## Inserting users in the user table

### User 1
```
db.user.insertOne(
    {
        _id: "jakob@gmail.com", 
        fn: "Jakob"
    }
)
```

### User 2
```
b.user.insertOne(
  {
    _id: "marie@gmail.com", 
    fn: "Marie"
    }
)
```

## Inserting posts
### Post 1

```
db.post.insertOne(
  {
    header: "test",
    text:"ksdjfg", 
    user: "jakob@gmail.com"
  }
)
```

this post was created:

```
{
  acknowledged: true,
  insertedId: ObjectId('6731c591a844965df959139f')
}
```

### Post 2

```
db.post.insertOne(
  {
    header: "test2",
    text:"kdfsjwhgrsdjfg", 
    user: "jakob@gmail.com"
  }
)
```

this post was created: 

```
{
  acknowledged: true,
  insertedId: ObjectId('6731c5a6a844965df95913a0')
}
```

### Post 3
```
db.post.insertOne(
  {
    header: "Shitty Cars",
    text:"Dacia Sandero",
    user: "marie@gmail.com"
    }
  )
```

this post was created:

```
{
  acknowledged: true,
  insertedId: ObjectId('6731c5b9a844965df95913a1')
}
```

## Inserting likes
### Like 1
```
db.like.insertOne(
  {
    postId: ObjectId('6731c591a844965df959139f'), 
    type:5, 
    omment: "nice", 
    user: "jakob@gmail.com"
    }
  )
``` 

### Like 2
```
db.like.insertOne(
  {
    postId: ObjectId('6731c5a6a844965df95913a0'), 
    type:2, 
    comment: "perfect", 
    user: "jakob@gmail.com"
    }
  )
```

### Like 3
```
db.like.insertOne(
  {
    postId: ObjectId('6731c5a6a844965df95913a0'),
    type:1, 
    comment: "perfect <§", 
    user: "marie@gmail.com"
    }
)
```

# Aggregating the data

```
db.post.aggregate(
  {$lookup: 
    {
      from: "like", 
      localField: "_id", 
      foreignField:"postId", 
      as: "likes"
    }
  }
)
```

this leads to the following output:

```json
[
  {
    _id: ObjectId('6731c591a844965df959139f'),
    header: 'test',
    text: 'ksdjfg',
    user: 'jakob@gmail.com',
    likes: [
      {
        _id: ObjectId('6731c648a844965df95913a2'),
        postId: ObjectId('6731c591a844965df959139f'),
        type: 5,
        comment: 'nice',
        user: 'jakob@gmail.com'
      }
    ]
  },
  {
    _id: ObjectId('6731c5a6a844965df95913a0'),
    header: 'test2',
    text: 'kdfsjwhgrsdjfg',
    user: 'jakob@gmail.com',
    likes: [
      {
        _id: ObjectId('6731c69ca844965df95913a3'),
        postId: ObjectId('6731c5a6a844965df95913a0'),
        type: 2,
        comment: 'perfect',
        user: 'jakob@gmail.com'
      },
      {
        _id: ObjectId('6731c6cfa844965df95913a4'),
        postId: ObjectId('6731c5a6a844965df95913a0'),
        type: 1,
        comment: 'perfect <§',
        user: 'marie@gmail.com'
      }
    ]
  },
  {
    _id: ObjectId('6731c5b9a844965df95913a1'),
    header: 'Shitty Cars',
    text: 'Dacia Sandero',
    user: 'marie@gmail.com',
    likes: []
  }
]
```

We can also restrict the aggregation by using $match:

```
db.post.aggregate(
  [
    {
      $match: {
        header: "test"
        }
    },
    {
      $lookup: {
        from: "like", 
        localField: "_id", 
        foreignField:"postId", 
        as: "likes"
        }
    }
  ]
)
```

which produces the following output:

```json
[
  {
    _id: ObjectId('6731c591a844965df959139f'),
    header: 'test',
    text: 'ksdjfg',
    user: 'jakob@gmail.com',
    likes: [
      {
        _id: ObjectId('6731c648a844965df95913a2'),
        postId: ObjectId('6731c591a844965df959139f'),
        type: 5,
        comment: 'nice',
        user: 'jakob@gmail.com'
      }
    ]
  }
]
```

# Adding friends
```
db.friend.insert(
  {
    email:"jakob@gmail.com", 
    friend: "marie@gmail.com"
  }
)
```