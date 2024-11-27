# Task 1
## Insert program data
```
db.program.insertOne(
    {
        _id: 'mbi',
        name: 'Medical- and Bioinformatics',
        semesters: 6,
        description: 'Something with biology I guess ....'
    }
);
db.program.insertOne(
    {
        _id: 'dse',
        name: 'Datascience- and Engineering',
        semesters: 4,
        description: 'Something with data I guess ....'
    }
);
```
## Insert student data
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

## Query for students in specific program
```
db.student.aggregate(
    [
        {
            $lookup:
            {
                from: 'program',
                localField: 'program',
                foreignField: '_id',
                as: 'program'
            }
        },
        {
            $match: {'program._id': {$eq: 'mbi'} }
        }
    ]
);
```

# Task 2
## Insert subject data
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
## Aggregate data
```
db.subject.aggregate(
    [
        {
            $lookup:
            {
                from: 'program',
                localField: 'program',
                foreignField: '_id',
                as: 'program'
            }
        },
        {
            $match: {'program._id': {$eq: 'mbi'} }
        }
    ]
);
```

# Task 4
## Add fields to subject
```
db.subject.updateOne(
    { _id: 'ALG5' },
    { $set: {semester: 5, credits: 3, description: 'some text ...'} }
);
db.subject.updateOne(
    { _id: 'BLT3' },
    { $set: {semester: 3, credits: 2, description: 'some text ...'} }
);
db.subject.updateOne(
    { _id: 'WEB4' },
    { $set: {semester: 4, credits: 1, description: 'some text ...'} }
);
db.subject.updateOne(
    { _id: 'BGD2' },
    { $set: {semester: 1, credits: 2, description: 'some text ...'} }
);
db.subject.updateOne(
    { _id: 'CO1' },
    { $set: {semester: 1, credits: 7, description: 'some text ...'} }
);
```

# Task 3
## Insert grade data
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

## Aggregate data
```
db.grade.aggregate(
    [
        {
            $lookup:
            {
                from: 'subject',
                localField: 'subject_id',
                foreignField: '_id',
                as: 'subject'
            }
        },
        {
            $lookup:
            {
                from: 'student',
                localField: 'student_id',
                foreignField: '_id',
                as: 'student'
            }
        },
        {
            $match: {'student._id': {$eq: 'jakobPeter@uni.com'} }
        },
        {
            $project: {
                'student_id':0,
                'subject_id':0
            }
        }
    ]
);
```