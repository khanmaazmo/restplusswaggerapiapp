from flask import Flask
from flask_restplus import Api, Resource, fields
from werkzeug.contrib.fixers import ProxyFix #added

#option 2 not recommended
#from werkzeug.contrib.fixers import ProxyFix
#app = Flask(__name__)
#app.wsgi_app = ProxyFix(app.wsgi_app)
#OR
#from werkzeug.middleware.proxy_fix import ProxyFix
#app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

#option 1
#@Property
#def specs_url(self):
#"""Monkey patch for HTTPS"""
#return url_for(self.endpoint('specs'), _external=True, _scheme='https')
#Api.specs_url = specs_url

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)  #added
api = Api(app) #, title='TodoMVC API', description='A simple TodoMVC API'
#name_space = app.namespace('main', description='Main APIs')

a_language = api.model('Language', {'language': fields.String('The Language.')})
a_language2 = api.model('Languagesss', {'languagesss': fields.String('The Languagessss.')})

#todo = api.model('Todo', {
#    'id': fields.Integer(readonly=True, description='The task unique identifier'),
#    'task': fields.String(required=True, description='The task details')
#})

languages = []
python = {'language': 'Python'}
languages.append(python)


@api.route('/language') #@ns.route('/language') if namespace is used
class Language(Resource):
    @api.expect(a_language2)
    def get(self):
        return languages

    @api.expect(a_language)
    def post(self):
        languages.append(api.payload)
        return {'result': 'Language added'}, 201


if __name__ == '__main__':
    app.run(debug=True)
