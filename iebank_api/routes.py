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
    app.logger.debug('Route / called')
    return 'Hello, World!'

@app.route('/skull', methods=['GET'])
def skull():
    app.logger.debug('Route /skull GET called')
    text = 'Hi! This is the BACKEND SKULL! 💀 '
    text = text +'<br/>Database URL:' + db.engine.url.database
    if db.engine.url.host:
        text = text +'<br/>Database host:' + db.engine.url.host
    if db.engine.url.port:
        text = text +'<br/>Database port:' + db.engine.url.port
    if db.engine.url.username:
        text = text +'<br/>Database user:' + db.engine.url.username
    if db.engine.url.password:
        text = text +'<br/>Database password:' + db.engine.url.password
    return text


@app.route('/accounts', methods=['POST'])
def create_account():
    app.logger.debug('Route /accounts POST called')
    name = request.json['name']
    country = request.json['country']
    currency = request.json['currency']
    account = Account(name, currency, country)
    db.session.add(account)
    db.session.commit()
    return format_account(account)

@app.route('/accounts', methods=['GET'])
def get_accounts():
    app.logger.debug('Route /accounts GET')
    accounts = Account.query.all()
    return {'accounts': [format_account(account) for account in accounts]}

@app.route('/accounts/<int:id>', methods=['GET'])
def get_account(id):
    app.logger.debug('Route /accounts GET called with id: ' + str(id))
    account = Account.query.get(id)
    return format_account(account)

@app.route('/accounts/<int:id>', methods=['PUT'])
def update_account(id):
    app.logger.debug('Route /accounts PUT called with id: ' + str(id))
    account = Account.query.get(id)
    account.name = request.json['name']
    db.session.commit()
    return format_account(account)

@app.route('/accounts/<int:id>', methods=['DELETE'])
def delete_account(id):
    app.logger.debug('Route /accounts DELETE called with id: ' + str(id))
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
        'country': account.country,
        'status': account.status,
        'created_at': account.created_at
    }