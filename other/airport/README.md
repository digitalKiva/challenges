ref: https://www.youtube.com/watch?v=qz9tKlF431k

> Note: I watched this video and then I wanted to practice the concepts.

# Airport Route Connector

Given a list of airports (`airports`), 1-way routes between the airports (`routes`) and a starting airport (`startingAirpot`) determine the number of additional routes that will need to be added to ensure that a traveler can get to any of the airports from the starting airport.  The number of connections is not important.

# Examples

```
Inputs:
airports = ["BGI", "CDG", "DEL", "DOH", "DSM", "EWR", "EYW", "HND", "ICN", "JFK", "LGA", "LHR", "ORD", "SAN", "SFO", "SIN", "TLV", "BUD"]
routes = [
    ["DSM", "ORD"],
    ["ORD", "BGI"],
    ["BGI", "LGA"],
    ["SIN", "CDG"],
    ["CDG", "SIN"],
    ["CDG", "BUD"],
    ["DEL", "DOH"],
    ["DEL", "CDG"],
    ["TLV", "DEL"],
    ["EWR", "HND"],
    ["HND", "ICN"],
    ["HND", "JFK"],
    ["ICN", "JFK"],
    ["JFK", "LGA"],
    ["EYW", "LHR"],
    ["LHR", "SFO"],
    ["SFO", "SAN"],
    ["SFO", "DSM"],
    ["SAN", "EYW"],
]
startingAirport = "LGA"

Output: 3

for note the aiports to add would be:
- LGA, TLV
- LGA, SFO/SAN
- LGA, EWR
```
