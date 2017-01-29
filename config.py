class Config(object):
	"""
	Configurations that are common across all environments
	"""



class DevelopmentConfig(Config):
	"""
	Configurations for development
	"""
	DEBUG = True
	SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
	"""
	Configurations for live app
	"""
	DEBUG = False


app_config = {
	"development": DevelopmentConfig,
	"production": ProductionConfig
}