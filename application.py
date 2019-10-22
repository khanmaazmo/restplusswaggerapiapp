from flask import Flask
from flask_restplus import Api, Resource, fields

app = Flask(__name__)
api = Api(app)

a_language = api.model('Language', {'language': fields.String('The Language.')})
a_language2 = api.model('Languagesss', {'languagesss': fields.String('The Languagessss.')})

languages = []
python = {'language': 'Python'}
languages.append(python)


@api.route('/language')
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
