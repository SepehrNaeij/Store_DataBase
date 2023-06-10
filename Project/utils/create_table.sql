create table customer (
  customer_id serial primary key ,
  first_name varchar (250) ,
  last_name varchar (250) ,
  phone_number text ,
  address_id int , 
  validity int 
);

create table staff (
  staff_id serial primary key ,
  first_name varchar (250) ,
  last_name varchar (250) ,
  phone_number text ,
  address_id text,
  store_id int
);

create table address (
  address_id serial primary key ,
  postal_code varchar (200),
  country varchar (150) ,
  city varchar (150) ,
  exacte_address text 
);

create table store (
  store_id serial primary key ,
  name varchar (200),
  address_id int 
);

create table inventory (
  inventory_id serial primary key ,
  product_id  int ,
  store_id int ,
  number int
);

create table product (
  product_id serial primary key ,
  name varchar(250) , 
  price int,
  size int,
  brand varchar(250)
);


create table cart (
  cart_id serial primary key ,
  total_price int ,
  payment_id int ,
  customer_id int 
);

create table shopping_receipt (
  shopping_receipt_id serial primary key ,
  address_id int ,
  shopping_receipt_date date
);

create table cart_item (
  cart_item_id serial primary key ,
  price int ,
  quantity int ,
  cart_id int ,
  product_id int 
);
