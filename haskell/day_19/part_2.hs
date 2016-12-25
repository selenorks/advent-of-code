import Debug.Trace
import Data.List.Zipper

nextN b 0
    | endp b = start b
    | otherwise = b

nextN b n 
    | endp b = start b `nextN` n
    | otherwise =  right b `nextN` (n-1)

elfStep b len step
    | len == 1 = cursor b
    | otherwise =
        let stepC = if step then 0 else 1 in
        elfStep (delete b `nextN`  stepC) (len-1) $ not step

elf k = 
    let pos = quot k 2 in
    let l = fromList [1..k] in
    let start = nextN l pos in
    elfStep start k True

main = do
    print $ elf 3001330
