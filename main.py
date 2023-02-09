from aiohttp import web
from app.settings import config, BASE_DIR
from app.store.database.accessor import PostgresAccessor
import jinja2
import aiohttp_jinja2


def setup_accessor(application):
    application["db"] = PostgresAccessor()
    application["db"].setup(application)


def setup_config(application):
    application["config"] = config


def setup_routes(application):
    from app.forum.routes import setup_routes as setup_forum_routes
    setup_forum_routes(application)


def setup_external_libraries(application):
    aiohttp_jinja2.setup(application, loader=jinja2.FileSystemLoader("templates"))


def setup_app(application):
    setup_config(application)
    setup_accessor(application)
    setup_external_libraries(application)
    setup_routes(application)


app = web.Application()

if __name__ == '__main__':
    setup_app(app)
    web.run_app(app, host=config["common"]['host'], port=config["common"]["port"])
