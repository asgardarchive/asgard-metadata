from flask import g, current_app

from asgard_sdk.core.api.meta import MetaAPI

def get_meta(func):
    def inner(*args, **kwargs):
        if "meta" not in g:
            config = current_app.config["config"]
            g.server = MetaAPI(config, connect=True)
            
            ret = func(*args, **kwargs)
        return ret
    return inner

def teardown_meta(exception):
    meta = g.pop("meta", None)

    if meta is not None:
        meta.disconnect()