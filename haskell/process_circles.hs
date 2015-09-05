import Circle
main = do
        contents <- readFile "listofcircles"
        let cs = read contents :: [Circle]
        let output = map getRadius $ map incRadius cs
        writeFile "output.txt" ( unlines $map show output) 
convert :: String -> [Circle]
convert s = read s :: [Circle]
