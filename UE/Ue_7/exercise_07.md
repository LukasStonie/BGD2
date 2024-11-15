# University Records 
This is the solution for the voluntary exercise 7. Both implementations (Cassandra & MongoDB) are done via the shell command in an appropiate docker image.

## Cassandra Implementation
### Docker Image
To use Cassandra, we use a docker image which can be installed by the command `docker pull cassandra:5`. We run the image by executing `docker run --name cassandra cassandra:5` and we connect to the running image (in a new terminal) by excuting `docker exec -it cassandra /bin/bash`. 

Once we are in the shell of the docker container we use `cqlsh` to start the Cassandra Query Language shell. Before we can get started, we create a keyspace:
```bash
CREATE KEYSPACE university WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};
```

In order to use the keyspace we just created, we use the command:
```bash
USE university;
```
### Solutions

#### Task 1
Create the table:
```
CREATE TABLE students_by_program (
    program_id TEXT,        
    matrikel_nr TEXT,       
    first_name TEXT,
    last_name TEXT,
    start_date DATE,
    PRIMARY KEY (program_id, matrikel_nr)
);
```


Insert some test data:
```
INSERT INTO students_by_program (program_id, matrikel_nr, first_name, last_name, start_date)
VALUES ('mbi', 'hubertMayer@uni.com', 'Hubert', 'Mayer', '2002-09-01');

INSERT INTO students_by_program (program_id, matrikel_nr, first_name, last_name, start_date)
VALUES ('mbi', 'jakobPeter@uni.com', 'Jakob', 'Peter', '2005-04-11');

INSERT INTO students_by_program (program_id, matrikel_nr, first_name, last_name, start_date)
VALUES ('dse', 'charlieSheen@uni.com', 'Charlie', 'Sheen', '1980-12-23');
```

Query the data

```
SELECT * FROM students_by_program WHERE program_id = 'mbi';

SELECT * FROM students_by_program WHERE program_id = 'dse';
```


#### Task 2
Create the table:
```
CREATE TABLE subjects_by_program (
    program_id TEXT,        
    subject_id TEXT,       
    PRIMARY KEY (program_id, subject_id)
);
```

Insert some test data:
```
INSERT INTO subjects_by_program (program_id, subject_id)
VALUES ('mbi', 'ALG5');

INSERT INTO subjects_by_program (program_id, subject_id)
VALUES ('mbi', 'BLT3');

INSERT INTO subjects_by_program (program_id, subject_id)
VALUES ('mbi', 'WEB4');

INSERT INTO subjects_by_program (program_id, subject_id)
VALUES ('dse', 'BGD2');

INSERT INTO subjects_by_program (program_id, subject_id)
VALUES ('dse', 'CO1');
```

Query the data:

```
SELECT * from subjects_by_program where program_id = 'mbi';

SELECT * from subjects_by_program where program_id = 'dse';
```

#### Task 3
Create the table:

```
CREATE TABLE grades_by_student (
    matrikel_nr TEXT,
    subject_id TEXT,       
    grade INT,
    PRIMARY KEY (matrikel_nr, subject_id)
);
```

Insert some data:

```
INSERT INTO grades_by_student (matrikel_nr, subject_id, grade)
VALUES ('jakobPeter@uni.com', 'ALG5', 5);

INSERT INTO grades_by_student (matrikel_nr, subject_id, grade)
VALUES ('charlieSheen@uni.com', 'WEB4', 1);

INSERT INTO grades_by_student (matrikel_nr, subject_id, grade)
VALUES ('jakobPeter@uni.com', 'CO1', 2);
```

Query the data:

```
SELECT * from grades_by_student where matrikel_nr = 'jakobPeter@uni.com';
```

#### Task 4
Create the table:

```
CREATE TABLE subjects_details (
    subject_id TEXT,
    program_id TEXT,       
    semester INT,
    credits INT,
    description TEXT,
    PRIMARY KEY (subject_id)
);
```

Insert some test data:
```
INSERT INTO subjects_details (subject_id, program_id, semester, credits, description)
VALUES ('ALG5', 'mbi',  5, 3, 'Algorithms in Bioinformatics' );

INSERT INTO subjects_details (subject_id, program_id, semester, credits, description)
VALUES ('BLT3','mbi', 3, 5, 'Biochemical Lab Course (you will brew beer)' );

INSERT INTO subjects_details (subject_id, program_id, semester, credits, description)
VALUES ('WEB4','mbi', 4, 1, 'Introduction to Server Side Web development' );

INSERT INTO subjects_details (subject_id, program_id, semester, credits, description)
VALUES ('BGD2','dse', 1, 2, 'Intorduction to Big Data (Redis, Cassandra, Mongo)' );

INSERT INTO subjects_details (subject_id, program_id, semester, credits, description)
VALUES ('CO1','dse',1, 7, 'Computational Intelligence (what is ML)' );
```

Query the data:

```
SELECT * from subjects_details where subject_id = 'ALG5';

SELECT * from subjects_details where subject_id = 'CO1';
```



## Mongo DB Implementation
### Docker Image
To use MongoDB, we use a docker image which can be installed by the command `docker pull mongo:8`. We run the image by executing `docker run --name mongo mongo:8` and we connect to the running image (in a new terminal) by excuting `docker exec -it mongo /bin/bash`. 

Once we are in the shell of the docker container we use `mongosh` to start the MongoDB shell. With `use universiy` we change to a new database.

### Solutions

#### Task 1

Insert the data:
```
db.student.insertOne(
    {
        _id: 'hubertMayer@uni.com',
        firstname: 'Hubert',
        lastname: 'Mayer',
        birthdate: new Date('2002-09-01'),
        program: 'mbi'
    }
);
db.student.insertOne(
    {
        _id: 'jakobPeter@uni.com',
        firstname: 'Jakob',
        lastname: 'Peter',
        birthdate: new Date('2005-04-11'),
        program: 'mbi'
    }
);
db.student.insertOne(
    {
        _id: 'charlieSheen@uni.com',
        firstname: 'Charlie',
        lastname: 'Sheen',
        birthdate: new Date('1980-12-23'),
        program: 'dse'
    }
);
```

Query the data:
```
db.student.find({program: 'mbi'});
db.student.find({program: 'dse'});
```

#### Task 2
Insert the data:
```
db.subject.insertOne(
    {
        _id: 'ALG5',
        program: 'mbi'
    }
);
db.subject.insertOne(
    {
        _id: 'BLT3',
        program: 'mbi'
    }
);
db.subject.insertOne(
    {
        _id: 'WEB4',
        program: 'mbi'
    }
);
db.subject.insertOne(
    {
        _id: 'BGD2',
        program: 'dse'
    }
);
db.subject.insertOne(
    {
        _id: 'CO1',
        program: 'dse'
    }
);
```

Query the data:
```
db.subject.find({program:'mbi'});
db.subject.find({program:'dse'});
```

#### Task 3

Inser the data:
```
db.grade.insertOne(
    {
        student_id: 'jakobPeter@uni.com',
        subject_id: 'ALG5',
        grade: 5
    }
);
db.grade.insertOne(
    {
        student_id: 'jakobPeter@uni.com',
        subject_id: 'CO1',
        grade: 2
    }
);
db.grade.insertOne(
    {
        student_id: 'charlieSheen@uni.com',
        subject_id: 'WEB4',
        grade: 1
    }
);
```

Query the data:
```
db.grade.find({student_id:'jakobPeter@uni.com'});
db.grade.find({student_id:'charlieSheen@uni.com'});
```

#### Task 4
Insert the data:
```
db.subject_detail.insertOne(
    {
        _id: 'ALG5',
        semester: 5,
        credits: 3,
        description: 'Algorithms in Bioinformatics'
    }
);
db.subject_detail.insertOne(
    {
        _id: 'BLT3',
        semester: 3,
        credits: 2,
        description: 'Biochemical Lab Course (you will brew beer)'
    }
);
db.subject_detail.insertOne(
    {
        _id: 'WEB4',
        semester: 4,
        credits: 1,
        description: 'Introduction to Server Side Web development'
    }
);
db.subject_detail.insertOne(
    {
        _id: 'BGD2',
        semester: 1,
        credits: 1,
        description: 'Intorduction to Big Data (Redis, Cassandra, Mongo)'
    }
);
db.subject_detail.insertOne(
    {
        _id: 'CO1',
        semester: 1,
        credits: 7,
        description: 'Computational Intelligence (what is ML)'
    }
);
```

Query the data:
```
db.subject.aggregate(
    {
        $lookup:
        {
            from: 'subject_detail',
            localField: '_id',
            foreignField: '_id',
            as: 'details'
        }
    }
);
```