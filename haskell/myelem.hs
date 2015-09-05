-- write equivalent of elem using foldl
-- 'elem item collection' returns true if 'item' is in the 'collection', otherwise it returns false
-- constraints:  item must be instance of eq (we must be able to compare two things of type item)
--               collection must be instance of foldable ( we must be able to fold the collection)

module Elem where

elem item collection = foldl (\acc x -> (||) acc (item == x)) False collection 

