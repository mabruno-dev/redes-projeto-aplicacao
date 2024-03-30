from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html, get_redoc_html
from route.public import Public

try:
    app = FastAPI(docs_url=None,
                  redoc_url=None,
                  title='RedesApi',
                  version='0.1')
    
    @app.get("/docs", include_in_schema=False)
    def overridden_swagger():
        return get_swagger_ui_html(openapi_url="/openapi.json",
                                   title='RedesApi - SwaggerUI',
                                   )
    #zswagger_favicon_url="./arquivos/logo.png"

    public_route = Public()
    app.include_router(public_route.person_router)

    
except Exception as E:
    print(f'Erro: {str(E)}')
    exit(0)