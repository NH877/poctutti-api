CREATE TABLE "product" (
    "product_id" SERIAL PRIMARY KEY,
    "name" VARCHAR(250) NOT NULL,
    "amount" INT NOT NULL, 
    "price" FLOAT NOT NULL,
    "image" VARCHAR(500),
    "active" BOOLEAN NOT NULL
);

INSERT INTO "product" ("name", "amount", "price", "image", "active") VALUES 
('Pantalon', 
20, 
100,
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQFiU73x3eI4u0ik2VwKTQQOnvm3Uf2uqOvXOk8wDpl2UvSY6n3XtfvGOwFkQHCBI2zDDw&usqp=CAU',
true),
('Camisa', 
10,
40.5,
'https://http2.mlstatic.com/D_NQ_NP_851004-MCO48201125477_112021-W.jpg',
true),
('Zapatillas', 
5, 
150,
'https://media.revistagq.com/photos/609e50299939be743693371f/master/pass/air%20jordan%201%20.jpeg',
true),
('Medias', 
25, 
10.5,
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRg3QJOsl8GSGN3K6LkvfWnmnnABEJ_5YVFJcDDTXybYfEiupmiPX57OTaJ1f5bokHg2Gg&usqp=CAU',
false);