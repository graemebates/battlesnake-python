import bottle
import os


@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')


@bottle.get('/')
def index():
    head_url = '%s://%s/static/head.png' % (
        bottle.request.urlparts.scheme,
        bottle.request.urlparts.netloc
    )

    return {
        'color': '#00ff00',
        'head': head_url
    }


@bottle.post('/start')
def start():
    data = bottle.request.json

    # TODO: Do things with data

    return {
        'taunt': 'battlesnake-python!'
    }


@bottle.post('/move')
def move():
    data = bottle.request.json
    bool foodMode = False
    # TODO: Do things with data

    if data.snakes.id[299642ef-7497-4b0b-9d46-5e8df951df5c].health < 30:
        foodMode = True

    if foodMode:
        directionsToFood = shortestCalcFoodDistance(data.food, data.snakes.id[299642ef-7497-4b0b-9d46-5e8df951df5c].coords[0]);

        if (directionsToFood[0] > 0):
            return {
                'move': 'west',
                'taunt': 'battlesnake-python!'
            }
        else if (directionsToFood[0] < 0):
            return {
                'move': 'east',
                'taunt': 'battlesnake-python!'
            }
        else if (directionsToFood[1] > 0):
            return {
                'move': 'north',
                'taunt': 'battlesnake-python!'
            }
        else if (directionsToFood[1] < 0):
            return {
                'move': 'south',
                'taunt': 'battlesnake-python!'
            }


@bottle.post('/end')
def end():
    data = bottle.request.json

    # TODO: Do things with data

    return {
        'taunt': 'battlesnake-python!'
    }


# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()
if __name__ == '__main__':
    bottle.run(application, host=os.getenv('IP', '0.0.0.0'), port=os.getenv('PORT', '8080'))


def calcDistance(coord, snakehead){
    int x = snakehead[0] - coord[0]
    int y = snakehead[1] - coord[1]
    return([x,y])
}

def shortestCalcFoodDistance(coord, snakehead){
    int distance = 100
    desiredFood = [0,0]
    for food in coord:
        int x = snakehead[0] - coord[0]
        int y = snakehead[1] - coord[1]
        if abs(x+y) < distance:
            int distnace = abs(x+y)
            desiredFood = [x,y]
    return desiredFood
}
