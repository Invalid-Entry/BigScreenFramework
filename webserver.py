import asyncio 
from aiohttp import web

import threading

import pygame

app = web.Application()
routes = web.RouteTableDef()

@routes.get("/")
async def handler(request):
    print("Hello")

    clacks = request.app['clacks']

    event_type = clacks.custom_events['MESSAGE']
    ev = pygame.event.Event(event_type, {'message': 'Something is there'})

    pygame.event.post(ev)

    return web.json_response('OK')

@routes.get("/api/stats/")
async def handler(request):
    print("Stats api called")

    clacks = request.app['clacks']

    data = {
        "fps": clacks.clock.get_fps()
    }

    return web.json_response(data)

async def main():
    app.add_routes(routes)
    
    web_runner = web.AppRunner(app)
    await web_runner.setup()

    site = web.TCPSite(web_runner, '0.0.0.0', 8080)
    await site.start()

    print("======= Serving on http://127.0.0.1:8080/ ======")

    await asyncio.sleep(100*3600)


def background_thread(clacks):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    app['clacks'] = clacks

    try:
        loop.run_until_complete(main())
    finally:
        loop.close()

def run_webserver(clacks):
    print('Starting WebThread')
    x = threading.Thread(target=background_thread, args=[clacks])
    x.start()
    print("Webserver Thread Started")