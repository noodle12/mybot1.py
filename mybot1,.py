import operator

def closset_friend(pw, enemy):
    distances = {}
    distance1 = 0
    distance2 = 0
    distance3 = 0
    d1 = 1
    d2 = 1
    d3 = 1
    for planet in pw.my_planets():
        distances[planet.planet_id()] = pw.distance(planet, enemy)
        if(distances[planet.planet_id()] < distance1):
            d1 = planet.planet_id()
            distance1 = distances[planet.planet_id()]
        elif(distances[planet.planet_id()] < distance2):
            d2 = planet.planet_id()
            distance2 = distances[planet.planet_id()]
        elif(distances[planet.planet_id()] < distance3):
            d3 = planet.planet_id()
            distance3 = distances[planet.planet_id()]
#    if(d1.num_ships() > enemy.num_ships()*1.5):
#        return d1
#    if(d2.num_ships() > enemy.num_ships()*1.5):
#        return d2
#    if(d3.num_ships() > enemy.num_ships()*1.5):
#        return d3
    return d1


def get_grade(pw, planet1):
    for planet in pw.my_planets():
        if planet.planet_id() == closset_friend(pw, planet):
            return (planet1.growth_rate())/(pw.distance(planet, planet1)*planet1.num_ships())
    return 1000

def do_turn(pw):
    planets = {}
    planet1 = 1000
    planet2 = 1000
    planet3 = 1000
    low = 1000
    pl1 = 1
    pl2 = 1
    pl3 = 1
    for planet in pw.planets():
        planets[planet.planet_id()] = planet.num_ships()
        if planets[planet.planet_id()] < low:
            low = planets[planet.planet_id()]
    planets = {}
#    for planet in pw.enemy_planets():
#        if planet.num_ships() <= low:
#            pw.issue_order(closset_friend(pw, planet), planet, planet.num_ships() + closset_friend(pw, planet).num_ships()*0.2)
    for planet in pw.neutral_planets():
        planets[planet] = get_grade(pw, planet)
        if  planets[planet] < planet1:
            planet1 = planets[planet]
            pl1 = planet.planet_id()
        elif planets[planet] < planet2:
            planet2 = planets[planet]
            pl2 = planet.planet_id()
        elif planets[planet] < planet3:
            planet3 = planets[planet]
            pl3 = planet.planet_id()
    for planet in pw.my_planets():
        if(planet.num_ships() > 100) and len(pw.neutral_planets()) > 0:
            pw.issue_order(planet, pw.neutral_planets()[0],  planet.num_ships()*0.2)
            pw.issue_order(planet, pw.neutral_planets()[0],  planet.num_ships()*0.2)
            pw.issue_order(planet, pw.neutral_planets()[0],  planet.num_ships()*0.2)
    if len(pw.neutral_planets()) == 0:
        for planet in pw.my_planets():
            pw.issue_order(planet, pw.enemy_planets()[0],  planet.num_ships()*0.2)
            pw.issue_order(planet, pw.enemy_planets()[0],  planet.num_ships()*0.2)
            pw.issue_order(planet, pw.enemy_planets()[0],  planet.num_ships()*0.2)
    return
