-- myfilter is a function that filters collections
-- myfilter :: (a -> Bool) -> [a] -> [a] 
--
-- 'myfitler criterion list' should return a new list 
-- that contain only those elments of 'list' that satisfy the 
-- 'criterion'. The criterion itself is a function with one arguments:
--  'criterion sample' returns True if 'sample' satifies the criterion
--  and returns False if the 'sample' does not satisfy the criterion.

-- The main idea is to fold the list from right. We start with [] empty list.
-- our accamulator is a list. We look at next element of input list and apply
-- criterion to it. It the outcome is True we append the element to 
-- accamulator list. If the outcome is false, we throw away the element.

myfilter cri list = foldr (\next acc -> if (cri next) then next:acc else acc) [] list
-- I test the code with
-- 'myfilter (<4) [1..10]' and the result was [1,2,3] which is correct.
--
