from pydantic import BaseModel


class RunAppConfig(BaseModel):
    host: str = '127.0.0.1'
    port: int = 8000
    reload: bool = True


class FastApiConfig(BaseModel):
    title: str = 'Clothing Store'
    description: str = 'Realization of vintage clothes'


class ApiVVersion(BaseModel):
    v1: str = '/v1'


class ApiPrefix(BaseModel):
    clothing: str = '/clothing'
    footwear: str = '/footwear'
    accessories: str = '/accessories'


class ApiTags(BaseModel):
    clothing: list = ['Clothing']
    footwear: list = ['Footwear']
    accessories: list = ['Accessories']


class ApiConfig(BaseModel):
    main_prefix: str = '/api'
    version: ApiVVersion = ApiVVersion()
    tags: ApiTags = ApiTags()
    prefix: ApiPrefix = ApiPrefix()
