-- Insert code to create Database Schema
-- This will create your .db database file for use

drop table if exists 'user';
drop table if exists 'trip';
drop table if exists 'trip_user';


CREATE TABLE 'user' ( 
    'uid' integer primary key,
    'username' text not null, 
    'pw' text not null
);

CREATE TABLE `trip` (
	`trip_id`	INTEGER NOT NULL PRIMARY KEY,
	`trip_title`	TEXT NOT NULL,
	`destination`	TEXT NOT NULL
);

CREATE TABLE `trip_user` (
	--'trip_user_id' integer not null primary key autoincrement,
	`trip_id`	integer,
	`uid`	integer,
	FOREIGN KEY(`uid`) REFERENCES `user`(`uid`),
	FOREIGN KEY(`trip_id`) REFERENCES `trip`(`trip_id`)
);