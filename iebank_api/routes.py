from flask import Flask, request
from iebank_api import db, app
from iebank_api.models import Account

@app.route('/')
def hello_world():
    # app.logger.debug('This is a debug log message')
    # app.logger.info('This is an information log message')
    # app.logger.warn('This is a warning log message')
    # app.logger.error('This is an error message')
    # app.logger.critical('This is a critical message')
    return 'Hello, World!'

@app.route('/skull', methods=['GET'])
def skull():
    text = 'Hi! This is the BACKEND SKULL! 💀 '
    text = text +'<br/>Database URL:' + db.session.bind.url.database
    if db.session.bind.url.host:
        text = text +'<br/>Database host:' + db.session.bind.url.host
    if db.session.bind.url.port:
        text = text +'<br/>Database port:' + db.session.bind.url.port
    if db.session.bind.url.username:
        text = text +'<br/>Database user:' + db.session.bind.url.username
    if db.session.bind.url.password:
        text = text +'<br/>Database password:' + db.session.bind.url.password
    return text


@app.route('/accounts', methods=['POST'])
def create_account():
    name = request.json['name']
    currency = request.json['currency']
    account = Account(name, currency)
    db.session.add(account)
    db.session.commit()
    return format_account(account)

@app.route('/accounts', methods=['GET'])
def get_accounts():
    accounts = Account.query.all()
    return {'accounts': [format_account(account) for account in accounts]}

@app.route('/accounts/<int:id>', methods=['GET'])
def get_account(id):
    account = Account.query.get(id)
    return format_account(account)

@app.route('/accounts/<int:id>', methods=['PUT'])
def update_account(id):
    account = Account.query.get(id)
    account.name = request.json['name']
    db.session.commit()
    return format_account(account)

@app.route('/accounts/<int:id>', methods=['DELETE'])
def delete_account(id):
    account = Account.query.get(id)
    db.session.delete(account)
    db.session.commit()
    return format_account(account)

def format_account(account):
    return {
        'id': account.id,
        'name': account.name,
        'account_number': account.account_number,
        'balance': account.balance,
        'currency': account.currency,
        'status': account.status,
        'created_at': account.created_at
    }