from healthtools_ec.app import app
from flask_assets import Environment, Bundle

assets = Environment(app)
assets.url_expire = False
assets.directory = '%s/public' % app.config.root_path
assets.load_path = ['assets']
assets.url = '/public'

assets.register('css',
                Bundle(
                    'css/bootstrap-3.2.0.min.css',
                    'css/bootstrap-theme-3.2.0.min.css',
                    'css/font-awesome-4.3.0.min.css',
                    'css/datepicker3.css',
                    'css/bootstrap-datetimepicker.min.css',
                    'css/daterangepicker-bs3.css',
                    'css/select2-3.4.8.css',
                    'css/select2-bootstrap-3.4.8.css',
                    'css/dropzone-3.10.2.css',
                    'css/freelancer.css',
                    Bundle(
                        'css/*.scss',
                        filters='pyscss',
                        output='css/app.%(version)s.css'),
                    output='css/all.%(version)s.css'))

assets.register('admin-css',
                Bundle(
                    'css/admin.css',
                ))

assets.register('maps-css',
                Bundle(
                    'css/leaflet-0.7.2.css',
                    output='css/maps.%(version)s.css'))

assets.register('js', Bundle(
    'js/jquery-1.10.2.min.js',
    'js/underscore-1.6.0.js',
    'js/bootstrap-3.2.0.min.js',
    'js/typeahead.bundle-0.10.2.min.js',
    'js/jquery-throttle-debounce.js',
    'js/ujs.js',
    'js/app.js',
    # 'js/uservoice.js',
    'js/person.js',
    'js/moment.min.js',
    'js/bootstrap-datepicker.js',
    'js/bootstrap-datetimepicker.min.js',
    'js/daterangepicker-1.3.5.js',
    'js/select2-3.4.8.min.js',
    'js/analysis.js',
    output='js/app.%(version)s.js'))

maps = Bundle(
    'js/d3.v3.min.js',
    'http://cdn.leafletjs.com/leaflet-0.7.2/leaflet.js',
    'js/maps.js')

charts = assets.register('charts',
                         Bundle(
                             'js/highcharts-4.0.1.js',
                             'js/sparklines.js',
                             output='js/charts.%(version)s.js'))

assets.register('dashboard',
                Bundle(
                    maps,
                    charts,
                    'js/dashboard/*.js',
                    output='js/dashboard.%(version)s.js'))

# Helper that is available in templates, and returns the
# urls to the named assets.
def assets_helper(*args, **kwargs):
    result = []
    for f in args:
        try:
            result.append(assets[f])
        except KeyError:
            result.append(f)

    bundle = Bundle(*result, **kwargs)
    with bundle.bind(assets):
        urls = bundle.urls()
    return urls


@app.context_processor
def webassets_processor():
    return dict(webassets=assets_helper)
