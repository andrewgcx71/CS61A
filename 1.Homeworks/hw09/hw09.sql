CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;

-- copy your solution from prev hw!
-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT name, size from dogs,sizes where height<=max and height>min;

-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT child from parents,dogs where parent=name order by -height;

-- Filling out this helper table is optional
CREATE TABLE siblings AS
  SELECT parents1.child as sb1, parents2.child as sb2, s1.size from size_of_dogs as s1, size_of_dogs as s2,parents as parents1,parents as parents2 where parents1.parent=parents2.parent and parents1.child!=parents2.child and parents1.child=s1.name and parents2.child=s2.name and s1.size=s2.size and parents1.child < parents2.child;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT sb1 || " and " || sb2 || " are " || size || " siblings" from siblings;
