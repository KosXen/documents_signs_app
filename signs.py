from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///em_signs.db'
db = SQLAlchemy(app)

class Sign(db.Model):
    id = db.Column(db.String(80), primary_key=True)
    signed_by = db.Column(db.String)
    tbs = db.Column(db.String)
    date_created = db.Column(db.Date)
    date_signed = db.Column(db.Date)

with app.app_context():
    db.create_all()


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')


@app.route('/create_record', methods=['POST'])
def create_record():
    # Get the input values from the form
    record_id = request.form['input_id']
    signed = request.form['signed']
    tbs_by = request.form['next']
    date_signed = request.form['date_signed']
    date_signed = datetime.strptime(date_signed, '%Y-%m-%d').date()

    # Check if a record with the given id already exists
    existing = Sign.query.filter_by(id=record_id).first()

    if existing:
        return render_template('create_record.html', flag=0, id=record_id)

    new_record = Sign(id=record_id, signed_by=signed, tbs=tbs_by, date_signed=date_signed, date_created=datetime.today())

    db.session.add(new_record)
    db.session.commit()

    return render_template('create_record.html', flag=1, id=record_id)


@app.route('/record_info', methods=['POST'])
def record_info():
    # Get the ID entered by the user from the form
    record_id = request.form['input_id']

    # Query the database for the record with the specified ID
    record = Sign.query.filter_by(id=record_id).first()

    # Check if the record exists
    if record:
        str = record.signed_by

        # If the record exists, render a template to display the record information
        return render_template('record_info.html', flag=0, record=record, signed=str)
    else:
        # If the record does not exist, return an error message
        return render_template('record_info.html', flag=1, id=record_id)


@app.route('/update_record', methods=['POST'])
def update():
    # Get the info provided by the user
    record_id = request.form['input_id']
    sf = request.form['signed']
    tbs = request.form['next']
    date_signed = request.form['date_signed']
    date_signed = datetime.strptime(date_signed, '%Y-%m-%d').date()

    # Query the database for the record with the specified ID
    record = Sign.query.filter_by(id=record_id).first()

    if record:
        record.tbs = tbs

        if record.signed_by:
            record.signed_by += ", " + sf
        else:
            record.signed_by = sf

        record.date_signed = date_signed

        db.session.commit()

        return render_template('update_record.html', flag=0, record=record)
    else:
        return render_template('update_record.html', flag=1, id=record_id)


@app.route('/delete', methods=['POST', 'DELETE'])
def delete_record():
    # Get the record id
    record_id = request.form['input_id']

    record = Sign.query.filter_by(id=record_id).first()

    # Check if record exists
    if record:
        return render_template('delete_confirmation.html', flag=0, record=record)
    else:
        return render_template('delete_confirmation.html', flag=1, id=record_id)

@app.route('/delete_confirmed', methods=['POST'])
def delete_confirmed():
    record_id = request.form['record_id']

    record = Sign.query.filter_by(id=record_id).first()

    db.session.delete(record)
    db.session.commit()

    return render_template('delete_record.html', flag=0, id=record_id)



@app.route('/all_records', methods=['POST'])
def all_info():
    # Get all records
    records = Sign.query.all()

    rec_list = list(records)

    # Print all records using all_records.html
    if len(rec_list) > 0:
        return render_template('all_records.html', flag=0, records=rec_list)
    else:
        return render_template('all_records.html', flag=1)


if __name__ == '__main__':
  app.run(debug=True, port=8000)

