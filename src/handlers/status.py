from aiohttp import web


class StatusView(web.View):

    async def get(self):
        return web.json_response({
            'status': 'OK'
        })
