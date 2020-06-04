#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    cache = {}
    route = []
    for ticket in tickets:
        if ticket.source not in cache:
            cache[ticket.source] = ticket.destination

    cur = "NONE"
    while True:
        for ticket in cache:
            # print(cur)
            if ticket == cur:
                route.append(cache[ticket])
                cur = cache[ticket]
                break
        # print(cache)
        if cache[ticket] == "NONE":
            break
    return route
