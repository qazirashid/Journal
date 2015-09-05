module Circle where

type Radius=Float
type Xco   =Float
type Yco   =Float

data Circle = Vec Radius Xco Yco deriving (Show, Read)

getRadius :: Circle -> Radius
getRadius (Vec r x y )= r

incRadius :: Circle -> Circle
incRadius (Vec r x y) = (Vec (r+1.0) x y) 
