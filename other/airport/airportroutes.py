
def solution(airports: list[str], routes: list[list[str]], startingAirpot: str) -> int:
    res = 0
    numAiports = len(airports)
    airportIDs = {}
    airportRoutes = [[] for i in range(numAiports)]

    # map of airpot strings to IDs
    for i in range(numAiports):
        airportIDs[airports[i]] = i

    # create directed graph of airpots
    for rt in routes:
        airportRoutes[airportIDs[rt[0]]].append(airportIDs[rt[1]])

    # print(airportIDs)
    # print(airportRoutes)

    # LEFT OFF HERE
    # uses "strongly connected node algorithm" - Korasaju's algorithm


    return res

def main():
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

    res = solution(airports, routes, startingAirport)


if __name__ == "__main__":
    main()