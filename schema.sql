DROP TABLE IF EXISTS users;
CREATE TABLE users
(
    userid TEXT PRIMARY KEY,
    password TEXT NOT NULL
);

DROP TABLE IF EXISTS appointments;
CREATE TABLE appointments
(
    apptid INTEGER PRIMARY KEY AUTOINCREMENT,
    userid TEXT NOT NULL,
    apptdate TEXT NOT NULL,
    appttime TEXT NOT NULL,
    haircutname TEXT NOT NULL,
    price REAL NOT NULL
);

DROP TABLE IF EXISTS haircuts;
CREATE Table haircuts
(
    haircutid INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    description TEXT,
    image TEXT
);

DROP TABLE IF EXISTS reviews;
CREATE Table reviews
(
    reviewid INTEGER PRIMARY KEY AUTOINCREMENT,
    userid TEXT NOT NULL,
    review TEXT 
);

INSERT INTO haircuts (name, price, description,image)
VALUES
    ('Barcode',15,'With this haircut we shave a 30% discount code into your fringe for your next visit!','barcode.jpg'),
    ('The Chessboard',20.50,'Fancy a game anywhere you go? Dont just pull out your phone like everyone else, play from the top of your head!','chessboard.jpg'),
    ('Mowhawk',15,'Sleek,aerodynamic and cool, the ladies will love this!','coolmowhawk.jpg'),
    ('The Ed Sheeran',20.50,'Look like everyones favorite musician with this mop of ginger hair we swept off the floor!','ed-sheeran.jpeg'),
    ('Hairline Fade',5,'Go bald with confidence!','hairlinefade.jpg'),
    ('50/50',10,'This one is only available after hours when our barbers have had too much to drink','halfandhalf.jpg'),
    ('Headphones',15,'Cant afford real headphones? We will shave them into your hair!(music playback unavailable at this time.)','headphones.jpg'),
    ('Mid Life Crisis',10,'Wife giving you a hard time? This haircut paired with a newly purchase motorcycle or boat will show her','midlifecrisis.jpg'),
    ('Mushroom',15,'This haircut is perfect for our fungus fans out there,(contains spores that may be toxic if inhaled)','mushroom.jpg'),
    ('Reverse Mowhawk',10,'Not as sleek or aerodynamic as the normal mowhawk, but just as successful with the ladies!','reversemohawk.jpg'),
    ('Safety Sissors',5,'We use this haircut to train our new employees that we dont trust with adult scissors yet.','safetyscissors.jpg'),
    ('Straight Mop Taper',12,'This is perfect for people who have a hidden face on the back of their head!','straightmoptaper.jpg'),
    ('The Lady killer',2,'Get this cut at your own risk and prepare to be attacked by hundreds of girls','pete.jpg'),
    ('The Mark Burns',57,'For people with crippling insecurity','themarkburns.jpg');

