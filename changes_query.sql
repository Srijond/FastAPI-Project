CREATE TABLE users (
          id INTEGER NOT NULL AUTO_INCREMENT, 
          name VARCHAR(255), 
          email VARCHAR(255), 
          password VARCHAR(255), 
          PRIMARY KEY (id)
);

CREATE TABLE blogs (
          id INTEGER NOT NULL AUTO_INCREMENT, 
          title VARCHAR(255), 
          body VARCHAR(255), 
          PRIMARY KEY (id)
);