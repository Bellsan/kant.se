from flask import Flask
from flask_assets import Environment, Bundle

def create_app(config='instance.config.DevelopmentConfig'):
    app = Flask(__name__)
    
    app.config.from_object(config)
    print(f"Environment: {app.config['ENV']}")
    print(f"Debug: {app.config['DEBUG']}")
    print(f"Secret key: {app.config['SECRET_KEY']}")
    
    from app.main.routes import main
    app.register_blueprint(main)
    
    assets = Environment(app)
    
    style_bundle = Bundle(
        'src/sass/style.scss',
        filters='scss,cssmin',
        depends='src/sass/*.scss',
        output='dist/css/style.min.css',
        extra={'rel': 'stylesheet/css'}   
    )
    js_bundle = Bundle(
        'src/js/main.js',
        filters='jsmin',
        output='dist/js/main.min.js'
    )

    assets.register('main_styles', style_bundle)
    assets.register('main_js', js_bundle)
    style_bundle.build()
    js_bundle.build()
    
    return app