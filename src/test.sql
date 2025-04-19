CREATE TABLE riders (
    id  SERIAL PRIMARY KEY NOT NULL,
    rider_name VARCHAR(30) NOT NULL DEFAULT 'John Doe',
    instructions VARCHAR(50) NOT NULL DEFAULT 'None',
    rating VARCHAR(3) NOT NULL DEFAULT '0.0',
    credit_card VARCHAR(16) NOT NULL DEFAULT 'abc123'
);

CREATE TABLE drivers (
    id  SERIAL PRIMARY KEY NOT NULL,
    driver_name VARCHAR(30) NOT NULL DEFAULT 'Jane Doe',
    instructions VARCHAR(50) NOT NULL DEFAULT 'None',
    rating VARCHAR(3) NOT NULL DEFAULT '0.0',
    make VARCHAR(16) NOT NULL DEFAULT 'mercedes',
    model VARCHAR(16) NOT NULL DEFAULT 'benz',
    duration VARCHAR(5) NOT NULL DEFAULT '0',
    license VARCHAR(10) NOT NULL DEFAULT 'abc123'
);

INSERT INTO drivers(driver_name, instructions, rating)
    VALUES ('Tom Magliozzi', 'Don''t drive like my brother', '3.2'),
            ('Ray Magliozzi', 'Don''t drive like my brother', '3.4');

INSERT INTO riders(rider_name, rating)
    VALUES ('Mike Easter', '4.3')