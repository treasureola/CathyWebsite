DROP TABLE IF EXISTS users;
CREATE TABLE users (
  fname varchar(50) not null,
  llname varchar(50) not null,
  email varchar(50),
  password varchar(50) not null,
  primary key(email)
);

DROP TABLE IF EXISTS products;
CREATE TABLE products(
  p_name varchar(50) not null,
  id varchar(50) not null,
  price varchar(10),
  primary key(id)
);

DROP TABLE IF EXISTS cart;
CREATE TABLE cart(
  cp_email varchar(50) not null,
  cp_name varchar(50) not null,
  cp_price int(10),
  cp_id int(100),
  cp_quantity int(100),
  cpo_id varchar(50),
  primary key(cp_id),
  Foreign Key (cp_id) REFERENCES products(id)
);

DROP TABLE IF EXISTS orders;
CREATE TABLE orders(
  user_email varchar(50) not null,
  order_date varchar(15),
  order_time varchar(15),
  order_id varchar(8),
  primary key(order_id),
  foreign key(user_email) REFERENCES users(email),
  foreign key(order_id) REFERENCES cart(cpo_id)
);

-- PRAGMA foreign_keys=on;


INSERT INTO users VALUES('test', 'user', 'testuser@gmail.com', 'testpass');

INSERT INTO products VALUES('Meat-Pie(1 dozen)', '1Dozen', 10);
INSERT INTO products VALUES('Meat-Pie(2 dozen)', '2Dozen', 10);
