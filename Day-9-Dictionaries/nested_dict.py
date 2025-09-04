capital = {
    "france":"paris",
    "germany":"berlin",
    "india":"delhi",
}

#nested dictionary
travel_log = {
    "france": ["paris", "lille", "dijon"],
    "germany": ["berlin", "hamburg", "stuttgart"],
}
print(travel_log)
print(travel_log["france"])
print(travel_log["france"][2])


#dictionary in dictionary
travel_log = {
    "france": {"cities_visited": ["paris", "lille", "dijon"], "total_visits": 12},
    "germany": {"cities_visited": ["berlin", "hamburg", "stuttgart"], "total_visits": 5},
}
print(travel_log)
print(travel_log["france"])
print(travel_log["france"]["cities_visited"])
print(travel_log["france"]["cities_visited"][1])
print(travel_log["france"]["total_visits"])