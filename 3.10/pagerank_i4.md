# Pagerank

## Task one

| i | Pr(1) | Pr(2) | Pr(3) |
| - | ----  | ----- | ----- |
| 0 | 0.333 | 0.333 | 0.333 |
| 1 | 0.475 | 0.333 | 0.192 |
| 2 | 0.355 | 0.454 | 0.192 |
| 3 | 0.406 | 0.351 | 0.243 |
| 4 | 0.406 | 0.395 | 0.199 |

## Task two

### recurive DFS processing order

```
S -> D -> B -> A -> C -(return to S)-> E -> F -> H -> J -> I -(return to E)-> G -> RETURN nothing
```

## Task three

### A

```
function DFS-r(G, v)

//Inputs: G is a graph, v is a starting node

        mark node v as visited

        for all neighbours u of v in G do

            if node u is not visited then
                if u property treasure = true do
                    return u
                Endif

                DFS-r(G, u) // recur

           Endif

        End do

End function
```

### B

```
function DFS-r(G, v, treasures)

//Inputs: G is a graph, v is a starting node
	if property x treasures = total treasures do
        return node
    Endif

    mark node v as visited

    for all neighbours u of v in G do
        if node u is not visited then
	        if node property treasure = true do
		        property x of treasures += 1
	        Endif
        DFS-r(G, u, treasures) // recur
        Endif
    Endfor
End do

End function
```

