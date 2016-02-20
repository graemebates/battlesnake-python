import bottle
import os


@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')


@bottle.get('/')
def index():
    head_url = '%s://%s/static/suh.png' % (
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
        'taunt': 'aha asuh dude'
    }

x=0
@bottle.post('/move')
def move():
    data = bottle.request.json
    # TODO: Do things with data
    # if(x == 1):
    #     x = 0
    #     return {
    #         'move': 'north',
    #         'taunt': 'battlesnake-python!'
    #     }
    # if x==0:
    #     x=1
    #     return {
    #         'move': 'west',
    #         'taunt': 'battlesnake-python!'
    #     }
    # if (turtle):

    return {
     'move': 'east',
     'taunt': data[game]
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
