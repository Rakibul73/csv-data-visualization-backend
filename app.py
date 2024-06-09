from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    trade_code = db.Column(db.String(10))
    date = db.Column(db.String(10))
    open = db.Column(db.Float)
    high = db.Column(db.Float)
    low = db.Column(db.Float)
    close = db.Column(db.Float)
    volume = db.Column(db.Integer)

    def serialize(self):
        return {
            'id': self.id,
            'trade_code': self.trade_code,
            'date': self.date,
            'open': self.open,
            'high': self.high,
            'low': self.low,
            'close': self.close,
            'volume': self.volume
        }


@app.route('/data_without_pagination', methods=['GET', 'POST'])
def data_without_pagination():
    if request.method == 'POST':
        new_data = request.get_json()
        db.session.add(Data(**new_data))
        db.session.commit()
        return jsonify(new_data), 201
    data = Data.query.all()
    return jsonify([d.serialize() for d in data])



@app.route('/data', methods=['GET', 'POST'])
def manage_data():
    if request.method == 'POST':
        new_data = request.get_json()
        db.session.add(Data(**new_data))
        db.session.commit()
        return jsonify(new_data), 201
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    data = Data.query.paginate(page=page, per_page=per_page, error_out=False)
    serialized_data = [d.serialize() for d in data.items]
    return jsonify({
        'data': serialized_data,
        'total_pages': data.pages,
        'total_items': data.total,
        'current_page': data.page
    })

@app.route('/data/<int:id>', methods=['PUT', 'DELETE'])
def update_data(id):
    data = Data.query.get(id)
    if request.method == 'PUT':
        for key, value in request.get_json().items():
            setattr(data, key, value)
        db.session.commit()
        return jsonify(data.serialize()), 200
    elif request.method == 'DELETE':
        db.session.delete(data)
        db.session.commit()
        return '', 204

if __name__ == '__main__':
    db.create_all() 
    app.run(debug=True)
